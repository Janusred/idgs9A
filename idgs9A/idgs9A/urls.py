"""idgs9A URL Configuration

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
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from core import views
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
<<<<<<< HEAD
    # path('peli/', views.peli, name='peli'),
    path('about/',views.about, name='about')
=======
    path('books/', include('books.urls')),
    path('Musica/', include ('Musica.urls')),
    path('videogames/', include('videogames.urls')),
    path('peliculasSVM/', include('peliculasSVM.urls')),
    path('series/', include('seriesByRVY.urls')),
    path('anime/', include('anime.urls')),
    path('equipoJWN/', include('equipoJWN.urls')),
    path('peli/',include('Directores.urls')),
>>>>>>> bc274ad0421e76b5dad930c34fa54042b272cc97
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
