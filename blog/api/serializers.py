from rest_framework import serializers
from blog.models import Post


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'author',
            'content',
            'post_dated',
        ]


class PostCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields =(
            #'id',
            'title',
            'author',
            'content',
        )
