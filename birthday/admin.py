from django.contrib import admin
from django.utils.html import format_html
from .models import QuizResponse, OpenWhenResponse, VoiceNote, LetterBackground, OpenWhenMessage

@admin.register(QuizResponse)
class QuizResponseAdmin(admin.ModelAdmin):
    list_display = ['question', 'answer', 'created_at']
    list_filter = ['created_at']
    search_fields = ['question', 'answer']
    readonly_fields = ['created_at']

@admin.register(OpenWhenResponse)
class OpenWhenResponseAdmin(admin.ModelAdmin):
    list_display = ['message_type', 'voice_note_played_badge', 'voice_note_downloaded_badge', 'opened_at']
    list_filter = ['message_type', 'opened_at', 'voice_note_played', 'voice_note_downloaded']
    readonly_fields = ['opened_at']
    
    def voice_note_played_badge(self, obj):
        if obj.voice_note_played:
            return format_html('<span style="color: green; font-weight: bold;">✓ Played</span>')
        return format_html('<span style="color: orange;">Not Played</span>')
    voice_note_played_badge.short_description = 'Voice Note Played'
    
    def voice_note_downloaded_badge(self, obj):
        if obj.voice_note_downloaded:
            return format_html('<span style="color: blue; font-weight: bold;">✓ Downloaded</span>')
        return format_html('<span style="color: orange;">Not Downloaded</span>')
    voice_note_downloaded_badge.short_description = 'Voice Note Downloaded'

@admin.register(VoiceNote)
class VoiceNoteAdmin(admin.ModelAdmin):
    list_display = ['title', 'message_type', 'audio_player', 'created_at']
    list_filter = ['message_type', 'created_at']
    search_fields = ['title', 'message_type']
    readonly_fields = ['created_at', 'audio_preview']
    
    fieldsets = (
        ('Voice Note Details', {
            'fields': ('title', 'message_type', 'audio_file', 'audio_preview')
        }),
        ('Metadata', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )
    
    def audio_preview(self, obj):
        if obj.audio_file:
            return format_html(
                '<audio controls style="width: 100%; max-width: 400px;">'
                '<source src="{}" type="audio/mpeg">'
                'Your browser does not support the audio element.'
                '</audio><br><br>'
                '<a href="{}" download class="button" style="background-color: #417690; color: white; padding: 5px 15px; border-radius: 3px; text-decoration: none; display: inline-block; margin-top: 10px;">⬇️ Download Voice Note</a>',
                obj.audio_file.url,
                obj.audio_file.url
            )
        return format_html('<p style="color: red;">No audio file uploaded</p>')
    audio_preview.short_description = 'Audio Preview'
    
    def audio_player(self, obj):
        if obj.audio_file:
            return format_html(
                '<audio controls style="width: 200px;">'
                '<source src="{}" type="audio/mpeg">'
                '</audio>',
                obj.audio_file.url
            )
        return '—'
    audio_player.short_description = 'Player'

@admin.register(LetterBackground)
class LetterBackgroundAdmin(admin.ModelAdmin):
    list_display = ['preview', 'is_active_badge', 'created_at']
    list_filter = ['is_active', 'created_at']
    readonly_fields = ['created_at', 'image_preview']
    
    fieldsets = (
        ('Background Image', {
            'fields': ('image', 'image_preview', 'is_active')
        }),
        ('Metadata', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )
    
    def preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="100" height="100" style="border-radius: 5px; object-fit: cover;" />',
                obj.image.url
            )
        return '—'
    preview.short_description = 'Preview'
    
    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-width: 300px; height: auto; border-radius: 10px;" />',
                obj.image.url
            )
        return format_html('<p style="color: red;">No image uploaded</p>')
    image_preview.short_description = 'Full Preview'
    
    def is_active_badge(self, obj):
        if obj.is_active:
            return format_html('<span style="color: green; font-weight: bold;">✓ Active</span>')
        return format_html('<span style="color: orange;">Inactive</span>')
    is_active_badge.short_description = 'Status'

@admin.register(OpenWhenMessage)
class OpenWhenMessageAdmin(admin.ModelAdmin):
    list_display = ['title', 'emoji', 'order', 'active_badge', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['title', 'message']
    list_editable = ['order']
    readonly_fields = ['created_at']
    
    fieldsets = (
        ('Message Content', {
            'fields': ('title', 'message', 'emoji')
        }),
        ('Display Settings', {
            'fields': ('order', 'is_active')
        }),
        ('Metadata', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )
    
    def active_badge(self, obj):
        if obj.is_active:
            return format_html('<span style="color: green; font-weight: bold;">✓ Active</span>')
        return format_html('<span style="color: red;">✗ Inactive</span>')
    active_badge.short_description = 'Status'
