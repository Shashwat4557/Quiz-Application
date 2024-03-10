"""lets_quiz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.contrib import admin
# from quiz import views as quiz_views
from django.conf.urls import handler404, handler500
from django.conf import settings
from django.conf.urls.static import static
from quiz import *
import quiz
from django.shortcuts import render, get_object_or_404, redirect


import sys
sys.path.append('lets_quiz/quiz/views.py')

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'^', include('quiz.urls')),
]


def error_404(request, exception):
    data = {}
    return render(request, 'quiz/error_404.html', data)


def error_500(request):
    data = {}
    return render(request, 'quiz/error_500.html', data)

handler404 = error_404
handler500 = error_500


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
