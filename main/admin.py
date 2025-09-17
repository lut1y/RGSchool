from django.contrib import admin
from .models import HeroImage, Service, ContactForm


@admin.register(HeroImage)
class HeroImageAdmin(admin.ModelAdmin):
    """Администрирование hero-изображений"""
    list_display = ['title', 'is_active', 'order', 'created_at']
    list_filter = ['is_active', 'created_at']
    list_editable = ['is_active', 'order']
    search_fields = ['title', 'alt_text']
    ordering = ['order', '-created_at']
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('title', 'image', 'alt_text')
        }),
        ('Настройки', {
            'fields': ('is_active', 'order')
        }),
    )
    
    readonly_fields = ['created_at']


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    """Администрирование направлений/услуг"""
    list_display = ['name', 'is_active', 'order']
    list_filter = ['is_active']
    list_editable = ['is_active', 'order']
    search_fields = ['name', 'description']
    ordering = ['order', 'name']
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('name', 'short_description', 'description')
        }),
        ('Оформление', {
            'fields': ('icon_class',)
        }),
        ('Настройки', {
            'fields': ('is_active', 'order')
        }),
    )


@admin.register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
    """Администрирование заявок"""
    list_display = ['name', 'phone', 'service', 'created_at', 'is_processed']
    list_filter = ['is_processed', 'service', 'created_at']
    list_editable = ['is_processed']
    search_fields = ['name', 'phone', 'email']
    ordering = ['-created_at']
    readonly_fields = ['created_at']
    
    fieldsets = (
        ('Контактная информация', {
            'fields': ('name', 'phone', 'email')
        }),
        ('Заявка', {
            'fields': ('service', 'message')
        }),
        ('Обработка', {
            'fields': ('is_processed', 'created_at')
        }),
    )
    
    def has_add_permission(self, request):
        """Запрещаем добавление новых заявок через админку"""
        return False
