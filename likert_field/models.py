#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

import likert_field.forms as forms


class LikertField(models.IntegerField):
    """A Likert field is simply stored as an IntegerField"""
    description = _('Likert item field')

    def __init__(self, *args, **kwargs):
        if 'null' not in kwargs and not kwargs.get('null'):
            kwargs['null'] = True
        super(LikertField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {
            'min_value': 0,
            'form_class': forms.LikertField
        }
        defaults.update(kwargs)
        return super(LikertField, self).formfield(**defaults)
