#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models.fields import Field
from django.test import SimpleTestCase

from likert_field.models import LikertField


class LikertFieldTestCase(SimpleTestCase):

    def setUp(self):
        pass

    def test_instantiation(self):
        item = LikertField()
        self.assertIsInstance(item, Field)

    def test_(self):
        item = LikertField()
        print(item)

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
