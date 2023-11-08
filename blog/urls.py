from django.urls import path
from . import views
from .feeds import LatestPostsFeed

app_name = 'blog'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('general/<slug:link_slug>', views.general_info, name='general_info'),
    path('about/', views.about_page, name='about_page'),
    path('blog/', views.post_list, name='post_list'),
    path('blog/<slug:post>/', views.post_detail, name='post_detail'),
    path('blog/tag/<slug:tag_slug>/', views.post_list, name='post_list_tag'),
    path('homelab/', views.homelab_page, name='homelab_page'),
    path('services/', views.services_page, name='services_page'),
    path('metafaq/', views.metafaq_page, name='metafaq_page'),
    path('newsletter/', views.newsletter, name='newsletter'),
    path('mail/<slug:post>/', views.post_share, name='post_share'),
    path('feed/', LatestPostsFeed(), name='post_feed'),
]
