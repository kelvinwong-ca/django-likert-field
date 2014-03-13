#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import SimpleTestCase

from likert_field.templatetags.likert_star_tools import render_stars
from likert_field.templatetags.likert_fa_stars import fa_stars3, fa_stars4
from likert_field.templatetags.likert_bs_stars import bs_stars2, bs_stars3


class StarToolsTestCase(SimpleTestCase):

    def setUp(self):
        self.star_set = {
            'star': 's',
            'unlit': 'u',
            'noanswer': 'n'
        }

    def test_render_stars(self):
        max_test_stars = 50
        for max_stars in xrange(1, max_test_stars + 1):
            for num in xrange(max_stars + 1):
                stars = render_stars(num, max_stars, self.star_set)
                self.assertEqual(len(stars), max_stars)
                self.assertEqual(stars.count(self.star_set['star']), num)
                self.assertEqual(stars.count(self.star_set['unlit']), max_stars - num)

    def test_render_stars_none(self):
        stars = render_stars(None, 5, self.star_set)
        self.assertEqual(len(stars), 1)
        self.assertEqual(stars.count(self.star_set['noanswer']), 1)

    def test_render_stars_blank(self):
        stars = render_stars('', 5, self.star_set)
        self.assertEqual(len(stars), 1)
        self.assertEqual(stars.count(self.star_set['noanswer']), 1)

    def test_num_greater_than_max_error(self):
        num = 4
        max_stars = 3
        self.assertTrue(num > max_stars)
        stars = render_stars(4, 3, self.star_set)
        self.assertEqual(len(stars), max_stars)
        self.assertEqual(stars.count(self.star_set['star']), max_stars)
        self.assertEqual(stars.count(self.star_set['unlit']), 0)


class BootstrapTestCase(SimpleTestCase):

    def test_bs_stars2_render(self):
        num = 3
        expected_stars = (
            "<i class='icon-star likert-star'></i>"
            "<i class='icon-star likert-star'></i>"
            "<i class='icon-star likert-star'></i>"
            "<i class='icon-star-empty likert-star'></i>"
            "<i class='icon-star-empty likert-star'></i>")
        stars = bs_stars2(num)
        self.assertEqual(stars, expected_stars)

    def test_bs_stars2_render_parameters(self):
        num = 1
        max_stars = 3
        expected_stars = (
            "<i class='icon-star likert-star'></i>"
            "<i class='icon-star-empty likert-star'></i>"
            "<i class='icon-star-empty likert-star'></i>")
        stars = bs_stars2(num, max_stars)
        self.assertEqual(stars, expected_stars)

    def test_fa_stars2_render_noanswer(self):
        num = None
        expected_stars = "<i class='icon-ban-circle likert-star'></i>"
        stars = bs_stars2(num)
        self.assertEqual(stars, expected_stars)

    def test_bs_stars3_render(self):
        num = 1
        expected_stars = (
            "<i class='glyphicon glyphicon-star likert-star'></i>"
            "<i class='glyphicon glyphicon-star-empty likert-star'></i>"
            "<i class='glyphicon glyphicon-star-empty likert-star'></i>"
            "<i class='glyphicon glyphicon-star-empty likert-star'></i>"
            "<i class='glyphicon glyphicon-star-empty likert-star'></i>")
        stars = bs_stars3(num)
        self.assertEqual(stars, expected_stars)

    def test_bs_stars3_render_parameters(self):
        num = 1
        max_stars = 2
        expected_stars = (
            "<i class='glyphicon glyphicon-star likert-star'></i>"
            "<i class='glyphicon glyphicon-star-empty likert-star'></i>")
        stars = bs_stars3(num, max_stars)
        self.assertEqual(stars, expected_stars)

    def test_fa_stars3_render_noanswer(self):
        num = None
        expected_stars = "<i class='glyphicon glyphicon-ban-circle likert-star'></i>"
        stars = bs_stars3(num)
        self.assertEqual(stars, expected_stars)


class FontAwesomeTestCase(SimpleTestCase):

    def test_fa_stars3_render(self):
        num = 2
        expected_stars = (
            "<i class='icon-star likert-star'></i>"
            "<i class='icon-star likert-star'></i>"
            "<i class='icon-star-empty likert-star'></i>"
            "<i class='icon-star-empty likert-star'></i>"
            "<i class='icon-star-empty likert-star'></i>")
        stars = fa_stars3(num)
        self.assertEqual(stars, expected_stars)

    def test_fa_stars3_render_parameters(self):
        num = 1
        max_stars = 7
        expected_stars = (
            "<i class='icon-star likert-star'></i>"
            "<i class='icon-star-empty likert-star'></i>"
            "<i class='icon-star-empty likert-star'></i>"
            "<i class='icon-star-empty likert-star'></i>"
            "<i class='icon-star-empty likert-star'></i>"
            "<i class='icon-star-empty likert-star'></i>"
            "<i class='icon-star-empty likert-star'></i>")
        stars = fa_stars3(num, max_stars)
        self.assertEqual(stars, expected_stars)

    def test_fa_stars3_render_noanswer(self):
        num = None
        expected_stars = "<i class='icon-ban-circle likert-star'></i>"
        stars = fa_stars3(num)
        self.assertEqual(stars, expected_stars)

    def test_fa_stars4_render(self):
        num = 2
        expected_stars = (
            "<i class='fa fa-star likert-star'></i>"
            "<i class='fa fa-star likert-star'></i>"
            "<i class='fa fa-star-o likert-star'></i>"
            "<i class='fa fa-star-o likert-star'></i>"
            "<i class='fa fa-star-o likert-star'></i>")
        stars = fa_stars4(num)
        self.assertEqual(stars, expected_stars)

    def test_fa_stars4_render_parameters(self):
        num = 1
        max_stars = 4
        expected_stars = (
            "<i class='fa fa-star likert-star'></i>"
            "<i class='fa fa-star-o likert-star'></i>"
            "<i class='fa fa-star-o likert-star'></i>"
            "<i class='fa fa-star-o likert-star'></i>")
        stars = fa_stars4(num, max_stars)
        self.assertEqual(stars, expected_stars)

    def test_fa_stars4_render_noanswer(self):
        num = None
        expected_stars = "<i class='fa fa-ban likert-star'></i>"
        stars = fa_stars4(num)
        self.assertEqual(stars, expected_stars)
