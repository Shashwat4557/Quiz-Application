from django.urls import path
from . import views
from django.contrib import admin

app_name = 'quiz'

from . import views

urlpatterns = [
    path(r'^$', views.home, name='home'),
    path(r'^user-home$', views.user_home, name='user_home'),
    path(r'^play/$', views.play, name='play'),
    path(r'^leaderboard/$', views.leaderboard, name='leaderboard'),
    path(r'^submission-result/(?P<attempted_question_pk>\d+)/', views.submission_result, name='submission_result'),
    path(r'^login/', views.login_view, name='login'),
    path(r'^logout/', views.logout_view, name='logout'),
    path(r'^register/', views.register, name='register'),

]
