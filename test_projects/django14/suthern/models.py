# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from likert_field.models import LikertField


class MuffinModel(models.Model):
    fudge_is_yummy = LikertField()
    # item = LikertField('fudge beats everything')

    # Parameters tests
    # too_many_questions = LikertField(null=True, blank=True)
    too_many_questions = LikertField(null=False, blank=False, default=3)
    # too_few_questions = LikertField(null=True)
    too_few_questions = LikertField(null=False, default=3)
    # questions_should_not_be_optional = LikertField(blank=True)
    questions_should_not_be_optional = LikertField(blank=False)
