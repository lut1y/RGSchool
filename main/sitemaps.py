from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Service


class StaticViewSitemap(Sitemap):
    """Карта сайта для статических страниц"""
    priority = 0.8
    changefreq = 'weekly'
    
    def items(self):
        return ['home', 'services', 'contact']
    
    def location(self, item):
        return reverse(item)
    
    def lastmod(self, obj):
        return None


class ServiceSitemap(Sitemap):
    """Карта сайта для услуг/направлений"""
    changefreq = 'monthly'
    priority = 0.6
    
    def items(self):
        return Service.objects.filter(is_active=True)
    
    def lastmod(self, obj):
        # Если у модели Service будет поле updated_at, используйте его
        return None
    
    def location(self, item):
        # Пока что ссылаемся на страницу services, 
        # в будущем можно добавить детальные страницы услуг
        return reverse('services')