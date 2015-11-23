# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from likert_field.models import LikertField


class LikertModel(models.Model):
    test_is_the_best = LikertField()


class ParametersModel(models.Model):
    ice_cream_is_yummy = LikertField()
    # cabbage_is_yummy = LikertField(max_value=4)
    item = LikertField('ice cream beats cabbage')
    # seven = LikertField('seven is my lucky number', max_value=7)
    # ten = LikertField('ten is the best', max_value=10)

    questions_should_not_be_optional = LikertField(blank=False)
