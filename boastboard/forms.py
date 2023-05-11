from django import forms
from .models import BoastPost

class PostForm(forms.ModelForm):
    class Meta:
        model = BoastPost
        fields = ['title', 'content', 'image']
