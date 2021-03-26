from django.urls import path
from .views import PostsList, LikeUnlikePost, PostDeleteView

app_name = 'posts'

urlpatterns = [
    path('', PostsList, name='Networking'),
    path('liked/', LikeUnlikePost, name='like-post-view'),
    path('<pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]