from django.contrib import admin

from blog.core.models import Article, Comment, Paragraph


class ParagraphAdmin(admin.StackedInline):
    model = Paragraph


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('headline', 'author', 'pub_date', 'created_at', 'updated_at',)
    inlines = [ParagraphAdmin,]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'created_at',)
