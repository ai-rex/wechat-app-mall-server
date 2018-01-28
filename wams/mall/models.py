# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Config(models.Model):
    key = models.CharField(max_length=20)
    value = models.CharField(max_length=200)


class User(models.Model):
    openid = models.CharField(max_length=200, db_index=True)
    session_key = models.CharField(max_length=200)
    token = models.CharField(max_length=200, db_index=True)


class Banner(models.Model):
    goods_id = models.IntegerField(db_index=True)
    pic_url = models.CharField(max_length=200)
