# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import template
from django.utils.safestring import mark_safe

from .likert_star_tools import render_stars


register = template.Library()

# Glyphicon halflings for Bootstrap courtesy http://glyphicons.com/
#
# Bootstrap glyphicon stars ver 2
star_set_2 = {
    'star': "<i class='icon-star likert-star'></i>",
    'unlit': "<i class='icon-star-empty likert-star'></i>",
    'noanswer': "<i class='icon-ban-circle likert-star'></i>"
}

# Bootstrap glyphicon stars ver 3
star_set_3 = {
    'star': "<i class='glyphicon glyphicon-star likert-star'></i>",
    'unlit': "<i class='glyphicon glyphicon-star-empty likert-star'></i>",
    'noanswer': "<i class='glyphicon glyphicon-ban-circle likert-star'></i>"
}

# Bootstrap glyphicon stars ver 3 for bootstrap-star-rating
star_set_3_bsr = {
    'star': "<i class='glyphicon glyphicon-star likert-star'></i>",
    'unlit': "<i class='glyphicon glyphicon-star-empty likert-star'></i>",
    'noanswer': "<i class='glyphicon glyphicon-minus-sign likert-star'></i>"
}


def bs_stars2(num, max_stars=5):
    """
    Stars for Bootstrap 2

    If num is not None, the returned string will contain num solid stars
    followed by max_stars - num empty stars
    """
    return mark_safe(render_stars(num, max_stars, star_set_2))

register.filter('bs_stars2', bs_stars2)


def bs_stars3(num, max_stars=5):
    """
    Stars for Bootstrap 3

    If num is not None, the returned string will contain num solid stars
    followed by max_stars - num empty stars
    """
    return mark_safe(render_stars(num, max_stars, star_set_3))

register.filter('bs_stars3', bs_stars3)


def bs_stars3_bsr(num, max_stars=5):
    """
    Stars for Bootstrap 3 w bootstrap-star-rating

    BSR uses a minus sign for an empty response

    If num is not None, the returned string will contain num solid stars
    followed by max_stars - num empty stars
    """
    return mark_safe(render_stars(num, max_stars, star_set_3_bsr))

register.filter('bs_stars3_bsr', bs_stars3_bsr)
