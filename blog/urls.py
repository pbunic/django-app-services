from django.urls import path
from . import views
from .feeds import LatestPostsFeed

app_name = 'blog'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('about/', views.about_page, name='about_page'),
    path('soc/', views.soc_page, name='soc_page'),
    path('blog/', views.post_list, name='post_list'),
    path('blog/<slug:post>/', views.post_detail, name='post_detail'),
    path('tag/<slug:tag_slug>', views.post_list, name='post_list_tag'),
    path('mail/<slug:post>/', views.post_share, name='post_share'),
    path('comment/<slug:post>/', views.post_comment, name='post_comment'),
    path('feed/', LatestPostsFeed(), name='post_feed'),
    path('search/', views.post_search, name='post_search'),
    path('services/', views.services_page, name='services_page'),
]
