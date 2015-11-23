# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models.fields import Field
from django.test import SimpleTestCase
from django.utils.six.moves import xrange

from likert_field.models import LikertField
from likert_field import forms


class LikertFieldTestCase(SimpleTestCase):

    def setUp(self):
        pass

    def test_instantiation(self):
        item = LikertField()
        self.assertIsInstance(item, Field)

    def test_null_set(self):
        """Unanswered questions are saved as NULL"""
        item = LikertField()
        self.assertTrue(item.null)

    def test_null_settable(self):
        item = LikertField(null=False)
        self.assertFalse(item.null)

    def test_blank_set(self):
        """By default, responses are not required"""
        item = LikertField()
        self.assertTrue(item.blank)

    def test_blank_settable(self):
        item = LikertField(blank=False)
        self.assertFalse(item.blank)

    def test_get_prep_value_int(self):
        item = LikertField()
        for value in xrange(1, 50+1):
            self.assertIsInstance(item.get_prep_value(value), int)

    def test_get_prep_value_strings(self):
        item = LikertField()
        for value in xrange(1, 50+1):
            self.assertIsInstance(item.get_prep_value(str(value)), int)

    def test_get_prep_value_negative_int(self):
        item = LikertField()
        self.assertIsInstance(item.get_prep_value(-1), int)
        self.assertEqual(item.get_prep_value(-1), 0)

    def test_get_prep_value_empty_string(self):
        item = LikertField()
        self.assertTrue(item.get_prep_value('') is None)

    def test_get_prep_value_null(self):
        item = LikertField()
        self.assertTrue(item.get_prep_value(None) is None)

    def test_formfield(self):
        item = LikertField()
        ff = item.formfield()
        self.assertEqual(ff.min_value, 0)
        self.assertIsInstance(ff, forms.LikertFormField)
