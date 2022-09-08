"""config URL Configuration

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
# from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import include, path

# Подключаем редирект, что бы при обращении к основному адресу,
# перенаправляло на нужный адрес
from django.views.generic import RedirectView

#   Список путей, которые будут доступны в проекте.
#   При их идентичности, используется первый.
#       (Адрес, Контроллер)
#   Контроллер содержится в модуле views.py

urlpatterns = [
    path("admin/", admin.site.urls),
    # Подключаем редирект
    path("", RedirectView.as_view(url="mainapp/")),
    # импортируем include
    # С помощью include, по пути mainapp мы указываем какие адреса
    # из какого приложения мы включаем в рамках нашего модуля
    # "Папка.Файл" - не указание пути а обращение к внутреннему пакету
    path("mainapp/", include("mainapp.urls")),
]
