"""musicdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from rest_framework import routers                    # add this
from musicapp import views                             # add this

router = routers.DefaultRouter()                      # add this
"""
router.register(r'users', views.UsersView, 'user')     # add this

"""
router.register(r'artists', views.ArtistsView, 'artist')     # add this
router.register(r'ratings', views.RatingsView, 'rating')     # add this
router.register(r'prices', views.PriceView, 'price')     # add this

urlpatterns = [
    path('musicapp/', include('musicapp.urls')),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
