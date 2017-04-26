#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import template
from django.utils.safestring import mark_safe

from .likert_star_tools import render_stars


register = template.Library()

# http://zurb.com/playground/foundation-icon-fonts-3
#
# Foundation Icon Fonts 3
star_set_3 = {
    'star': "<i class='fi-star likert-star'></i>",
    'unlit': "<i class='fi-star fi-star-o likert-star'></i>",
    'noanswer': "<i class='fi-star fi-star-ban likert-star'></i>"
}




def fi_stars3(num, max_stars=5):
    """
    Stars for Foundation Icon Fonts

    If num is not None, the returned string will contain num solid stars
    followed by max_stars - num empty stars
    """
    return mark_safe(render_stars(num, max_stars, star_set_3))

register.filter('fi_stars3', fi_stars3)



