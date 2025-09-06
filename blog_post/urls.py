from django.urls import path
from .views import PostListCreateView
from .views import PostDetailView

urlpatterns = [
    path('list-posts/', PostListCreateView.as_view(), name='post-list'),
    path('list-posts/<int:id>/', PostDetailView.as_view(), name='post-detail'),
]
