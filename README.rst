django-likert-field
===================

A Likert field for Django models

Installation
============

::

    pip install django-likert-field


Basic usage
===========

Use in the same manner as a regular model field::

    from likert_field.models import LikertField
    class PetShopSurvey(models.Model):
        respondent = models.CharField(max_length=255)
        i_like_snakes = LikertField()
        parrots = LikertField("I like parrots.")
