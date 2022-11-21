from django.shortcuts import render, redirect
from django.core.paginator import Paginator

from blog.core.forms import CommentForm
from blog.core.models import Article, Comment


def index(request):
    articles = Article.objects.all()[:4]
    context = {'articles': articles}
    return render(request, 'index.html', context)


def articles(request):
    if request.method == 'POST':
        headline = request.POST.get('headline')
        articles = Article.objects.filter(headline__icontains=headline)
        paginator = Paginator(articles, 1000)

    else:
        articles = Article.objects.all()
        paginator = Paginator(articles, 20)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'page_obj': page_obj}
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
