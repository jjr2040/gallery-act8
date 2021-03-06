"""gallery URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from rest_framework.routers import DefaultRouter
from mediagallery.views import *
from mediagallery import views

from django.urls import path, include

router = DefaultRouter()
router.register(r'media', views.MediaViewSet)


urlpatterns = [
	path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('', MediaListView.as_view(), name='media_index'),

    path('details/<int:id>/', views.details, name='details'),

    path('signup/', SignUp.as_view(), name='signup'),
    path('edit-user/<int:pk>', ChangeUserView.as_view(), name='edit_user'),
    path('accounts/', include('django.contrib.auth.urls'))

]
