from django.urls import path, include
from blog import views

app_name = 'blog'

urlpatterns = [
    path('blog/', views.index, name='index'),
    path('detail/<int:pk>', views.detail, name='detail'),
    path('boardlist/', views.boardlist, name='boardlist'),
    path('post/create/', views.post_create, name='post_create'),
    #게시글 수정
    path('post/modify/<int:pk>/', views.post_modify,
         name='post_modify'),
    #게시글 삭제
    path('post/delete/<int:pk>/', views.post_delete,
         name='post_delete'),
]