from django import forms
from .models import FreePost

class PostForm(forms.ModelForm):
    class Meta:
        model = FreePost
        fields = ['title', 'content', 'image']

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['placeholder'] = '제목'
        self.fields['content'].widget = forms.Textarea(attrs={'placeholder': '내용을 입력하세요'})