from django.contrib import admin
from django.urls import path

import blog.core.views

urlpatterns = [
    path('', blog.core.views.index),
    path('articles', blog.core.views.articles),
    path('admin/', admin.site.urls),
]
