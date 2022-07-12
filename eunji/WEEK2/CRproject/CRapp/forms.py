from django import forms
from .models import Blog

class BlogForm(forms.Form): # 장고로부터 가져온 forms에서 Form을 상송받아와서 만들고자 함
    title = forms.CharField(label="제목")
    body = forms.CharField(widget=forms.Textarea, label="내용")

class BlogModelForm(forms.ModelForm): # froms 안에 ModelForm을 상속받은 클래스를 생성
    class Meta:
        model = Blog
        fields = ['title', 'body']
        labels = {
            'title' : '제목',
            'body' : '내용'
        }

# form 기능을 가져오는 명령어