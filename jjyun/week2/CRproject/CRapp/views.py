from webbrowser import get
from django.shortcuts import render, redirect, redirect, get_object_or_404
from .models import Blog
from django.utils import timezone
from .forms import BlogForm, BlogModelForm

def home(request):
    posts = Blog.objects.all()
    return render(request, 'index.html', {'posts':posts})

#html Form

#블로그 글 작성 html을 보여주는 함수
def new(request):
    return render(request, 'new.html')

def create(request):
    if(request.method == 'POST'):
        post = Blog()
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.date = timezone.now()
        post.save()
    return redirect('home')

# django modelform

def formC(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            post = Blog()
            post.title = form.cleaned_data['title']
            post.body = form.cleaned_data['body']
            post.save()
            return redirect('home')
    else:
        form = BlogForm()
    return render(request, 'form_C.html', {'form':form})

def modelformC(request):
    if request.method =='POST':
        form = BlogModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else: 
        form = BlogModelForm()
    return render(request, 'form_C.html', {'form':form})

def detail(request, blog_id):
    
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'blog_detail':blog_detail})