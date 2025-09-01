from django.urls import path
from .views import PostListCreateView

urlpatterns = [
    path('list-posts/', PostListCreateView.as_view(), name='post-list'),
]
