# coding: utf-8
# author: dlyapun

from django import forms
from django.forms import ModelForm
from force_blog.models import BlogPost, Category
from django_summernote.widgets import SummernoteWidget


class BlogPostForm(ModelForm):
    # text = forms.CharField(widget=SummernoteWidget())

    class Meta:
        model = BlogPost
        exclude = ['owner', 'date_publication', 'image', 'default_image',
                   'date_creation', 'rating', 'blog_edit', 'karma_users', 'files', ]

    def save_with_owner(self, *args, **kwargs):
        owner = kwargs.pop('owner')
        obj = super(BlogPostForm, self).save(commit=False)
        obj.owner = owner
        obj.save()
        return obj
