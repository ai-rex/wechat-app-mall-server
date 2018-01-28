# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import inspect

from django.contrib import admin
from django.db.models import Model

from mall import models


class CustomModelAdmin(admin.ModelAdmin):
    def __init__(self, model, admin_site):
        self.list_display = [f.name for f in model._meta.get_fields()]
        super(CustomModelAdmin, self).__init__(model, admin_site)


def auto_find_models(module):
    model_items = []
    attrs = dir(module)
    for attr in attrs:
        model_item = getattr(module, attr)
        if inspect.isclass(model_item) and issubclass(model_item, Model):
            model_items.append(model_item)
    return model_items


def register_models(model_items):
    for model_item in model_items:
        admin.site.register(model_item, CustomModelAdmin)


def auto_register_models(module):
    model_items = auto_find_models(module)
    register_models(model_items)


auto_register_models(models)
