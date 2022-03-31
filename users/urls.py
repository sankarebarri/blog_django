from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('registration/', views.registration, name='registration'),
    path('profile/', views.profile, name='profile'),
    # path('newPost/', views.new_post, name='new-post'),
    path('newPost/', views.PostCreateView.as_view(), name='new-post'),
    path('article/<int:pk>/update', views.PostUpdateView.as_view(), name='update-article'),
    path('article/<int:pk>/delete', views.PostDeleteView.as_view(), name='delete-article'),

]
