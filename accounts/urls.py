from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('sign_up/',views.signup_view,name='sign_up'),
    path('home/',views.home_view,name='home'),
    path('login/',auth_views.LoginView.as_view(template_name = 'login.html'),name = 'login'),
    path('logout/',auth_views.LogoutView.as_view(),name = 'logout')
]
