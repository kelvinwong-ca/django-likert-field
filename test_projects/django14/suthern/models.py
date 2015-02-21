from django.db import models

from likert_field.models import LikertField


class MuffinModel(models.Model):
    fudge_is_yummy = LikertField()
    #cabbage_is_yummy = LikertField(max_value=4)
    item = LikertField('fudge beats everything')
    #seven = LikertField('seven is my lucky number', max_value=7)
    #ten = LikertField('ten is the best', max_value=10)

    # Parameters tests
    too_many_questions = LikertField(null=True, blank=True)
    #too_many_questions = LikertField()
    too_few_questions = LikertField(null=True)
    #too_few_questions = LikertField(null=False)
    questions_should_not_be_optional = LikertField(blank=True)
    #questions_should_not_be_optional = LikertField(blank=False)
