from django.urls import path
from .views import *




urlpatterns = [
    path('post_list/', PostListView.as_view(), name='post_list'),
    path('post_detail/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
]

















