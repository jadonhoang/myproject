from django.urls import path

from apps.core import views

urlpatterns = [
    path('', views.view_panels, name='home'),
    path('all_repos/', views.allrepos, name='all_repos'),
    path('repos_sizes/', views.repos_size, name='repos_sizes'),
    path('panel_details/<panel_id>', views.panel_details),
]
