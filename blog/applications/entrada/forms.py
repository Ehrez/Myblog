from django import forms
from django.template.defaultfilters import default
from ckeditor.widgets import CKEditorWidget
from django.db import models
from django.forms import fields, widgets
#
from applications.users.models import User
from .models import Category, Entry

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = (
            'user',
            'category',
            'tag',
            'title',
            'resume',
            'content',
            'public',
            'image',
            'portada',
            'in_home',
        )
        widgets = {
            'tag': forms.CheckboxSelectMultiple(),
            'content': forms.CharField(widget=CKEditorWidget()),
        }