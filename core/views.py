from django.shortcuts import render, get_object_or_404, redirect
from core.models import Post
from django.utils import timezone

from django.views.generic import (TemplateView,ListView,
                                  DetailView)

from django.urls import reverse_lazy

from django.db.models import Q 
from django.http import HttpRequest



class AboutView(TemplateView):
    template_name = 'core/about.html'


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')


def post_list_view(request):

    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

    if request.method == 'GET':
        query= request.GET.get('q')

        if query is not None:
            print('------- QUERY -----------', query)
            posts = Post.objects.filter(Q(title__icontains=query) | Q(text__icontains=query))

    return render(request, 'core/post_list.html', {'post_list':posts})

class PostDetailView(DetailView):
    model = Post

    context_object_name = 'post'
    template_name = 'core/post_detail.html'
