from django.urls import path
from . import views    #Manik

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home_url'),         #Manik pointing to views.py in current app
    #Any rference to integer after blog/ to land on view.detail
    path('<int:blog_id>/', views.detail, name='detail_url')
]