from django.contrib import admin
from django.urls import path

import blog.core.views

urlpatterns = [
    path('', blog.core.views.index),
    path('articles', blog.core.views.articles),
    path('articles/<uuid:pk>', blog.core.views.detail),
    path('admin/', admin.site.urls),
]
