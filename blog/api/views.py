from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, \
    DestroyAPIView, RetrieveDestroyAPIView
from .serializers import PostListSerializer, PostDetailSerializer, PostCreateUpdateSerializer, CommentSerializer,\
    CommentCreateSerializer, CommentUpdateSerializer
from django.shortcuts import get_object_or_404
from blog.models import Post, Comment
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from django.db.models import Q
from rest_framework.filters import SearchFilter,OrderingFilter

class PostListAPIView(ListAPIView):
    serializer_class = PostListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title']
    def get_queryset(self, *arg, **kwargs):
        queryset_list = Post.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                Q(title__icontains=query)|
                Q(text__icontains=query)
                ).distinct()
        return queryset_list


class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateUpdateSerializer
    permission_classes = [IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer

class PostUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateUpdateSerializer

class PostDeleteAPIView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer

class CommentListAPIView(ListAPIView):
    serializer_class = CommentSerializer
    def get_queryset(self):
        queryset = Comment.objects.filter(post=self.kwargs["pk"])
        return queryset

class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer
    def perform_create(self, serializer):
        obj = Post.objects.get(pk=self.kwargs["pk"])
        serializer.save(post=obj)

class ApproveCommentView(RetrieveUpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentUpdateSerializer

class CommentDetailAPIView(RetrieveDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
