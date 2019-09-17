from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(),name='post_list'),
    path('post/<int:pk>', views.PostDetailView.as_view(),name='post_detail'),
    path('about/', views.AboutView.as_view(),name='about'),
    path('post/create',views.PostCreateView.as_view(),name='post_create'),
    path('post/<int:pk>/edit/', views.PostUpdateView.as_view(),name='post_edit'),
    path('post/<int:pk>/remove/', views.PostDeleteView.as_view(),name='post_remove'),
    path('post/<int:pk>/comment/', views.add_comment_to_post,name='add_comment_to_post'),
    path('comment/<int:pk>/approve/', views.comment_approve,name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove,name='comment_remove'),

]
