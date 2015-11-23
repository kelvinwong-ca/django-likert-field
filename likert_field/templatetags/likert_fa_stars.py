# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import template

from .likert_star_tools import render_stars
from django.utils.safestring import mark_safe


register = template.Library()

# Font-awesome stars ver 3
star_set_3 = {
    'star': "<i class='icon-star likert-star'></i>",
    'unlit': "<i class='icon-star-empty likert-star'></i>",
    'noanswer': "<i class='icon-ban-circle likert-star'></i>"
}

# Font-awesome stars ver 4
star_set_4 = {
    'star': "<i class='fa fa-star likert-star'></i>",
    'unlit': "<i class='fa fa-star-o likert-star'></i>",
    'noanswer': "<i class='fa fa-ban likert-star'></i>"
}


def fa_stars3(num, max_stars=5):
    """
    Stars for Font Awesome 3

    If num is not None, the returned string will contain num solid stars
    followed by max_stars - num empty stars
    """
    return mark_safe(render_stars(num, max_stars, star_set_3))

register.filter('fa_stars3', fa_stars3)


def fa_stars4(num, max_stars=5):
    """
    Stars for Font Awesome 4

    If num is not None, the returned string will contain num solid stars
    followed by max_stars - num empty stars
    """
    return mark_safe(render_stars(num, max_stars, star_set_4))

register.filter('fa_stars4', fa_stars4)
