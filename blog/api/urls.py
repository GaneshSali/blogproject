from django.contrib import admin
from django.urls import path
from .views import PostListAPIView, PostDetailAPIView, PostUpdateAPIView, PostDeleteAPIView, PostCreateAPIView,\
    CommentListAPIView, CommentCreateAPIView, ApproveCommentView, CommentDetailAPIView

urlpatterns = [
    path('', PostListAPIView.as_view(),name='list'),
    path('<int:pk>', PostDetailAPIView.as_view(),name='detail'),
    path('<int:pk>/edit/',PostUpdateAPIView.as_view(),name='edit'),
    path('<int:pk>/delete/', PostDeleteAPIView.as_view(),name='remove'),
    path('create', PostCreateAPIView.as_view(),name='create'),
    path('<int:pk>/comments/', CommentListAPIView.as_view(),name='comment_list'),
    path('<int:pk>/add_comment/', CommentCreateAPIView.as_view() ,name='add_comment'),
    path('comment/<int:pk>/approve/', ApproveCommentView.as_view(),name='comment_approve'),
    path('comment/<int:pk>', CommentDetailAPIView.as_view(),name='comment_detail'),

]
