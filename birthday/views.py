from django.shortcuts import render, redirect
from django.http import JsonResponse, FileResponse
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from .models import QuizResponse, OpenWhenResponse, VoiceNote, LetterBackground, OpenWhenMessage
from .pdf_generator import generate_love_letter_pdf
import json

def home(request):
    """Main birthday landing page"""
    # Get the active background image if any
    try:
        background = LetterBackground.objects.filter(is_active=True).first()
    except:
        background = None
    context = {'background': background}
    return render(request, 'birthday/home.html', context)

@csrf_exempt
def submit_quiz(request):
    """Handle quiz submissions"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            question = data.get('question')
            answer = data.get('answer')
            
            QuizResponse.objects.create(
                question=question,
                answer=answer
            )
            
            return JsonResponse({'status': 'success', 'message': 'Response saved!'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

@csrf_exempt
def open_when(request):
    """Handle Open When interactions"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            message_type = data.get('message_type')
            message_content = data.get('message_content', '')
            action = data.get('action')  # 'opened', 'played', 'downloaded'
            
            response = OpenWhenResponse.objects.create(
                message_type=message_type,
                message_content=message_content
            )
            
            if action == 'played':
                response.voice_note_played = True
                response.save()
            elif action == 'downloaded':
                response.voice_note_downloaded = True
                response.save()
            
            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    
    # GET request - return Open When messages
    # GET request - return Open When messages from database
    messages_list = []
    custom_messages = OpenWhenMessage.objects.filter(is_active=True).all()
    
    for msg in custom_messages:
        messages_list.append({
            'id': msg.id,
            'title': msg.title,
            'message': msg.message,
            'emoji': msg.emoji,
            'voice_note': {
                'url': VoiceNote.objects.filter(message_type=msg.title).first().audio_file.url if VoiceNote.objects.filter(message_type=msg.title).first() else None,
                'exists': VoiceNote.objects.filter(message_type=msg.title).exists()
            }
        })
    
    return JsonResponse(messages_list, safe=False)

def admin_portal(request):
    """Admin portal to view all responses (password protected)"""
    # Simple password check
    if request.method == 'POST':
        password = request.POST.get('password')
        if password == 'andile2025':  # Change this password!
            request.session['admin_authenticated'] = True
            return redirect('admin_portal')
    
    if not request.session.get('admin_authenticated'):
        return render(request, 'birthday/admin_login.html')
    
    quiz_responses = QuizResponse.objects.all()
    open_when_responses = OpenWhenResponse.objects.all()
    
    context = {
        'quiz_responses': quiz_responses,
        'open_when_responses': open_when_responses
    }
    
    return render(request, 'birthday/admin_portal.html', context)

def logout_admin(request):
    """Logout from admin portal"""
    request.session['admin_authenticated'] = False
    return redirect('home')

@staff_member_required
def voice_recorder(request):
    """Voice recorder page for admin"""
    return render(request, 'admin/voice_recorder.html')

@csrf_exempt
def upload_voice_note(request):
    """Handle voice note uploads"""
    if request.method == 'POST':
        try:
            title = request.POST.get('title', 'Voice Message')
            message_type = request.POST.get('message_type', '')
            audio_file = request.FILES.get('audio_file')
            
            if not audio_file:
                return JsonResponse({'status': 'error', 'message': 'No audio file provided'})
            
            # Create voice note
            voice_note = VoiceNote.objects.create(
                title=title,
                message_type=message_type,
                audio_file=audio_file
            )
            
            return JsonResponse({
                'status': 'success',
                'message': 'Voice note saved!',
                'id': voice_note.id
            })
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

@csrf_exempt
def get_voice_notes(request):
    """Get all voice notes"""
    try:
        voice_notes = VoiceNote.objects.all().values('id', 'title', 'message_type', 'audio_file', 'created_at')
        voice_notes_list = []
        for note in voice_notes:
            voice_notes_list.append({
                'id': note['id'],
                'title': note['title'],
                'message_type': note['message_type'],
                'audio_file': f"/media/{note['audio_file']}",
                'created_at': note['created_at'].isoformat()
            })
        return JsonResponse({'voice_notes': voice_notes_list})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)})

@csrf_exempt
def download_letter_pdf(request):
    """Download love letter as PDF"""
    try:
        pdf_buffer = generate_love_letter_pdf()
        response = FileResponse(pdf_buffer, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="Andile_Love_Letter.pdf"'
        return response
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)})

@csrf_exempt
def add_message(request):
    """Add a new Open When message"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            title = data.get('title')
            message = data.get('message')
            emoji = data.get('emoji', '💝')
            
            if not title or not message:
                return JsonResponse({'status': 'error', 'message': 'Title and message are required'})
            
            # Get the highest order and add 1
            last_msg = OpenWhenMessage.objects.all().order_by('-order').first()
            next_order = (last_msg.order if last_msg else 0) + 1
            
            OpenWhenMessage.objects.create(
                title=title,
                message=message,
                emoji=emoji,
                order=next_order,
                is_active=True
            )
            
            return JsonResponse({'status': 'success', 'message': 'Message added successfully!'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
