// Quiz Questions
const quizQuestions = [
    {
        question: "What do I love most about you?",
        options: [
            "Your beautiful smile",
            "Your kind heart",
            "Your amazing personality",
            "All of the above"
        ],
        correctAnswer: "All of the above",
        reaction: "You're absolutely right! I love EVERYTHING about you. Your smile, your heart, your personality - every single thing makes you perfect in my eyes. 💗"
    },
    {
        question: "One small thing you think I could improve?",
        options: [
            "Being more patient",
            "Communicating better",
            "Being more organized",
            "You're perfect as you are"
        ],
        correctAnswer: "You're perfect as you are",
        reaction: "Exactly! You don't need to change anything. You're amazing just the way you are, and I wouldn't want you any other way. 🥰"
    },
    {
        question: "What's your hidden talent?",
        options: [
            "Making me smile",
            "Brightening any room you walk into",
            "Being incredibly thoughtful",
            "All of the above"
        ],
        correctAnswer: "All of the above",
        reaction: "YES! You have so many amazing talents, and the best part is that you don't even realize how incredible you are! 🌟"
    },
    {
        question: "How do I feel when I'm with you?",
        options: [
            "Happy",
            "Complete",
            "At home",
            "All of these"
        ],
        correctAnswer: "All of these",
        reaction: "You got it! Being with you feels like home. You make me happier than I ever thought possible. 💕"
    },
    {
        question: "Birthday special: What are you today?",
        options: [
            "A year older and wiser",
            "More beautiful than ever",
            "The birthday queen",
            "All of the above"
        ],
        correctAnswer: "All of the above",
        reaction: "ABSOLUTELY! Today is YOUR day, and you deserve to be celebrated for the incredible person you are! Happy Birthday, my love! 🎂🎉💖"
    }
];

let currentQuestionIndex = 0;

// Initialize Quiz
function initQuiz() {
    showQuestion(currentQuestionIndex);
}

// Show Question
function showQuestion(index) {
    if (index >= quizQuestions.length) {
        showQuizComplete();
        return;
    }
    
    const question = quizQuestions[index];
    document.getElementById('question-text').textContent = question.question;
    
    const optionsContainer = document.getElementById('options-container');
    optionsContainer.innerHTML = '';
    
    question.options.forEach(option => {
        const button = document.createElement('button');
        button.className = 'option-btn';
        button.textContent = option;
        button.onclick = () => handleAnswer(option, question.reaction);
        optionsContainer.appendChild(button);
    });
    
    document.getElementById('question-container').classList.remove('hidden');
    document.getElementById('reaction-container').classList.add('hidden');
}

// Handle Answer
function handleAnswer(answer, reaction) {
    // Save answer to database
    saveQuizResponse(quizQuestions[currentQuestionIndex].question, answer);
    
    // Show reaction
    document.getElementById('reaction-text').textContent = reaction;
    document.getElementById('question-container').classList.add('hidden');
    document.getElementById('reaction-container').classList.remove('hidden');
}

// Next Question
function nextQuestion() {
    currentQuestionIndex++;
    showQuestion(currentQuestionIndex);
}

// Show Quiz Complete
function showQuizComplete() {
    document.getElementById('question-container').classList.add('hidden');
    document.getElementById('reaction-container').classList.add('hidden');
    document.getElementById('quiz-complete').classList.remove('hidden');
    
    // Trigger confetti
    launchConfetti();
}

// Save Quiz Response
async function saveQuizResponse(question, answer) {
    try {
        await fetch('/submit-quiz/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                question: question,
                answer: answer
            })
        });
    } catch (error) {
        console.error('Error saving response:', error);
    }
}

// Open When Messages
let openWhenMessages = {};

async function loadOpenWhenMessages() {
    try {
        const response = await fetch('/open-when/');
        const messages = await response.json();
        openWhenMessages = {};
        
        // Convert array to object for easier access
        messages.forEach((msg, index) => {
            openWhenMessages[index] = msg;
        });
        
        // Generate buttons dynamically
        const buttonsContainer = document.getElementById('open-when-buttons');
        if (buttonsContainer) {
            buttonsContainer.innerHTML = '';
            messages.forEach((msg, index) => {
                const button = document.createElement('button');
                button.className = 'open-when-btn';
                button.dataset.type = index;
                button.innerHTML = `${msg.emoji} ${msg.title}`;
                button.onclick = () => openMessage(index);
                buttonsContainer.appendChild(button);
            });
        }
    } catch (error) {
        console.error('Error loading messages:', error);
    }
}

function openMessage(type) {
    const message = openWhenMessages[type];
    
    if (!message) return;
    
    document.getElementById('message-title').textContent = message.title;
    document.getElementById('message-text').textContent = message.message;
    
    // Show voice note player if available
    const voiceNotePlayer = document.getElementById('voice-note-player');
    if (message.voice_note && message.voice_note.url) {
        document.getElementById('audio-player').src = message.voice_note.url;
        document.getElementById('download-link').href = message.voice_note.url;
        voiceNotePlayer.classList.remove('hidden');
        
        // Track when audio is played
        document.getElementById('audio-player').addEventListener('play', () => {
            trackOpenWhen(message.title, message.message, 'played');
        });
        
        // Track when audio is downloaded
        document.getElementById('download-link').addEventListener('click', () => {
            trackOpenWhen(message.title, message.message, 'downloaded');
        });
    } else {
        voiceNotePlayer.classList.add('hidden');
    }
    
    // Show modal
    document.getElementById('message-modal').classList.add('active');
    document.getElementById('message-modal').classList.remove('hidden');
    
    // Track that message was opened
    trackOpenWhen(message.title, message.message, 'opened');
}

