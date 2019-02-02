from django.urls import path

from . import views
urlpatterns = [

    path('' , views.PostListAPIView.as_view() , name ='list' ),
    path('create/' , views.PostCreateView.as_view() , name ='create' ),
    path('<int:pk>/' , views.PostDetaliView.as_view() , name ='detail' ),
    path('delete/<int:pk>/' , views.PostDetaliView.as_view() , name ='delete' ),
    path('edit/<int:pk>/' , views.PostEditView.as_view() , name ='edit' ),

]