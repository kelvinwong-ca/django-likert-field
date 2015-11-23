# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.six import string_types


def render_stars(num, max_stars, star_set):
    """
    Star renderer returns a HTML string of stars

    If num is None or a blank string, it returns the unanswered tag

    Otherwise, the returned string will contain num solid stars
    followed by max_stars - num empty stars

    If num > max_stars, render max_stars solid stars

    star_set is a dictionary of strings with keys: star, unlit, noanswer
    """
    if num is None or (isinstance(num, string_types) and len(num) == 0):
        return star_set['noanswer']

    difference = int(max_stars) - int(num)
    if difference < 0:
        num = max_stars
        difference = 0

    return ''.join(
        star_set['star'] * int(num) + star_set['unlit'] * difference)