function closeMessage() {
    document.getElementById('message-modal').classList.remove('active');
    document.getElementById('message-modal').classList.add('hidden');
    
    // Pause audio if playing
    const audioPlayer = document.getElementById('audio-player');
    audioPlayer.pause();
}

async function trackOpenWhen(messageType, messageContent, action) {
    try {
        await fetch('/open-when/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                message_type: messageType,
                message_content: messageContent,
                action: action
            })
        });
    } catch (error) {
        console.error('Error tracking interaction:', error);
    }
}

// Compliment Machine
const compliments = [
    "You are absolutely beautiful, inside and out! 💖",
    "Your smile could light up the darkest room! ✨",
    "You make the world a better place just by being in it! 🌍",
    "You are so incredibly special to me! 💝",
    "Your kindness knows no bounds! 🤗",
    "You inspire me every single day! 🌟",
    "You are stronger than you know! 💪",
    "Your laugh is my favorite sound in the world! 😊",
    "You deserve all the happiness in the universe! 🌈",
    "You are the most amazing person I've ever met! 👑",
    "Your presence makes everything better! ✨",
    "You are loved more than you could ever imagine! 💗",
    "You are brilliant and talented! 🎨",
    "Your heart is pure gold! 💛",
    "You make every day brighter! ☀️"
];

function generateCompliment() {
    const randomCompliment = compliments[Math.floor(Math.random() * compliments.length)];
    document.getElementById('compliment-text').textContent = randomCompliment;
    document.getElementById('compliment-text').style.animation = 'none';
    setTimeout(() => {
        document.getElementById('compliment-text').style.animation = 'fadeIn 0.5s ease-in';
    }, 10);
}

// Heart Meter
function fillHeart() {
    const heartFill = document.getElementById('heart-fill');
    const loveResult = document.getElementById('love-result');
    
    heartFill.style.width = '100%';
    heartFill.innerHTML = '💖💖💖';
    
    setTimeout(() => {
        loveResult.textContent = 'Love Level: INFINITE! ∞ My love for you has no limits! 💗';
    }, 1000);
}

// Smooth Scrolling
function scrollToSection(sectionId) {
    document.getElementById(sectionId).scrollIntoView({
        behavior: 'smooth'
    });
}

// Confetti Animation
function launchConfetti() {
    const canvas = document.getElementById('confetti-canvas');
    const ctx = canvas.getContext('2d');
    
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    
    const particles = [];
    const colors = ['#ff57ab', '#ff8dc7', '#ffc1e3', '#ffa8d5', '#ff72b9'];
    
    class Particle {
        constructor() {
            this.x = Math.random() * canvas.width;
            this.y = -10;
            this.size = Math.random() * 8 + 4;
            this.speedY = Math.random() * 3 + 2;
            this.speedX = Math.random() * 2 - 1;
            this.color = colors[Math.floor(Math.random() * colors.length)];
            this.rotation = Math.random() * 360;
            this.rotationSpeed = Math.random() * 10 - 5;
        }
        
        update() {
            this.y += this.speedY;
            this.x += this.speedX;
            this.rotation += this.rotationSpeed;
            
            if (this.y > canvas.height) {
                return false;
            }
            return true;
        }
        
        draw() {
            ctx.save();
            ctx.translate(this.x, this.y);
            ctx.rotate(this.rotation * Math.PI / 180);
            ctx.fillStyle = this.color;
            ctx.fillRect(-this.size / 2, -this.size / 2, this.size, this.size);
            ctx.restore();
        }
    }
    
    function createParticles() {
        for (let i = 0; i < 10; i++) {
            particles.push(new Particle());
        }
    }
    
    function animate() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        
        for (let i = particles.length - 1; i >= 0; i--) {
            if (particles[i].update()) {
                particles[i].draw();
            } else {
                particles.splice(i, 1);
            }
        }
        
        if (particles.length > 0) {
            requestAnimationFrame(animate);
        } else {
            canvas.width = 0;
            canvas.height = 0;
        }
    }
    
    // Launch confetti
    const interval = setInterval(createParticles, 50);
    setTimeout(() => {
        clearInterval(interval);
    }, 3000);
    
    animate();
}

// Intersection Observer for fade-in animations
const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
        }
    });
}, {
    threshold: 0.1
});

document.addEventListener('DOMContentLoaded', () => {
    // Initialize quiz
    initQuiz();
    
    // Load Open When messages
    loadOpenWhenMessages();
    
    // Observe all sections for animations
    document.querySelectorAll('.fade-in-section').forEach(section => {
        observer.observe(section);
    });
    
    // Close modal when clicking outside
    document.getElementById('message-modal').addEventListener('click', (e) => {
        if (e.target.id === 'message-modal') {
            closeMessage();
        }
    });
    
    // Prevent zoom on double tap for mobile
    document.addEventListener('touchstart', function(event) {
        if (event.touches.length > 1) {
            event.preventDefault();
        }
    }, { passive: false });
    
    // Improve button responsiveness on mobile
    const buttons = document.querySelectorAll('button, .btn-record, .option-btn, .open-when-btn, .game-btn');
    buttons.forEach(btn => {
        btn.addEventListener('touchstart', function() {
            this.style.opacity = '0.8';
        });
        btn.addEventListener('touchend', function() {
            this.style.opacity = '1';
        });
    });
    
    // Prevent accidental scrolls while interacting
    document.addEventListener('touchmove', function(e) {
        if (e.target.closest('audio')) {
            e.preventDefault();
        }
    }, { passive: false });
});
