#!/usr/bin/env python
from distutils.core import setup, Command
import os
import re
import sys

from likert_field import __version__


cmdclasses = dict()
README_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                           'README.rst')
long_description = open(README_PATH, 'r').read()


def setup_django():
    """Initialize apps for Django 1.7 and later"""
    import django
    try:
        django.setup()
    except AttributeError:
        pass


class DemoTester(Command):
    """Runs demonstration project tests"""

    user_options = []
    test_settings = {
        '1.4': 'test_projects.django14.django14.settings',
        '1.5': 'test_projects.django14.django14.settings',
        '1.6': 'test_projects.django14.django14.settings',
        '1.7': 'test_projects.django14.django14.settings',
        '1.8': 'test_projects.django18.django18.settings',
        '1.9': 'test_projects.django18.django18.settings',
    }

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        sys.dont_write_bytecode = True
        from django import get_version
        django_release = re.search(r'^\d\.\d', get_version()).group(0)
        test_settings_exist = django_release in self.test_settings.keys()
        try:
            dj_ver = [int(n) for n in re.split(r'[.ab]', get_version())]
        except ValueError:
            # Pre-release Djangos must be testable!!!
            dj_too_old = False
        else:
            dj_too_old = dj_ver < [1, 4, 2]

        if test_settings_exist is False or dj_too_old:
            print("Please install Django 1.4.19 - 1.9 to run the test suite")
            exit(-1)

        os.environ['DJANGO_SETTINGS_MODULE'] = self.test_settings[
            django_release]
        try:
            from django.core.management import call_command
        except ImportError:
            print("Please install Django 1.4.2 - 1.9 to run the test suite")
            exit(-1)

        setup_django()

        call_command('test', 'likert_test_app', interactive=False, verbosity=1)

        try:
            import south
        except ImportError:
            pass
        else:
            call_command('test', 'suthern', interactive=False, verbosity=1)


cmdclasses['test_demo'] = DemoTester


class Tester(Command):
    """Runs project unit tests"""

    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        sys.dont_write_bytecode = True
        os.environ['DJANGO_SETTINGS_MODULE'] = 'test_suite.settings_for_tests'
        setup_django()

        try:
            from django.utils.unittest import TextTestRunner, defaultTestLoader
        except ImportError:
            from unittest import TextTestRunner, defaultTestLoader

        from test_suite import (
            test_forms, test_models, test_templatetags, test_widgets)
        suite = defaultTestLoader.loadTestsFromModule(test_forms)
        suite.addTests(defaultTestLoader.loadTestsFromModule(test_models))
        suite.addTests(
            defaultTestLoader.loadTestsFromModule(test_templatetags))
        suite.addTests(defaultTestLoader.loadTestsFromModule(test_widgets))
        runner = TextTestRunner()
        result = runner.run(suite)
        if result.wasSuccessful() is not True:
            raise SystemExit(int(bool(result.errors or result.failures)))

cmdclasses['test'] = Tester

setup(
    name='django-likert-field',
    description='A Likert field for Django models',
    long_description=long_description,
    version=__version__,
    license='BSD',
    keywords=[
        'Likert', 'ratings', 'star-rating', 'star-classification', 'Django',
        'model-field', 'Django-Likert-Field'],
    author='Kelvin Wong',
    author_email='code@kelvinwong.ca',
    url='https://github.com/kelvinwong-ca/django-likert-field',
    classifiers=['Development Status :: 3 - Alpha',
                 # 'Development Status :: 4 - Beta',
                 'Environment :: Web Environment',
                 'Framework :: Django',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: BSD License',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python',
                 'Programming Language :: Python :: 2.6',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.2',
                 'Programming Language :: Python :: 3.3',
                 'Programming Language :: Python :: 3.4',
                 'Programming Language :: Python :: 3.5',
                 'Topic :: Internet :: WWW/HTTP'],
    packages=['likert_field', 'likert_field.templatetags'],
    cmdclass=cmdclasses
)
