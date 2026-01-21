from django.urls import path
from .import views


urlpatterns = [
    path('', views.home, name="home"),
    path('home/', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('book/', views.book, name="book"),
    path('menu/', views.menu, name="menu"),
    path('menu/<int:pk>/', views.menu_detail, name="menu_detail"),
    # pr nambah link blog
    # Add the remaining URL path configurations here
]