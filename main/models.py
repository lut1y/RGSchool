from django.db import models
from django.core.validators import FileExtensionValidator
from PIL import Image
import os


class HeroImage(models.Model):
    """Модель для hero-изображений, которые можно загружать через админку"""
    title = models.CharField(max_length=200, verbose_name="Название изображения")
    image = models.ImageField(
        upload_to='hero_images/',
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'webp'])],
        verbose_name="Изображение"
    )
    alt_text = models.CharField(max_length=255, verbose_name="Alt-текст для SEO")
    is_active = models.BooleanField(default=True, verbose_name="Активно")
    order = models.PositiveIntegerField(default=0, verbose_name="Порядок отображения")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    
    class Meta:
        verbose_name = "Hero-изображение"
        verbose_name_plural = "Hero-изображения"
        ordering = ['order', '-created_at']
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        # Оптимизация изображения для быстрой загрузки
        if self.image and hasattr(self.image, 'path') and os.path.exists(self.image.path):
            try:
                img = Image.open(self.image.path)
                
                # Максимальный размер для hero-изображений
                max_size = (1920, 1080)
                if img.height > max_size[1] or img.width > max_size[0]:
                    img.thumbnail(max_size, Image.Resampling.LANCZOS)
                    img.save(self.image.path, optimize=True, quality=85)
            except Exception:
                pass  # Если не удалось оптимизировать изображение, продолжаем без ошибки


class Service(models.Model):
    """Модель для услуг/направлений школы"""
    name = models.CharField(max_length=200, verbose_name="Название направления")
    description = models.TextField(verbose_name="Описание")
    short_description = models.CharField(max_length=300, verbose_name="Краткое описание")
    icon_class = models.CharField(max_length=100, blank=True, verbose_name="CSS класс иконки")
    is_active = models.BooleanField(default=True, verbose_name="Активно")
    order = models.PositiveIntegerField(default=0, verbose_name="Порядок отображения")
    
    class Meta:
        verbose_name = "Направление"
        verbose_name_plural = "Направления"
        ordering = ['order', 'name']
    
    def __str__(self):
        return self.name


class ContactForm(models.Model):
    """Модель для сохранения заявок с контактной формы"""
    name = models.CharField(max_length=100, verbose_name="Имя")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    email = models.EmailField(blank=True, verbose_name="Email")
    message = models.TextField(blank=True, verbose_name="Сообщение")
    service = models.ForeignKey(Service, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="Интересующее направление")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    is_processed = models.BooleanField(default=False, verbose_name="Обработано")
    
    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} - {self.phone}"
