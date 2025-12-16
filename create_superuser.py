import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'andile_birthday.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# Create superuser if it doesn't exist
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser(
        username='admin',
        email='admin@andile.com',
        password='admin123'
    )
    print("✅ Superuser created!")
    print("Username: admin")
    print("Password: admin123")
    print("Email: admin@andile.com")
else:
    print("Superuser already exists")
