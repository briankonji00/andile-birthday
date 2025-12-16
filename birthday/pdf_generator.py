from io import BytesIO
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from datetime import datetime

def generate_love_letter_pdf():
    """Generate a PDF of the love letter"""
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4)
    styles = getSampleStyleSheet()
    story = []
    
    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor='#ff57ab',
        spaceAfter=30,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    letter_style = ParagraphStyle(
        'Letter',
        parent=styles['Normal'],
        fontSize=11,
        leading=18,
        spaceAfter=12,
        textColor='#333333'
    )
    
    signature_style = ParagraphStyle(
        'Signature',
        parent=styles['Normal'],
        fontSize=12,
        spaceAfter=6,
        textColor='#ff57ab',
        alignment=TA_LEFT,
        fontName='Helvetica-Oblique'
    )
    
    # Title
    story.append(Paragraph("Happy Birthday Andile 🎂💖", title_style))
    story.append(Spacer(1, 0.3*inch))
    
    # Letter content
    story.append(Paragraph("My Dearest Andile,", letter_style))
    story.append(Spacer(1, 0.1*inch))
    
    paragraphs = [
        "From the moment I started taking you serious, everything changed. The world became brighter, my days became filled with laughter, and my heart found its home. You are the most incredible person I have ever known, and I am so grateful for every moment we share together.",
        
        "Your smile lights up my entire world. Your laugh is my favorite sound. Your kindness, your strength, your beautiful spirit – everything about you makes me fall in love with you all over again, every single day.",
        
        "On this special day, I want you to know that you deserve all the happiness in the world. You deserve to be celebrated not just today, but every day. You are loved, you are cherished, and you are appreciated more than words could ever express.",
        
        "Thank you for being you. Thank you for letting me be part of your life. Thank you for every smile, every laugh, every moment of joy.",
        
        "Happy Birthday, my love. Here's to you, to us, and to all the beautiful moments still to come."
    ]
    
    for para in paragraphs:
        story.append(Paragraph(para, letter_style))
        story.append(Spacer(1, 0.1*inch))
    
    story.append(Spacer(1, 0.2*inch))
    
    # Signature
    story.append(Paragraph("Forever yours,", signature_style))
    story.append(Paragraph("With all my love", signature_style))
    story.append(Paragraph("Brian 💗", signature_style))
    
    story.append(Spacer(1, 0.3*inch))
    
    # Footer
    footer_style = ParagraphStyle(
        'Footer',
        parent=styles['Normal'],
        fontSize=9,
        textColor='#999999',
        alignment=TA_CENTER
    )
    story.append(Paragraph(f"Generated on {datetime.now().strftime('%B %d, %Y')}", footer_style))
    
    # Build PDF
    doc.build(story)
    buffer.seek(0)
    return buffer
