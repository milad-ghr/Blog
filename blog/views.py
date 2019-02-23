from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView , DetailView , CreateView , UpdateView , DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin
import logging
from blog.api.serializers import PostCreateSerializer
from rest_framework.response import Response
from rest_framework import status
import json
logger = logging.getLogger('blog')

def home(request):
    post = Post.objects.all()
    for i in post:
        d = {'title': i.title, 'content': i.content}
        logger.warning('', extra=d)
    context = {
        'post': post,
        'title': 'Home Page',
    }
    return render(request, 'home.html' , context)


class HomePostView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'post'
    ordering = ['-post_dated']
    paginate_by = 6


class DetailPostView(DetailView):
    model = Post
    template_name = 'post-detail.html'


class CreatePostView(LoginRequiredMixin , CreateView):
    logger.debug('Create')
    model = Post
    fields = ['title' , 'content']
    template_name = 'post_create.html'

    def post(self, request, *args, **kwargs):
        print('aaaaa' + str(request.POST))
        post = PostCreateSerializer(data=request.POST)
        if post.is_valid():
            post.save()
            return redirect('')
        else:
            return Response(post.errors , status=status.HTTP_400_BAD_REQUEST)

# Aslan Nafahmidam #
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdatePostView(LoginRequiredMixin , UserPassesTestMixin , UpdateView):
    model = Post
    fields = ['title' , 'content']
    template_name = 'post_create.html'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

# Aslan Nafahmidam #
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class DeletePostView(LoginRequiredMixin , UserPassesTestMixin ,DeleteView):
    model = Post
    template_name = 'post_confirm_delete.html'
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False



def about(request):
    return render(request, 'home.html' , { 'title': 'Home'})


def newpost(request):
    return render(request, 'home.html' , { 'title': 'Home'})


from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

@csrf_exempt
def j(request):
    if request.method == 'POST':
        receive = json.loads(request.body)
        sender = User.objects.filter(is_superuser=True).first()
        receive['sender'] = sender.username
        print ('aaaaaaaaaa' + str(receive))
        return HttpResponse('Received')
    else:
        return HttpResponse('get')

