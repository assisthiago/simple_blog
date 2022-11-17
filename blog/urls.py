from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

import blog.core.views

urlpatterns = [
    path('', blog.core.views.index),
    path('articles', blog.core.views.articles),
    path('articles/<uuid:pk>', blog.core.views.detail),
    path('profile/<uuid:pk>', blog.core.views.settings),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
