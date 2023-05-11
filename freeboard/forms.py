from django import forms
from .models import FreePost

class PostForm(forms.ModelForm):
    class Meta:
        model = FreePost
        fields = ['title', 'content', 'image']
