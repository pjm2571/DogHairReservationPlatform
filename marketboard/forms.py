from django import forms
from .models import MarketPost

class PostForm(forms.ModelForm):
    class Meta:
        model = MarketPost
        fields = ['title', 'content', 'image']
