"""
URL configuration for djangorecruit project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from  . import views
from django.urls import path
from .views import position, filter_positions
from django.urls import path

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('index/',views.index,name='index'),
    path('custom/',views.custom,name='custom'),
    path('cs/',views.cs,name='cs'),
    path('qa/',views.qa,name='qa'),
    path('models/',views.person_list,name='models'),
    path('position/',views.position,name='position'),
    path('filter-positions/', filter_positions, name='filter_positions'),  # 添加新URL模式
    path('demo/',views.demo,name='demo')

]
