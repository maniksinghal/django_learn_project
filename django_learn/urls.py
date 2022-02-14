"""django_learn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from pwd_generator import views    #Manik
from mysite_portfolio import portfolio_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('form/', views.form),         #Manik pointing to views.py in pwd_generator

    #Manik: name argument
    #- created a variable password_url which points to the password/ path
    #- The pages which refer this URL can use {% url 'password_url' %}
    #  notation, without having to hard-code the path.
    #- This way, we can easily change the path names without having to 
    #  update the references in the html pages
    path("my_password/", views.password, name='password_url'),
    
    path("styling/", views.styling, name='styling_url'),
    path("portfolio/", portfolio_views.portfolio, name='port_url'),
    path("portfolio_about/", portfolio_views.portfolio_about, name='port_about_url'),

    #Empty string points to the home URL
    path('', views.home, name='home_url'),

    #Forward all requests to blog/... to mysite_blog app
    #Requires a urls.py inside the app
    path('blog/', include('mysite_blog.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
