from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def articles(request):
    return render(request, 'articles.html')


def detail(request, pk):
    return render(request, 'detail.html')


def settings(request, pk):
    return render(request, 'settings.html')
