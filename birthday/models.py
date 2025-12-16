from django.db import models
from django.utils import timezone

class QuizResponse(models.Model):
    """Store responses from the birthday quiz"""
    question = models.CharField(max_length=500)
    answer = models.CharField(max_length=500)
    created_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.question[:50]} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"


class OpenWhenResponse(models.Model):
    """Store which 'Open When' messages she has opened"""
    message_type = models.CharField(max_length=200)  # e.g., "Open when you're sad"
    message_content = models.TextField()
    voice_note_played = models.BooleanField(default=False)
    voice_note_downloaded = models.BooleanField(default=False)
    opened_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ['-opened_at']
    
    def __str__(self):
        return f"{self.message_type} - {self.opened_at.strftime('%Y-%m-%d %H:%M')}"


class VoiceNote(models.Model):
    """Store voice notes for the website"""
    title = models.CharField(max_length=200)
    audio_file = models.FileField(upload_to='voice_notes/')
    message_type = models.CharField(max_length=200, blank=True)  # Link to Open When category
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title


class OpenWhenMessage(models.Model):
    """Store customizable Open When messages"""
    title = models.CharField(max_length=200)  # e.g., "Open when you're sad"
    message = models.TextField()  # The actual message content
    emoji = models.CharField(max_length=10, default='💝')  # Emoji for button
    order = models.PositiveIntegerField(default=0)  # Display order
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.title


class LetterBackground(models.Model):
    """Store background image for the love letter"""
    image = models.ImageField(upload_to='letter_backgrounds/')
    created_at = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Background - {self.created_at.strftime('%Y-%m-%d')}"
    
    def save(self, *args, **kwargs):
        # Only allow one active background at a time
        if self.is_active:
            LetterBackground.objects.filter(is_active=True).exclude(id=self.id).update(is_active=False)
        super().save(*args, **kwargs)
