# Quick Start Guide - Andile's Birthday Website

## 🚀 Getting Started in 2 Minutes

### Step 1: Open Terminal
```powershell
cd "c:\Users\owner\Documents\andile websit"
```

### Step 2: Start Server
```powershell
python manage.py runserver
```

You should see:
```
Starting development server at http://127.0.0.1:8000/
```

### Step 3: Open Browser
Navigate to: **http://127.0.0.1:8000/**

---

## 🌐 Live Features

### On the Home Page
1. **Scroll through sections** using the "Scroll Down" button
2. **Take the Quiz** - answer 5 questions and see reactions
3. **Open Messages** - click the "Open When" buttons to reveal special messages
4. **Play Games** - try the Compliment Machine and Love Meter
5. **Download Letter** - click the 📥 button in the love letter section to download PDF

### In Admin Portal
1. Navigate to: http://127.0.0.1:8000/admin-portal/
2. Password: `andile2025`
3. **Voice Tab**: Record and upload audio messages
4. **Quiz Tab**: See all quiz responses
5. **Open When Tab**: Track which messages were opened/played

### In Django Admin
1. Navigate to: http://127.0.0.1:8000/admin/
2. Username: `admin`
3. Password: `admin123`
4. **Upload Background Images**: Go to Letter Backgrounds
5. **View All Data**: See quiz responses, voice notes, etc.

---

## ⚙️ System Requirements

- Python 3.13+
- Windows 10/11 (or any OS with Python)
- Modern web browser (Chrome, Firefox, Edge, Safari)
- ~500MB disk space

---

## 🔧 Installation (First Time Only)

```powershell
# Navigate to project
cd "c:\Users\owner\Documents\andile websit"

# Install dependencies (if needed)
pip install django==5.2.5 reportlab pillow

# Apply database migrations
python manage.py migrate

# Create superuser (optional, admin already created)
python manage.py createsuperuser
```

---

## 📋 Common Tasks

### How to Upload a Background Image

1. Go to Django Admin: http://127.0.0.1:8000/admin/
2. Login with `admin` / `admin123`
3. Click **Letter Backgrounds**
4. Click **Add Letter Background**
5. Click **Choose File** to select an image
6. Check **Is Active** to make it the current background
7. Click **Save**
8. Refresh the home page to see the new background!

### How to Record a Voice Note

1. Go to Admin Portal: http://127.0.0.1:8000/admin-portal/
2. Password: `andile2025`
3. In the **Voice Notes** tab:
   - Enter a title (e.g., "Love message")
   - Select a category (optional)
   - Click **Start Recording** 🎙️
   - Record your message
   - Click **Stop Recording** ⏹️
   - Click **Upload** to save
4. The voice note will now appear in the list below!

### How to View Quiz Responses

1. Go to Admin Portal: http://127.0.0.1:8000/admin-portal/
2. Password: `andile2025`
3. Click the **Quiz** tab
4. You'll see all quiz questions and answers with timestamps!

### How to Check Open When Interactions

1. Go to Admin Portal: http://127.0.0.1:8000/admin-portal/
2. Password: `andile2025`
3. Click the **Open When** tab
4. See which messages were opened, played, or downloaded!

---

## 🎨 Customization

### Change Admin Portal Password
Edit file: `c:\Users\owner\Documents\andile websit\birthday\views.py`

Find this line (around line 104):
```python
if password == 'andile2025':  # Change this password!
```

Change to your desired password.

### Change Love Letter Text
Edit file: `c:\Users\owner\Documents\andile websit\birthday\pdf_generator.py`

Find the `love_letter_text` variable and update with your message.

### Change Color Scheme
Edit file: `c:\Users\owner\Documents\andile websit\birthday\static\birthday\css\style.css`

Main colors to change:
- `#ff57ab` - Primary pink
- `#ffc1e3` - Light pink
- `#ff8dc7` - Coral

### Add More Quiz Questions
Edit file: `c:\Users\owner\Documents\andile websit\birthday\static\birthday\js\script.js`

Find the `quizQuestions` array and add new questions following the same structure.

