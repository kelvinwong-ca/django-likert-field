django-likert-field
===================

A Likert field for Django models. Useful for adding ratings star
functionality.

Installation
============

This package depends on Six the Python compatibility toolkit

::

    pip install six

::

    pip install django-likert-field


Basic usage
===========

Use in the same manner as a regular model field::

    # models.py
    from likert_field.models import LikertField
    class PetShopSurvey(models.Model):
        i_like_snakes = LikertField()

    # Renders in add.html
    #
    # jQuery star rating widget should be able to grab by 'likert-field' class
    #
    <label for="id_i_like_snakes">I like snakes:</label>
    <input id="id_i_like_snakes" type="text" name="i_like_snakes"
     class="likert-field" />

    # detail.html
    #
    # assume 'survey' is context object holding instance
    #
    {% load likert_fa_stars %}
    {{ survey.i_like_snakes|fa_stars4|safe }}

    # Renders in detail.html
    #
    # assuming one-star Likert item score
    #
    <i class='fa fa-star likert-star'></i> ... other stars maybe...

Bugs! Help!!
============

If you find any bugs in this software please report them via the Github
issue tracker [#]_ or send an email to code@kelvinwong.ca. Any serious
security bugs should be reported via email only.

.. [#] Django-likert-field issue tracker https://github.com/kelvinwong-ca/django-likert-field/issues

Thank-you
=========

Thank-you for taking the time to evaluate this software. I appreciate
receiving feedback on your experiences using it and I welcome code
contributions and development ideas.

http://www.kelvinwong.ca/coders
