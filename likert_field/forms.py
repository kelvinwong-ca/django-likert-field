#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core import validators
#from django.core.exceptions import ValidationError
from django.forms import fields
from django.utils.translation import ugettext_lazy as _

from .widgets import LikertTextField


class LikertField(fields.Field):
    widget = LikertTextField
    default_error_messages = {
        'invalid': _('Please rate how strongly you agree or disagree with '
                     'the statement.'),
    }

    def __init__(self, max_value=None, min_value=None, *args, **kwargs):
        self.max_value, self.min_value = max_value, min_value
        kwargs.setdefault('widget', self.widget)
        super(LikertField, self).__init__(*args, **kwargs)

        if max_value is not None:
            self.validators.append(validators.MaxValueValidator(max_value))
        if min_value is not None:
            self.validators.append(validators.MinValueValidator(min_value))
