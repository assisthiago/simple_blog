from django.shortcuts import render

from blog.core.models import Article


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
        'comments': article.comments.all()
    }
    return render(request, 'detail.html', context)


def settings(request, pk):
    return render(request, 'settings.html')
