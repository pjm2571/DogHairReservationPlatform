from django import forms
from .models import ReviewPost

class PostForm(forms.ModelForm):
    class Meta: #Meta 클래스에는 사용할 모델과 모델의 속성을 적어야 한다.
        model = ReviewPost 
        fields = ['title', 'content','imgfile']

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['placeholder'] = '제목'
        self.fields['content'].widget.attrs['placeholder'] = '내용을 입력하세요'

