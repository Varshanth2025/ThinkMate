
from django.urls import path,include
from .import views

urlpatterns = [
    path('login/', views.LoginPage,name="login"),
    path('logout/', views.LogoutPage,name="logout"),
    path('register/', views.RegisterPage,name="register"),
    path('', views.home,name="home"),
    path('room/<str:pk>/', views.room,name="room"),
    path('profile/<str:pk>/', views.userProfile,name="user-profile"),
    path('create-room/', views.create_room,name="create-room"),
    path('update-room/<str:pk>/', views.update_room,name="update-room"),
    path('delete-room/<str:pk>/', views.delete_room,name="delete-room"),
    path('delete-message/<str:pk>/', views.deleteMessage,name="delete-message"),
]
