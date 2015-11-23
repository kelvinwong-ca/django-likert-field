# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.forms import widgets


class LikertTextField(widgets.TextInput):
    """A Likert field represented as a text input"""

    def render(self, name, value, attrs=None):
        """
        Returns this Widget rendered as HTML, as a Unicode string.
        """
        rendered_attrs = {'class': 'likert-field'}
        if attrs:
            rendered_attrs.update(attrs)

        return super(LikertTextField, self).render(name, value, rendered_attrs)
