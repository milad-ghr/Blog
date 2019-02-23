from rest_framework.generics import ListAPIView, RetrieveAPIView , DestroyAPIView , UpdateAPIView , CreateAPIView
from blog.models import Post
from .serializers import PostSerializer , PostCreateSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import redirect
from rest_framework import status
import os


class PostCreateView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer


class PostListAPIView(APIView):
    # queryset = Post.objects.all()
    # serializer_class = PostSerializer

    def get(self, request):
        queryset = Post.objects.all()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        print('aaaaa' + str(request.data))
        print ('bbbbb' + str(request.user) + 'ccccc' + str(request.user.id))
        request.data['author'] = request.user.id
        serializer = PostCreateSerializer(data=request.data)
        print ('iiiii' + str(serializer))
        if serializer.is_valid():
            serializer.save()
            return redirect("/api", status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)


class PostDetailView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDeleteView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostEditView(UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


def test():
    return 0