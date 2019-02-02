from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView , DetailView , CreateView , UpdateView , DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin

def home(request):

    post = Post.objects.all()

    context = {
        'post' : post,
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
    model = Post
    fields = ['title' , 'content']
    template_name = 'post_create.html'


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




