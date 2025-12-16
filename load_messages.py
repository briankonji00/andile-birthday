#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'andile_birthday.settings')
django.setup()

from birthday.models import OpenWhenMessage

# Create default messages
messages = [
    {
        'title': "Open when you're sad",
        'message': "My love, I know things can be tough sometimes. But remember, you are stronger than you think, braver than you believe, and loved more than you know. I'm always here for you, even when we're apart. Your smile lights up my world, and I can't wait to see it again. 💗",
        'emoji': '😢',
        'order': 0
    },
    {
        'title': "Open when you miss me",
        'message': "I miss you too, more than words can say. Close your eyes and imagine I'm there with you, holding your hand, making you laugh. Distance means nothing when someone means everything. I'm counting down the moments until I can see you again. 💕",
        'emoji': '💭',
        'order': 1
    },
    {
        'title': "Open when you're happy",
        'message': "Your happiness is my happiness! I love seeing you smile and knowing that life is treating you well. Keep shining bright, my beautiful Andile. You deserve all the joy in the world! 🌟💖",
        'emoji': '😊',
        'order': 2
    },
    {
        'title': "Open when you feel overwhelmed",
        'message': "Take a deep breath, my love. You don't have to have everything figured out right now. It's okay to take things one step at a time. I believe in you, and I know you can handle whatever comes your way. You've got this! 💪💗",
        'emoji': '😰',
        'order': 3
    }
]

for msg_data in messages:
    msg, created = OpenWhenMessage.objects.get_or_create(
        title=msg_data['title'],
        defaults={
            'message': msg_data['message'],
            'emoji': msg_data['emoji'],
            'order': msg_data['order'],
            'is_active': True
        }
    )
    if created:
        print(f"✓ Created: {msg.title}")
    else:
        print(f"→ Already exists: {msg.title}")

print("\n✓ All Open When messages loaded!")
