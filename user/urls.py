from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.user_sign_up_view, name='register'),
    path('login/', views.user_login_view, name='login'),
    path('logout/', views.user_logout, name='logout'),
]
