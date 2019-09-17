from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField, SerializerMethodField
from blog.models import Post, Comment

class PostCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['title','text']

class PostListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name = 'detail'
        )
    delete_url = HyperlinkedIdentityField(
        view_name = 'remove'
        )
    comment_url = HyperlinkedIdentityField(
        view_name = 'comment_list'
        )
    author = SerializerMethodField()
    comments_count = SerializerMethodField()
    class Meta:
        model = Post
        fields = ['url','delete_url','title','text','author','comments_count','create_date','comment_url']
    def get_author(self, obj):
        return str(obj.author.username)
    def get_comments_count(self, obj):
        return obj.comments.count()

class PostDetailSerializer(ModelSerializer):
    author = SerializerMethodField()
    class Meta:
        model = Post
        fields = '__all__'
    def get_author(self, obj):
        return str(obj.author.username)

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id','post','author','text','create_date','approved_comment']

class CommentCreateSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['author','text']

class CommentUpdateSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['approved_comment']
