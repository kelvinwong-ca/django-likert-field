django-likert-field
===================

A Likert field for Django models. Useful for adding ratings star
functionality.

Installation
============

::

    pip install django-likert-field


Basic usage
===========

Use in the same manner as a regular model field::

    from likert_field.models import LikertField
    class PetShopSurvey(models.Model):
        i_like_snakes = LikertField()
        parrots = LikertField("i like parrots.")
