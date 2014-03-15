#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.forms import widgets
from django.test import SimpleTestCase
from django.utils.six.moves import xrange

from likert_field.widgets import LikertTextField


class LikertTextFieldTestCase(SimpleTestCase):

    def test_instantiation(self):
        w = LikertTextField()
        self.assertIsInstance(w, widgets.TextInput)