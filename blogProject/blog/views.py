from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.
def home(request):
    blogs = Blog.objects
    return render(request, 'home.html', {'blogs':blogs})
     # render라는 함수를 통해 페이지를 띄워줄 건데, home.html 파일을 띄워줄 것이고 
    # 이 때, blogs라고 이름 지은 객체도 함께 넘겨주도록 하겠다.

def detail(request, blog_id):
    #detail 페이지로 들어가면 그 게시글만의 본문 내용을 다 보여주어야 함.
    blog_detail = get_object_or_404(Blog, pk= blog_id) #특정 object 가져오기(없으면 404 에러)
    return render(request, 'detail.html', {'blog':blog_detail})
    # render라는 함수를 통해 페이지를 띄워줄 건데, home.html 파일을 띄워줄 것이고 
    # 이 때, blog라고 이름 지은 객체도 함께 넘겨주도록 하겠다.

def new(request):
    return render(request, 'new.html')
#C-new(새로운 글을 작성할 수 있는 공간 띄워주기)

