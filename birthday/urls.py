from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('submit-quiz/', views.submit_quiz, name='submit_quiz'),
    path('open-when/', views.open_when, name='open_when'),
    path('admin-portal/', views.admin_portal, name='admin_portal'),
    path('logout/', views.logout_admin, name='logout_admin'),
    path('voice-recorder/', views.voice_recorder, name='voice_recorder'),
    path('api/upload-voice-note/', views.upload_voice_note, name='upload_voice_note'),
    path('api/get-voice-notes/', views.get_voice_notes, name='get_voice_notes'),
    path('download-letter/', views.download_letter_pdf, name='download_letter_pdf'),
    path('add-message/', views.add_message, name='add_message'),
]
