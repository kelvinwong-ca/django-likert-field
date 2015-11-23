# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.exceptions import ValidationError
from django.forms import fields
from django.test import SimpleTestCase
from django.utils.six.moves import xrange

from likert_field.forms import LikertFormField
from likert_field.widgets import LikertTextField


class LikertFormFieldTestCase(SimpleTestCase):

    def test_instantiation(self):
        ff = LikertFormField()
        self.assertIsInstance(ff, fields.Field)

    def test_widget_class(self):
        ff = LikertFormField()
        self.assertIsInstance(ff.widget, LikertTextField)

    def test_min_value(self):
        ff = LikertFormField()
        self.assertEqual(ff.min_value, 0)

    def test_valid_integer_values(self):
        """These are valid responses and should raise no failures"""
        ff = LikertFormField()
        for v in xrange(50+1):
            ff.clean(v)

    def test_valid_integer_string_values(self):
        """These are valid responses and should raise no failures"""
        ff = LikertFormField()
        for v in xrange(50+1):
            ff.clean(str(v))

    def test_invalid_value(self):
        ff = LikertFormField()
        with self.assertRaises(ValidationError) as cm:
            ff.clean("InvalidValue")

        self.assertEqual(
            cm.exception.messages[0],
            LikertFormField.default_error_messages['invalid'])

    def test_max_value_is_settable(self):
        ff = LikertFormField(max_value=5)
        ff.clean(ff.max_value)
        with self.assertRaises(ValidationError) as cm:
            ff.clean(ff.max_value+1)

        params = {'limit_value': ff.max_value}
        self.assertEqual(
            cm.exception.messages[0],
            LikertFormField.default_error_messages['max_value'] % params)

    def test_negative_value_raises_validation_error(self):
        ff = LikertFormField()
        negatives = [-1, '-1']
        for v in negatives:
            with self.assertRaises(ValidationError) as cm:
                ff.clean(v)

            params = {'limit_value': ff.min_value}
            self.assertEqual(
                cm.exception.messages[0],
                LikertFormField.default_error_messages['min_value'] % params)
