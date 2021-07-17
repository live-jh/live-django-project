"""config URL Configuration

The `urlpatterns` list routes URLs to presentationals. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function presentationals
    1. Add an import:  from my_app import presentationals
    2. Add a URL to urlpatterns:  path('', presentationals.home, name='home')
Class-based presentationals
    1. Add an import:  from other_app.presentationals import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    # MEDIA_URL 로 시작되는 요청이 올시 MEDIA_ROOT에 찾아서 서빙
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


