# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.forms import fields
from django.utils.translation import ugettext_lazy as _

from .widgets import LikertTextField


class LikertFormField(fields.IntegerField):
    widget = LikertTextField
    default_error_messages = {
        'invalid': _('Please rate how strongly you agree or disagree with '
                     'the statement.'),
        'min_value': _(
            'Ensure your response is greater than or equal to '
            '%(limit_value)s.'),
        'max_value': _(
            'Ensure your response is less than or equal to %(limit_value)s.'),
    }

    def __init__(self, min_value=0, *args, **kwargs):
        kwargs.setdefault('widget', self.widget)
        kwargs.setdefault('min_value', min_value)
        super(LikertFormField, self).__init__(*args, **kwargs)
