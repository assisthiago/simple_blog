import uuid

from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    headline = models.CharField(max_length=100, verbose_name='cabeçalho')
    description = models.CharField(max_length=160, verbose_name='descrição')
    photo = models.ImageField(upload_to='img', max_length=256)
    pub_date = models.DateTimeField(null=True, default=None, verbose_name='publicação')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='atualizado em')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='autor')

    def __str__(self):
        return f'{self.headline} ({str(self.id)})'

    def __repr__(self):
        return self.headline

    class Meta:
        db_table = 'article'
        verbose_name = 'artigo'


class Paragraph(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100, verbose_name='título')
    content = models.CharField(max_length=800, verbose_name='parágrafo')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='atualizado em')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='paragraphs')

    def __str__(self):
        return str(self.id)

    def __repr__(self):
        return self.title

    class Meta:
        db_table = 'paragraph'
        verbose_name = 'parágrafo'


class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(max_length=256, verbose_name='e-mail')
    first_name = models.CharField(max_length=100, verbose_name='nome')
    last_name = models.CharField(max_length=100, verbose_name='sobrenome')
    content = models.CharField(max_length=800, verbose_name='comentário')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='criado em')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return str(self.id)

    def __repr__(self):
        return self.email

    class Meta:
        db_table = 'comment'
        verbose_name = 'comentário'
