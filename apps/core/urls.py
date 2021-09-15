from django.urls import path

from apps.core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('all_repos/', views.allrepos, name='all_repos'),
    path('repos_sizes/', views.repos_size, name='repos_sizes'),
]
