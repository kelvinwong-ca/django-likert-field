#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from six import string_types

from django.db import models
from django.utils.encoding import force_text, python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

import likert_field.forms as forms


@python_2_unicode_compatible
class LikertField(models.IntegerField):
    """A Likert field is simply stored as an IntegerField"""
    description = _('Likert item field')

    def __init__(self, *args, **kwargs):
        if 'null' not in kwargs and not kwargs.get('null'):
            kwargs['null'] = True
        super(LikertField, self).__init__(*args, **kwargs)

    def __str__(self):
        return "%s" % force_text(self.description)

    def get_prep_value(self, value):
        """
        Perform preliminary non-db specific value checks and conversions.

        The field expects a number as a string (ie. '2'). Unscored fields are
        empty strings and are stored as NULL
        """
        if value is None:
            return None

        if isinstance(value, string_types) and len(value) == 0:
            return None

        return int(value)

    def formfield(self, **kwargs):
        defaults = {
            'min_value': 0,
            'form_class': forms.LikertField
        }
        defaults.update(kwargs)
        return super(LikertField, self).formfield(**defaults)
