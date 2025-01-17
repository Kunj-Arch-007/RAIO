from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signin/', views.loginRenderpage, name='signin'),  # Ensure correct name here for login URL
    path('signup/', views.signupRenderPage, name='signup'),
    path('logout/', views.logoutRenderPage, name='logout'),  # Logout URL
]
