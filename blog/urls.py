from django.urls import path
from . import views
urlpatterns = [

    path('' , views.home , name = 'home' ),
    path('blog/<int:pk>/', views.DetailPostView.as_view(), name='post-detail'),
    path('blog/<int:pk>/update/', views.UpdatePostView.as_view(), name='post-update'),
    path('blog/<int:pk>/delete/', views.DeletePostView.as_view(), name='post-delete'),
    path('post/new', views.CreatePostView.as_view(), name='post-create'),
    path('j/', views.j, name='j'),

]