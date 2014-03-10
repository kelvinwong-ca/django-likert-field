#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import SimpleTestCase

from likert_field.models import LikertField


class LikertFieldTestCase(SimpleTestCase):

    def setUp(self):
        pass

    def test_instantiation(self):
        item = LikertField()
        self.assertTrue(len(item.description) > 0)
