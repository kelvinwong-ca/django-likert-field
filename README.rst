*******************
django-likert-field
*******************

A Likert field for Django models. Useful for adding star-ratings
functionality.

.. figure:: https://github.com/kelvinwong-ca/django-likert-field/raw/master/docs/images/add_form_rendered.jpg

   Rendered using the Bootstrap-star-rating plugin for jQuery [#]_

.. [#] Bootstrap-star-rating https://github.com/kartik-v/bootstrap-star-rating

Why use this?
=============

Django-likert-field has the following benefits:

* Just a simple field type for your models (not much else)
* Doesn't make you add a new table full of stuff when you only need a field
* Includes useful and simple star rendering filters for Font Awesome and Bootstrap/Glyphicons halflings
* Includes a simple Django widget that generates HTML that is usable by jQuery star-ratings widgets

Installation
============

This package requires Django 1.4.2 or later. It can be installed in the usual manner with Pip::

    pip install django-likert-field

Then add the app to your list of installed apps::

    # settings.py
    #
    INSTALLED_APPS = (
        'likert_field',

        ...other apps...
    )

That's it. No 'syncdb' required. You can now attach the field to your models.

Basic usage
===========

Use in the same manner as a regular model field::

    # models.py
    #
    from likert_field.models import LikertField
    class PetShopSurvey(models.Model):
        i_like_snakes = LikertField()

In your add.html template::

    # add.html
    #
    <form method="post">
        {% csrf_token %}
        {{ form }}
        <button type="submit">Save</button>
    </form>

Renders HTML similar to this::

    # Renders a widget
    #
    # jQuery star-rating widget should be able to grab by 'likert-field' class
    #
    <label for="id_i_like_snakes">I like snakes:</label>
    <input id="id_i_like_snakes" type="text" name="i_like_snakes"
     class="likert-field" />

When retrieving your responses, use one of the provided Django filters::

    # detail.html
    #
    # assume 'survey' is the context object holding survey instance
    #
    {% load likert_fa_stars %}
    {{ survey.i_like_snakes|fa_stars4 }}

This will render stars for the framework you choose (Font Awesome 4 in this case)::

    # Renders stars
    #
    # assuming one-star Likert item score
    #
    <i class='fa fa-star likert-star'></i> ... other stars maybe...

LikertField in your Django models
=================================

By default, your LikertField has the following settings:

* User responses are optional (blank=True)
* Score is an integer from 0 to n
* Min value is zero (min_value=0)
* There is no max value (max_value=None)
* "No answer" is stored in the database as NULL

LikertField stores the score of your Likert item as a simple integer from zero to n. You can set a max_value if you like but one is not set by default. It is assumed that your item is a 5-point Likert item.

Place the field onto your model::

    # models.py
    #
    from django.db import models
    from likert_field.models import LikertField

    class PetShopSurvey(models.Model):
        i_like_snakes = LikertField()

If you require a response, you can set 'blank' to False::

    # models.py
    #
    from django.db import models
    from likert_field.models import LikertField

    class PetShopSurvey(models.Model):
        i_like_snakes = LikertField(blank=False)

.. warning::

   By default, users are not required to provide item responses so the field parameter 'blank' is True. If you want to make your item a required field, set 'blank' to False in your field definition.

If you require a score from one to seven from your user (a 7-point Likert item). You can set a combination of min and max values with blank set to False to force a response::

    # models.py
    #
    from django.db import models
    from likert_field.models import LikertField

    class PetShopSurvey(models.Model):
        i_like_snakes = LikertField(
            min_value=1,
            max_value=7,
            blank=False)

.. warning::

   If you need a 7-point Likert item (the default is assumed to be 5-point) you must configure the model field *and* the template tag. The value stored in the database is a plain integer with no knowledge of the item settings.

Forms
=====

This package includes a form field called LikertFormField. It can be used to create a Django form::

    # forms.py
    #
    from django.forms import Form
    from likert_field.forms import LikertFormField

    class SurveyForm(Form):
        i_like_snakes = LikertFormField()

This will render a form with the following HTML::

    <p>
      <label for="id_i_like_snakes">I like snakes:</label>
      <input id="id_i_like_snakes" type="text" name="i_like_snakes" class="likert-field" />
    </p>

Widget
======

There is also a simple widget named LikertTextField. It is essentially a TextInput widget that adds a class ("likert-field") to the generated HTML input::

    >>> from likert_field.widgets import LikertTextField
    >>> w = LikertTextField()

    >>> w.render('item_1', 3)
    u'<input type="text" name="item_1" value="3" class="likert-field" />'

    >>> w.render('item_1', None)
    u'<input type="text" name="item_1" class="likert-field" />'

Rendering Your Likert Fields
============================

Once the data is in the model, you can render the data by passing the model instance to the Django template via the template context in the regular manner. Once in the template, you can use one of the templatetags to render the integer data as a row of stars.::

    # in Django template detail.html
    #
    {% load likert_fa_stars %}
    {{ survey.i_like_snakes|fa_stars4 }}

    # It will render the following HTML
    <i class='fa fa-star likert-star'></i>...etc...

The general scheme is to filter the model field through the appropriate templatetag.

Bootstrap stars
---------------

.. figure:: https://github.com/kelvinwong-ca/django-likert-field/raw/master/docs/images/bs_stars_color_style.png

   The stars on Mac Chrome.

Bootstrap uses Glyphicon halflings for font icons. There is a templatetags set for Bootstrap::

    # in Django template detail.html
    #
    {% load likert_bs_stars %}
    {{ survey.i_like_snakes|bs_stars3 }}

    # It will render the following HTML
    <i class='glyphicon glyphicon-star likert-star'></i>...etc...

The two star types for Bootstrap 3 are::

    # A lit star
    <i class='glyphicon glyphicon-star likert-star'></i>

    # An unlit star
    <i class='glyphicon glyphicon-star-empty likert-star'></i>

You can add additional style to the star by using the 'likert-star' class::

    /* Color the star red comrade */
    .likert-star {
        color: #ff0000;
    }

The stars will then take on the color you want.

.. figure:: https://github.com/kelvinwong-ca/django-likert-field/raw/master/docs/images/bs_stars_red_style.png

   The red stars on Mac Chrome.

Font Awesome stars
------------------

Font Awesome is a popular font icon set. There is a templatetags set for it::

    # in Django template detail.html
    #
    {% load likert_fa_stars %}
    {{ survey.i_like_snakes|fa_stars4 }}

    # It will render the following HTML
    <i class='fa fa-star likert-star'></i>...etc...

The two star types for Font Awesome 4 are::

    # A lit star
    <i class='fa fa-star likert-star'></i>

    # An unlit star
    <i class='fa fa-star-o likert-star'></i>

You can add additional style to the star by using the 'likert-star' class::

    /* Color the star Foundation 5 blue */
    .likert-star {
        color: #008CBA;
    }

The stars will then take on the color you want.

.. figure:: https://github.com/kelvinwong-ca/django-likert-field/raw/master/docs/images/fa_stars_foundation_5_style.png

   The blue stars on Mac Chrome.

You can attach styles to the lit and unlit stars using standard methods::

    /* Gold stars wih outline */
    .fa.fa-star.likert-star {
        color: #ffd76e;
        text-shadow:-1px -1px 0 #e1ba53,
                     1px -1px 0 #e1ba53,
                    -1px  1px 0 #e1ba53,
                     1px  1px 0 #e1ba53;
        -webkit-text-stroke: 1px #e1ba53;
    }
    .fa.fa-star-o.likert-star {
        color: #c0c0c0;
    }

The stars will then take on the styles.

.. figure:: https://github.com/kelvinwong-ca/django-likert-field/raw/master/docs/images/fa_stars_deluxe_style.png

   The gold stars on Mac Chrome.

Rendering 7-point Likert item
=============================

Rendering a 7-point Likert (or an n-point Likert) is simple. Append the maximum number of stars to the filter as a parameter::

    {{ survey.i_like_snakes|bs_stars_3:7 }}

Filters available
=================

Bootstrap
---------

For Bootstrap 2 & 3::

    {% load likert_bs_stars %}

    # Bootstrap 2
    {{ survey.i_like_snakes|bs_stars_2 }}

    # Bootstrap 3
    {{ survey.i_like_snakes|bs_stars_3 }}

Font Awesome
------------

For Font Awesome 3 & 4::

    {% load likert_fa_stars %}

    # Font Awesome 3
    {{ survey.i_like_snakes|fa_stars3 }}

    # Font Awesome 4
    {{ survey.i_like_snakes|fa_stars4 }}

Sample application
==================

There is a sample application included if you downloaded the tarball. You can try it like this::

    $ pwd
    /home/user/teststuff/django-likert-field
    $ cd test_projects/django14
    $ python manage.py syncdb
    $ python manage.py runserver

    Validating models...

    0 errors found
    Django version 1.4.2, using settings 'django14.settings'
    Development server is running at http://127.0.0.1:8000/
    Quit the server with CONTROL-C.

Troubleshooting
===============

Django-likert-field contains two test suites. One is for the field and one is for an implementation of the field in a Django 1.4.2 project.

You can run the field tests by downloading the tarball and running 'test' in setup.py::

    $ python setup.py test

You can run the Django 1.4.2 demo test in a similar manner::

    $ python setup.py test_demo

Needless to say you will need to have Django 1.4.2 or later installed.

Bugs! Help!!
============

If you find any bugs in this software please report them via the Github
issue tracker [#]_ or send an email to code@kelvinwong.ca. Any serious
security bugs should be reported via email only.

.. [#] Django-likert-field issue tracker https://github.com/kelvinwong-ca/django-likert-field/issues

Links
=====

* https://pypi.python.org/pypi/django-likert-field/
* https://github.com/kelvinwong-ca/django-likert-field

Thank-you
=========

Thank-you for taking the time to evaluate this software. I appreciate
receiving feedback on your experiences using it and I welcome code
contributions and development ideas.

http://www.kelvinwong.ca/coders
