from django import forms
from .models import ReviewPost

class PostForm(forms.ModelForm):
    class Meta:
        model = ReviewPost
        fields = ['title', 'content', 'image']
