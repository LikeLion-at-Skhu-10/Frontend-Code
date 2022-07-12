from django import forms
from .models import Blog

class BlogForm(forms.Form):
    title = forms.CharField(label="제목")
    body = forms.CharField(widget=forms.Textarea, label="내용")

class BlogModelForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'body']
        labels = {
            'title' : '제목',
            'body' : '내용'
        }