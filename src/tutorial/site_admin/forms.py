from django import forms

from django_cbv_utils.forms import SetFromControlMixin
from tutorial.master.models import Category


class CategoryCreateForm(forms.ModelForm, SetFromControlMixin):

    class Meta:
        model = Category
        fields = [
            'order',
            'name',
        ]
