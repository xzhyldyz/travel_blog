from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView
# Create your views here.


class PostListView(ListView):
    model = Post
    template_name = 'pages/post_list.html'
    context_object_name = 'posts1'
    queryset = Post.objects.all().order_by('-created_at')


class PostDetailView(DetailView):
    model = Post
    template_name = 'pages/post_detail.html'
    context_object_name = 'post'
    queryset = Post.objects.all()

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['comments'] = Comment.objects.filter(post=self.object)
    #     return context






# def get_context_data(self, **kwargs):
#     context =
#
# def get_queryset(self):
#     queryset = super().get_queryset()
#     query = self.request.GET.get('query')
#     if query :
#         keyword = query.split()
#         q_object =





