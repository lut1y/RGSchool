from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_http_methods
from .models import HeroImage, Service, ContactForm
from .forms import ContactFormForm


def home(request):
    """Главная страница сайта"""
    # Получаем активные hero-изображения
    hero_images = HeroImage.objects.filter(is_active=True)
    
    # Получаем активные направления/услуги
    services = Service.objects.filter(is_active=True)
    
    context = {
        'hero_images': hero_images,
        'services': services,
        'page_title': 'Grace School - Спортивная школа развития',
        'meta_description': 'Grace School - современная спортивная школа с бережным подходом к развитию детей. Художественная гимнастика, единоборства, танцы и воздушная гимнастика.',
        'meta_keywords': 'спортивная школа, художественная гимнастика, единоборства, танцы, воздушная гимнастика, развитие детей',
    }
    
    return render(request, 'main/home.html', context)


@csrf_protect
@require_http_methods(["GET", "POST"])
def contact_form_view(request):
    """Обработка контактной формы"""
    if request.method == 'POST':
        form = ContactFormForm(request.POST)
        if form.is_valid():
            # Сохраняем заявку в базу данных
            contact_form = form.save()
            
            # Добавляем сообщение об успешной отправке
            messages.success(request, 'Ваша заявка успешно отправлена! Мы свяжемся с вами в ближайшее время.')
            
            # Если это AJAX запрос, возвращаем JSON
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({
                    'success': True,
                    'message': 'Заявка успешно отправлена!'
                })
            
            return redirect('home')
        else:
            # Если форма невалидна
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({
                    'success': False,
                    'errors': form.errors
                })
    else:
        form = ContactFormForm()
    
    return render(request, 'main/contact_form.html', {'form': form})


def services_view(request):
    """Страница с услугами/направлениями"""
    services = Service.objects.filter(is_active=True)
    
    context = {
        'services': services,
        'page_title': 'Наши направления - Grace School',
        'meta_description': 'Направления Grace School: художественная гимнастика, воздушная гимнастика, танцы и единоборства для детей всех возрастов.',
    }
    
    return render(request, 'main/services.html', context)
