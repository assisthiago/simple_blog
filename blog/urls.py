from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

import blog.core.views

urlpatterns = [
    path('', blog.core.views.index, name='index'),
    path('articles', blog.core.views.articles, name='articles'),
    path('articles/<uuid:pk>', blog.core.views.detail, name='detail'),
    path('articles/<uuid:pk>/comments', blog.core.views.comment, name='comment'),
    path('profile/<uuid:pk>', blog.core.views.settings, name='settings'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
