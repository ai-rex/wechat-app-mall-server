# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^config/get-value$', views.get_config, name='config'),
    url(r'^score/send/rule$', views.score, name='score'),
    url(r'^user/wxapp/login$', views.login, name='login'),
    url(r'^user/check-token$', views.check_token, name='check_token'),
    url(r'^banner/list$', views.banners, name='banners'),
]
