*******************
django-likert-field
*******************

A Likert field for Django models. Useful for adding ratings star
functionality.

.. figure:: https://github.com/kelvinwong-ca/django-likert-field/raw/master/docs/images/add_form_rendered.jpg

   Rendered using the Bootstrap-star-rating plugin for jQuery [#]_

.. [#] Bootstrap-star-rating https://github.com/kartik-v/bootstrap-star-rating

Installation
============

This package depends on Six the Python compatibility toolkit (assuming that Django 1.4 or later is already installed)::

    pip install six

It can be installed in the usual manner with Pip::

    pip install django-likert-field


Basic usage
===========

Use in the same manner as a regular model field::

    # models.py
    from likert_field.models import LikertField
    class PetShopSurvey(models.Model):
        i_like_snakes = LikertField()

    # Renders a widget in add.html
    #
    # jQuery star-rating widget should be able to grab by 'likert-field' class
    #
    <label for="id_i_like_snakes">I like snakes:</label>
    <input id="id_i_like_snakes" type="text" name="i_like_snakes"
     class="likert-field" />

    # detail.html Django template
    #
    # assume 'survey' is context object holding instance
    #
    {% load likert_fa_stars %}
    {{ survey.i_like_snakes|fa_stars4 }}

    # Renders in detail.html
    #
    # assuming one-star Likert item score
    #
    <i class='fa fa-star likert-star'></i> ... other stars maybe...

LikertField in your Django models
=================================

.. warning::

   If you need a 7-point Likert item (the default is 5) you must configure the model field *and* the template tag. The value stored in the database is a plain integer with no knowledge of the item settings.



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
