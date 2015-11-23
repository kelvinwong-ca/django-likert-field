# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.core.urlresolvers import reverse

from .models import ParametersModel


# Views
#
class SurveyListViewTestCase(TestCase):

    def test_view(self):
        response = self.client.get(reverse('likert_list'))
        self.assertEqual(response.status_code, 200)


class SurveyCreateViewTestCase(TestCase):

    def test_add_view(self):
        response = self.client.get(reverse('likert_add'))
        self.assertEqual(response.status_code, 200)

    def test_creation_full_valid(self):
        post_data = {
            'ice_cream_is_yummy': '5',
            'item': '3',
            'questions_should_not_be_optional': '1'
        }
        response = self.client.post(reverse('likert_add'), post_data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.has_header('location'))
        self.assertEqual(
            response['location'].count(reverse('likert_added')),
            1)

    def test_creation_null(self):
        post_data = {
            'ice_cream_is_yummy': '5',
            'item': '',
            'questions_should_not_be_optional': '5'
        }
        response = self.client.post(reverse('likert_add'), post_data)
        self.assertEqual(response.status_code, 302)
        surveys = ParametersModel.objects.all()
        self.assertEqual(len(surveys), 1)
        survey = surveys[0]
        self.assertTrue(survey.item is None)

    def test_creation_noanswer(self):
        post_data = {
            'ice_cream_is_yummy': '',
            'item': '',
            'questions_should_not_be_optional': ''
        }
        response = self.client.post(reverse('likert_add'), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.context['form'].errors[
                'questions_should_not_be_optional'],
            ['This field is required.'])

    def test_added_view(self):
        response = self.client.get(reverse('likert_added'))
        self.assertEqual(response.status_code, 200)


class SurveyDetailViewTestCase(TestCase):

    def setUp(self):
        survey = ParametersModel.objects.create(
            ice_cream_is_yummy=5,
            item=3,
            questions_should_not_be_optional=1)
        survey.save()
        self.survey = survey

    def test_valid_detail(self):
        response = self.client.get(
            reverse('likert_detail', kwargs={'pk': self.survey.pk}))
        self.assertEqual(response.status_code, 200)

    def test_invalid_detail(self):
        response = self.client.get(
            reverse('likert_detail', kwargs={'pk': 999}))
        self.assertEqual(response.status_code, 404)
