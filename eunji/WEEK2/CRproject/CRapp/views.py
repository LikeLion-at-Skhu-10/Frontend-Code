from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from django.utils import timezone
from .forms import BlogForm, BlogModelForm #forms에서 BlogForm 가져오기

def home(request):
    posts = Blog.objects.all()
    return render(request, 'index.html', {'posts':posts})

# 블로그 글 작성 html을 보여주는 함수
def new(request):
    return render(request, 'new.html')

# 블로그 글을 저장해주는 함수
def create(request):
    if(request.method == 'POST'): # 만약에 요청의 method가 POST라면
        post = Blog()
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.date = timezone.now()
        post.save()
    return redirect('home')

def formC(request): # 이 함수가 실행될 때
    if request.method == 'POST': # post 요청이 들어왔다면 밑에 입력 내용을 DB에 저장하는 작업을 할 것임
        form = BlogForm(request.POST) # form 안에 request 안에 있는 post 데이터들을 담아줌
        if form.is_valid(): # form 태그 안의 값이 유효하다면 아래부터 저장 시작해라
            post = Blog() # models.py 안에 저장한 Blog 객체를 가져오고
            post.title = form.cleaned_data['title'] # form으로 검증받은 데이터를 post라는 객체의 각 요소에 저장해줌
            post.body = form.cleaned_data['body']
            post.save()
            return redirect('home')
    else: # =new Get 요청 처리: 입력값을 받을 수 있는 html 띄워주기
        form = BlogForm()
    return render(request, 'form_C.html', {'form':form})

def modelformC(request):
    if request.method == 'POST':
        form = BlogModelForm(request.POST)
        if form.is_valid():
            form.save() # 자체적으로 save 할 수 있음
            return redirect('home')
    else:
        form = BlogModelForm()
    return render(request, 'form_C.html', {'form':form})
    
def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'blog_detail':blog_detail})
# Get과 post의 차이- post: 데이터를 생성하기 위한 요청 Get: 데이터를 받기 위한 요청