---

## 🆘 Troubleshooting

### Server won't start
```powershell
# Make sure Python is installed
python --version

# Make sure you're in the right directory
cd "c:\Users\owner\Documents\andile websit"

# Try again
python manage.py runserver
```

### Port 8000 already in use
```powershell
# Use a different port
python manage.py runserver 8001
# Then visit http://127.0.0.1:8001/
```

### Database errors
```powershell
# Reset database
python manage.py migrate

# If still errors, delete db.sqlite3 and re-migrate
del db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```

### CSS/JS not updating
- Hard refresh browser: `Ctrl+Shift+R` (Windows) or `Cmd+Shift+R` (Mac)
- Clear browser cache
- Server should auto-reload on file changes

### Voice recording not working
- Use Chrome or Edge (best support)
- Check browser console for errors (F12 → Console tab)
- Ensure microphone permissions are granted

---

## 📊 File Locations

| Item | Location |
|------|----------|
| Home Page | `/birthday/templates/birthday/home.html` |
| Admin Portal | `/birthday/templates/birthday/admin_portal.html` |
| CSS Styles | `/birthday/static/birthday/css/style.css` |
| JavaScript | `/birthday/static/birthday/js/script.js` |
| Database | `/db.sqlite3` |
| Voice Notes | `/media/voice_notes/` |
| Background Images | `/media/letter_backgrounds/` |
| Django Models | `/birthday/models.py` |
| View Functions | `/birthday/views.py` |

---

## 🔐 Security Reminders

⚠️ **IMPORTANT**: This setup is for local/development use only!

For production deployment:
1. Change all passwords
2. Set `DEBUG = False` in settings
3. Use proper web server (Gunicorn, uWSGI)
4. Use PostgreSQL instead of SQLite
5. Enable HTTPS
6. Secure secret keys with environment variables
7. Set up proper logging

---

## 💡 Tips & Tricks

### Keyboard Shortcuts
- `Ctrl+F5` - Full page refresh (clears cache)
- `F12` - Open browser developer tools
- `Ctrl+Shift+I` - Inspect element
- `Ctrl+Shift+J` - Open console

### Mobile Testing
1. Open DevTools (F12)
2. Click device icon (top-left of DevTools)
3. Choose device (iPhone, Samsung Galaxy, etc.)
4. Refresh page to test responsive design

### Quick Database View
```powershell
# Open Django shell
python manage.py shell

# View quiz responses
from birthday.models import QuizResponse
for response in QuizResponse.objects.all():
    print(response)

# View voice notes
from birthday.models import VoiceNote
VoiceNote.objects.count()  # Count of voice notes

# Exit shell
exit()
```

---

## 📝 Notes

- Server logs appear in the terminal - useful for debugging
- All data is stored locally in SQLite3
- Files persist between server restarts
- Delete database to start fresh: `del db.sqlite3`

---

## ✅ Verification Checklist

After starting the server, verify everything works:

- [ ] Home page loads (http://127.0.0.1:8000/)
- [ ] All sections visible when scrolling
- [ ] Quiz loads and accepts answers
- [ ] Open When buttons display messages
- [ ] PDF downloads from love letter section
- [ ] Admin portal accessible (http://127.0.0.1:8000/admin-portal/)
- [ ] Can record voice notes
- [ ] Django Admin accessible (http://127.0.0.1:8000/admin/)
- [ ] Can upload background images
- [ ] Mobile layout works (test with F12 device view)

---

## 📞 Quick Reference

```
Home Page:        http://127.0.0.1:8000/
Admin Portal:     http://127.0.0.1:8000/admin-portal/ (password: andile2025)
Django Admin:     http://127.0.0.1:8000/admin/ (user: admin, pass: admin123)
PDF Download:     http://127.0.0.1:8000/download-letter/

Start Server:     python manage.py runserver
Stop Server:      Ctrl+C
Access Port:      http://127.0.0.1:8000/
```

---

**Happy Birthday, Andile!** 🎉💕

This website was created with love and care. Enjoy every feature!

---
