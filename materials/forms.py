# coding: utf-8
# author: dlyapun

from django import forms
from django.forms import ModelForm
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from materials.models import Material


class MaterialForm(ModelForm):
    text = forms.CharField(widget=SummernoteWidget())

    class Meta:
        model = Material
        exclude = ['owner', 'date_publication', 'date_creation',
                   'rating', 'karma_users', 'material_edit', 'if_comments']

    def save(self, *args, **kwargs):
        owner = kwargs.pop('owner')
        obj = super(MaterialForm, self).save(commit=False)
        obj.owner = owner
        obj.save()
        return obj
