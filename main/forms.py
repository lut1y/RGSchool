from django import forms
from .models import ContactForm, Service


class ContactFormForm(forms.ModelForm):
    """Форма для заявок"""
    
    class Meta:
        model = ContactForm
        fields = ['name', 'phone', 'email', 'message', 'service']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Настройка виджетов и атрибутов полей
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Ваше имя',
            'required': True
        })
        
        self.fields['phone'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': '+7 (999) 999-99-99',
            'required': True
        })
        
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'email@example.com',
            'type': 'email'
        })
        
        self.fields['message'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Ваше сообщение',
            'rows': 4
        })
        
        self.fields['service'].widget.attrs.update({
            'class': 'form-select'
        })
        
        # Делаем поле service необязательным для отображения
        self.fields['service'].empty_label = "Выберите направление (необязательно)"