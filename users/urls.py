from django.urls import path
from .views import register, user_login, user_list, user_update, user_delete, user_logout, user_create

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('', user_list, name='user_list'),
    path('logout/', user_logout, name='logout'),
    path('users/new/', user_create, name='user_create'),
    path('users/<int:pk>/edit/', user_update, name='user_update'),
    path('users/<int:pk>/delete/', user_delete, name='user_delete'),
]
