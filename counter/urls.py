from django.urls import path
from . import views

 
urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.login_page,name='login_page'),
    path('register/',views.register,name='register'),
    path('logout/',views.logout_page,name='logout_page'),
]