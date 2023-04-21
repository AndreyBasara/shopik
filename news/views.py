from django.shortcuts import render, HttpResponse
from .models import Post




def news_detail(request, pk):
    news = Post.objects.get(pk=pk)
    context = {
        'post': news,
    }
    return render(request, 'news/blog-poste.html', context)


def news(request):
    news = Post.objects.all()
    context = {
        'posts': news,

    }
    return render(request, 'news/blog-v2.html', context)