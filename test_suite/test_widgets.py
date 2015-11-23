# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.forms import widgets
from django.test import SimpleTestCase

from likert_field.widgets import LikertTextField


class LikertTextFieldTestCase(SimpleTestCase):

    def test_instantiation(self):
        w = LikertTextField()
        self.assertIsInstance(w, widgets.TextInput)

    def test_has_likert_class(self):
        w = LikertTextField()
        tag = w.render('test', 1)
        self.assertEqual(tag.count('likert-field'), 1)
