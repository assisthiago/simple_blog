from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def articles(request):
    return render(request, 'articles.html')
