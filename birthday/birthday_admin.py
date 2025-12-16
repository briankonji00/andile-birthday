from django.contrib import admin as django_admin
from django.urls import path, reverse
from django.utils.html import format_html
from .views import voice_recorder

class BirthdayAdminSite(django_admin.AdminSite):
    site_header = "Andile's Birthday 🎂💖"
    site_title = "Birthday Admin"
    index_title = "Welcome to the Birthday Portal"
    
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('voice-recorder/', voice_recorder, name='voice_recorder'),
        ]
        return custom_urls + urls
    
    def index(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['custom_links'] = [
            {
                'name': '🎙️ Record Voice Notes',
                'url': reverse('admin:voice_recorder'),
                'description': 'Record new voice messages for Andile'
            }
        ]
        return super().index(request, extra_context)

birthday_admin_site = BirthdayAdminSite(name='birthday_admin')
