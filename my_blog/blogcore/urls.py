from django.urls import path
from . import views


app_name = 'blogcore'

urlpatterns = [
    path('posts/', views.post_list, name='post_list'),
    path('topic/<slug:tag_slug>', views.post_list, name='post_list_topic'),
    path('p/<slug:post>/', views.post_detail, name='post_detail'),
    path('mail/<slug:post>/', views.post_share, name='post_share'),
    path('comment/<slug:post>/', views.post_comment, name='post_comment'),
]
