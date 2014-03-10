#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from six import string_types

from django import template


register = template.Library()

# Font-awesome stars ver 4
unlit_star_4 = ("<i class='fa fa-star-o likert-star'></i>",)
star_4 = ("<i class='fa fa-star likert-star'></i>",)
unanswered_4 = "<i class='fa fa-ban likert-star'></i>"


def fa_stars4(num, max_stars=5):
    """
    Stars for Font Awesome 4

    If num is not None, the returned string will contain num solid stars
    followed by max_stars - num empty stars
    """
    if num is None or (isinstance(num, string_types) and len(num) == 0):
        return unanswered_4

    remainder = max_stars - int(num)
    return ''.join(star_4 * int(num) + unlit_star_4 * remainder)

register.filter('fa_stars4', fa_stars4)
