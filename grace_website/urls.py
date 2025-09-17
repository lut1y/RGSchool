"""
URL configuration for grace_website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.http import HttpResponse
from django.views.generic import TemplateView
from main.sitemaps import StaticViewSitemap, ServiceSitemap

# Конфигурация карт сайта
sitemaps = {
    'static': StaticViewSitemap,
    'services': ServiceSitemap,
}

def robots_txt(request):
    content = """User-agent: *
Allow: /

# Sitemap
Sitemap: /sitemap.xml

# Важные файлы для сканирования
Allow: /static/

# Заблокировать административные разделы
Disallow: /admin/

# Заблокировать служебные файлы
Disallow: /*.json$
Disallow: /*.log$"""
    return HttpResponse(content, content_type='text/plain')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', robots_txt, name='robots_txt'),
]

# Для разработки - обслуживание медиа файлов
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
