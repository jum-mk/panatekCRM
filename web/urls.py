"""panatek URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', views.index, name='index'),
                  path('logout/', views.logout_view, name='logout_view'),
                  path('profile/', views.profile, name='profile'),
                  path('clients/', views.clients, name='clients'),
                  path('contact/', views.contact, name='contact'),
                  path('products/<str:id>/', views.single_product, name='single_product'),
                  path('brands/', views.brands, name='brands'),
                  path('single_brand_view/<str:name>/', views.single_brand_view, name='single_brand_view'),
                  path('<str:name>/', views.catalogue, name='catalogue')
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL,
                                                                                           document_root=settings.MEDIA_ROOT)
