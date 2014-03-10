#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import template


register = template.Library()

# Bootstrap glyphicon stars ver 3
#
# Glyphicon halflings for Bootstrap courtesy http://glyphicons.com/
#
unlit_star_3 = ("<i class='glyphicon glyphicon-star-empty likert-star'></i>",)
star_3 = ("<i class='glyphicon glyphicon-star likert-star'></i>",)
unanswered_3 = "<i class='glyphicon glyphicon-ban-circle likert-star'></i>"


def bs_stars3(num, max_stars=5):
    """
    Stars for Bootstrap 3

    If num is not None, the returned string will contain num solid stars
    followed by max_stars - num empty stars
    """
    if num is None:
        return unanswered_3

    remainder = max_stars - int(num)
    return ''.join(star_3 * int(num) + unlit_star_3 * remainder)

register.filter('bs_stars3', bs_stars3)
