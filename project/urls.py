from django.contrib import admin
from django.urls import path , include
from django.contrib.auth import views as auth_view
from users import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('api/', include('blog.api.urls')),
    path('register/',  views.register , name = 'register'),
    path('profile/change_password', views.change_password, name='changepassword'),
    path('login/', auth_view.LoginView.as_view(template_name = "login.html"), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name = "logout.html"), name='logout'),
    path('profile/', views.profile, name='profile'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)