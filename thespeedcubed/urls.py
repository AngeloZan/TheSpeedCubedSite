"""thespeedcubed URL Configuration

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
from django.urls import path

from website.views import (
    home,
    feedback,
    aprender,
    primeiros_passos,
    primeira_camada,
    segunda_camada,
    terceira_camada,
    sobre_o_cubo_magico,
    avancado,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('feedback/', feedback, name='feedback'),
    path('aprender/', aprender, name='aprender'),
    path('aprender/primeiros-passos', primeiros_passos, name='primeiros_passos'),
    path('aprender/primeira-camada', primeira_camada, name='primeira_camada'),
    path('aprender/segunda-camada', segunda_camada, name='segunda_camada'),
    path('aprender/terceira-camada', terceira_camada, name='terceira_camada'),
    path('sobre-o-cubo-magico', sobre_o_cubo_magico, name='sobre_o_cubo_magico'),
    path('avancado', avancado, name='avancado'),
]
