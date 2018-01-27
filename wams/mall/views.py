# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os

import requests
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from mall.models import Config, User
from wams import config


def generate_token():
    return os.urandom(32).encode('hex')


def ok(**kwargs):
    data = {
        'code': 0,
        'data': kwargs,
    }
    return JsonResponse(data)


def err():
    return JsonResponse({'code': 1})


def get_config(request):
    key = request.GET.get('key')
    conf = get_object_or_404(Config, key=key)
    return ok(value=conf.value)


def score(request):
    return err()


def login(request):
    code = request.GET.get('code')
    url = 'https://api.weixin.qq.com/sns/jscode2session?appid=%s&secret=%s&js_code=%s&grant_type=authorization_code'
    url = url % (config.APP_ID, config.SECRET, code)
    resp = requests.get(url)
    data = resp.json()
    try:
        user = User.objects.get(openid=data['openid'])
    except User.DoesNotExist:
        user = User()
        user.openid = data['openid']
        user.session_key = data['session_key']
        user.token = generate_token()
        user.save()
    return ok(uid=user.id, token=user.token)


def check_token(request):
    key = request.GET.get('token')
    user = get_object_or_404(User, token=token)
    return ok()
