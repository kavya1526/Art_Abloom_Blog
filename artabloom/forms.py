from django import forms
from . models import Blog

class edit_blog(forms.ModelForm):
    class Meta:
        model=Blog
        fields=('title','dsc')

class imageform(forms.ModelForm):
    class Meta:
        model=Blog
        fields='__all__'