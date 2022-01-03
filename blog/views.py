from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from blog.forms import PostForm
from blog.models import Post

def index(request):
    #블로그 메인 페이지
    return render(request, 'blog/index.html')

def boardlist(request):
    #Blog
    post_list = Post.objects.order_by('-pub_date')  #모든 자료 가져오기
    context = {'post_list':post_list}
    return render(request, 'blog/post_list.html', context)

def detail(request, pk):
    #블로그 상세 페이지
    post = get_object_or_404(Post, pk=pk)  #모든 자료 가져오기
    context = {'post':post}
    return render(request, 'blog/detail.html', context)

@login_required(login_url='common:login')
def post_create(request):
    #게시글 쓰기
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)    #폼에 입력된 자료 가져오기
        if form.is_valid():
            form = form.save(commit=False)  #가저장
            form.author = request.user
            form.pub_date = timezone.now()
            form.modify_date = timezone.now()
            form.save()     #실제 저장
            return redirect('blog:boardlist')   #등록후 블로그홈으로 경로 이동
    else:
        form = PostForm()   #비어있는 폼
    context = {'form':form}
    return render(request, 'blog/post_form.html', context)

@login_required(login_url='common:login')
def post_modify(request, pk):
    #게시글 수정
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES,  instance=post)
        if form.is_valid():
            post = form.save(commit=False)  #수정된 질문 가저장
            post.author = request.user      #세션 발급
            post.modify_date = timezone.now() #수정일
            post.save()
            return redirect('blog:detail', pk=post.id)
    else:
        form = PostForm(instance=post)  #instance를 쓰면 폼에 내용이 채워짐
    return render(request, 'blog/post_form.html', {'form':form})

@login_required(login_url='common:login')
def post_delete(request, pk):
    #게시글 삭제
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('blog:index')