"""GameZoneApp URL Configuration

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
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.HomePage,name="index"),
    path('showDetails',views.showDetails, name="showDetails"),
    path('showRunQuery',views.showRunQuery,name = "showRunQuery"),
    path('RunQuery',views.RunQuery,name = "RunQuery"),
    path('insertLaborer',views.insertLaborer,name = "insertLaborer"),
    path('sortLaborer',views.sortLaborer,name="sortLaborer"),
    path('editLaborer/<int:id>',views.editLaborer,name="editLaborer"),
    path('updateLaborer/<int:id>',views.updateLaborer,name="updateLaborer"),
    path('delLaborer/<int:id>',views.delLaborer,name="delLaborer"),
    path('deletedLaborer/<int:id>',views.deletedLaborer,name="deletedLaborer"),

]
