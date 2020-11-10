from django.urls import path, include

from home import views
urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.user_login, name='user_login'),
    path('logout', views.user_logout, name='user_logout'),
    path('signup', views.register, name='user_signup')


]