"""
URL configuration for clothing project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clothee/add/',views.ClothCreateView.as_view(),name="cloth-add"),
    path('clothee/list/',views.ClothListView.as_view(),name="cloth-list"),
    path('clothee/<int:pk>/edit/',views.ClothEditView.as_view(),name="cloth-edit"),
    path('clothee/<int:pk>/',views.ClothDetailView.as_view(),name="cloth-detail"),
    path('clothee/<int:pk>/delete/',views.ClothDeleteView.as_view(),name="cloth-delete")
    # path('clothee/<int:pk>/delete/',views.cloth_delete_view,name="cloth-delete")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
