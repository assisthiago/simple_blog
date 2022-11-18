from django.shortcuts import render, redirect

from blog.core.forms import CommentForm
from blog.core.models import Article, Comment


def index(request):
    articles = Article.objects.all()[:4]
    context = {'articles': articles}
    return render(request, 'index.html', context)


def articles(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'articles.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
        'paragraphs': article.paragraphs.all(),
        'comments': article.comments.all(),
        'form': CommentForm()
    }

    return render(request, 'detail.html', context)


def comment(request, pk):
    form = CommentForm(request.POST)
    if form.is_valid():
        form.cleaned_data['article'] = Article.objects.get(pk=pk)
        Comment(**form.cleaned_data).save()

    return redirect('detail', pk=pk)


def settings(request, pk):
    return render(request, 'settings.html')
