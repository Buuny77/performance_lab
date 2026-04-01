/*
 * Main JavaScript
 * Performance Lab - الوظائف الرئيسية
 */

// ==================== انتظار تحميل الصفحة ====================
document.addEventListener('DOMContentLoaded', function() {
    initNavbar();
    initMobileMenu();
    initScrollAnimations();
    initCounterAnimations();
    initTooltips();
});

// ==================== شريط التنقل ====================
function initNavbar() {
    const navbar = document.getElementById('navbar');
    if (!navbar) return;
    
    let lastScroll = 0;
    
    window.addEventListener('scroll', function() {
        const currentScroll = window.pageYOffset;
        
        // تغيير خلفية الـ Navbar عند التمرير
        if (currentScroll > 50) {
            navbar.classList.add('bg-dark-bg/95', 'backdrop-blur-xl', 'shadow-lg');
        } else {
            navbar.classList.remove('bg-dark-bg/95', 'backdrop-blur-xl', 'shadow-lg');
        }
        
        lastScroll = currentScroll;
    });
}

// ==================== قائمة الجوال ====================
function initMobileMenu() {
    const menuBtn = document.getElementById('mobile-menu-btn');
    const mobileMenu = document.getElementById('mobile-menu');
    
    if (!menuBtn || !mobileMenu) return;
    
    menuBtn.addEventListener('click', function() {
        mobileMenu.classList.toggle('hidden');
        
        // تغيير الأيقونة
        const icon = menuBtn.querySelector('i');
        if (mobileMenu.classList.contains('hidden')) {
            icon.classList.remove('fa-times');
            icon.classList.add('fa-bars');
        } else {
            icon.classList.remove('fa-bars');
            icon.classList.add('fa-times');
        }
    });
    
    // إغلاق القائمة عند النقر على رابط
    const links = mobileMenu.querySelectorAll('a');
    links.forEach(link => {
        link.addEventListener('click', () => {
            mobileMenu.classList.add('hidden');
            menuBtn.querySelector('i').classList.remove('fa-times');
            menuBtn.querySelector('i').classList.add('fa-bars');
        });
    });
}

// ==================== تأثيرات التمرير ====================
function initScrollAnimations() {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('revealed');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);
    
    const elements = document.querySelectorAll('.scroll-reveal');
    elements.forEach(el => observer.observe(el));
}

// ==================== عداد الأرقام ====================
function initCounterAnimations() {
    const counters = document.querySelectorAll('.counter');
    
    const observerOptions = {
        threshold: 0.5
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                animateCounter(entry.target);
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);
    
    counters.forEach(counter => observer.observe(counter));
}

function animateCounter(element) {
    const target = parseInt(element.getAttribute('data-target'));
    const duration = 2000;
    const step = target / (duration / 16);
    let current = 0;
    
    const timer = setInterval(() => {
        current += step;
        if (current >= target) {
            element.textContent = target.toLocaleString();
            clearInterval(timer);
        } else {
            element.textContent = Math.floor(current).toLocaleString();
        }
    }, 16);
}

// ==================== تلميحات ====================
function initTooltips() {
    const tooltips = document.querySelectorAll('[data-tooltip]');
    
    tooltips.forEach(tooltip => {
        tooltip.addEventListener('mouseenter', showTooltip);
        tooltip.addEventListener('mouseleave', hideTooltip);
    });
}

function showTooltip(e) {
    const text = e.target.getAttribute('data-tooltip');
    const tooltip = document.createElement('div');
    tooltip.className = 'tooltip';
    tooltip.textContent = text;
    
    document.body.appendChild(tooltip);
    
    const rect = e.target.getBoundingClientRect();
    tooltip.style.left = rect.left + (rect.width / 2) - (tooltip.offsetWidth / 2) + 'px';
    tooltip.style.top = rect.top - tooltip.offsetHeight - 10 + 'px';
    
    setTimeout(() => tooltip.classList.add('show'), 10);
}

function hideTooltip() {
    const tooltip = document.querySelector('.tooltip');
    if (tooltip) {
        tooltip.classList.remove('show');
        setTimeout(() => tooltip.remove(), 300);
    }
}

// ==================== إشعار ====================
function showNotification(message, type = 'success') {
    const toast = document.getElementById('toast');
    const toastMessage = document.getElementById('toast-message');
    
    if (!toast || !toastMessage) return;
    
    toastMessage.textContent = message;
    
    // تغيير اللون حسب النوع
    toast.className = 'fixed bottom-4 left-1/2 -translate-x-1/2 px-6 py-3 rounded-xl text-white transform transition-all duration-300 z-50';
    
    if (type === 'success') {
        toast.classList.add('bg-card-bg', 'border', 'border-neon-green/50', 'shadow-[0_0_30px_rgba(57,255,20,0.2)]');
    } else if (type === 'error') {
        toast.classList.add('bg-card-bg', 'border', 'border-neon-pink/50', 'shadow-[0_0_30px_rgba(255,0,110,0.2)]');
    }
    
    // إظهار الإشعار
    toast.classList.remove('translate-y-20', 'opacity-0');
    
    // إخفاء الإشعار بعد 3 ثواني
    setTimeout(() => {
        toast.classList.add('translate-y-20', 'opacity-0');
    }, 3000);
}

// ==================== تأثير الكتابة ====================
function typeWriter(element, text, speed = 100) {
    let i = 0;
    element.textContent = '';
    
    function type() {
        if (i < text.length) {
            element.textContent += text.charAt(i);
            i++;
            setTimeout(type, speed);
        }
    }
    
    type();
}

// ==================== تأثير الموجة ====================
function createWaveEffect(element) {
    const chars = element.textContent.split('');
    element.innerHTML = chars.map((char, i) => 
        `<span style="animation-delay: ${i * 0.05}s">${char}</span>`
    ).join('');
    element.classList.add('wave-text');
}

// ==================== تأثير الانفجار ====================
function explodeEffect(element) {
    element.style.transform = 'scale(1.5)';
    element.style.opacity = '0';
    
    setTimeout(() => {
        element.style.transform = 'scale(1)';
        element.style.opacity = '1';
    }, 300);
}

// ==================== تأثير الوميض ====================
function flashEffect(element, duration = 500) {
    element.classList.add('flash');
    setTimeout(() => {
        element.classList.remove('flash');
    }, duration);
}

// ==================== تأثير الاهتزاز ====================
function shakeEffect(element) {
    element.classList.add('shake');
    setTimeout(() => {
        element.classList.remove('shake');
    }, 500);
}

// ==================== تأثير التكبير ====================
function zoomEffect(element) {
    element.classList.add('zoom-in');
    setTimeout(() => {
        element.classList.remove('zoom-in');
    }, 500);
}

// ==================== تأثير الانزلاق ====================
function slideEffect(element, direction = 'up') {
    element.classList.add(`slide-${direction}`);
    setTimeout(() => {
        element.classList.remove(`slide-${direction}`);
    }, 600);
}

// ==================== تأثير الدوران ====================
function spinEffect(element, duration = 1000) {
    element.classList.add('spin');
    setTimeout(() => {
        element.classList.remove('spin');
    }, duration);
}

// ==================== تأثير النبض ====================
function pulseEffect(element) {
    element.classList.add('pulse');
    setTimeout(() => {
        element.classList.remove('pulse');
    }, 2000);
}

// ==================== تأثير الارتداد ====================
function bounceEffect(element) {
    element.classList.add('bounce');
    setTimeout(() => {
        element.classList.remove('bounce');
    }, 1000);
}

// ==================== تأثير الوجه ====================
function flipEffect(element) {
    element.classList.add('flip');
    setTimeout(() => {
        element.classList.remove('flip');
    }, 600);
}

// ==================== تأثير التحول المطاطي ====================
function rubberBandEffect(element) {
    element.classList.add('rubber-band');
    setTimeout(() => {
        element.classList.remove('rubber-band');
    }, 1000);
}

// ==================== تأثير الاهتزاز الدائري ====================
function tadaEffect(element) {
    element.classList.add('tada');
    setTimeout(() => {
        element.classList.remove('tada');
    }, 1000);
}

// ==================== تأثير الاهتزاز العمودي ====================
function jellyEffect(element) {
    element.classList.add('jelly');
    setTimeout(() => {
        element.classList.remove('jelly');
    }, 500);
}

// ==================== تأثير التحول الدائري ====================
function swingEffect(element) {
    element.classList.add('swing');
    setTimeout(() => {
        element.classList.remove('swing');
    }, 1000);
}

// ==================== تأثير التلاشي المتكرر ====================
function fadePulseEffect(element) {
    element.classList.add('fade-pulse');
    setTimeout(() => {
        element.classList.remove('fade-pulse');
    }, 2000);
}

// ==================== تأثير العائم ====================
function floatEffect(element) {
    element.classList.add('float');
}

// ==================== تأثير المورف ====================
function morphEffect(element) {
    element.classList.add('morph');
}

// ==================== تأثير الرادار ====================
function radarEffect(element) {
    element.classList.add('radar');
}

// ==================== تأثير الضباب ====================
function mistEffect(element) {
    element.classList.add('mist');
}

// ==================== تأثير التدرج المتحرك ====================
function gradientTextEffect(element) {
    element.classList.add('gradient-text-animated');
}

// ==================== تأثير الظل المتحرك ====================
function shadowAnimatedEffect(element) {
    element.classList.add('shadow-animated');
}

// ==================== تأثير الاهتزاز السريع ====================
function vibrateEffect(element) {
    element.classList.add('vibrate');
    setTimeout(() => {
        element.classList.remove('vibrate');
    }, 300);
}

// ==================== تأثير التحول ثلاثي الأبعاد ====================
function flip3DEffect(element) {
    element.classList.add('flip-3d');
}

// ==================== تأثير التكبير التدريجي ====================
function growEffect(element) {
    element.classList.add('grow');
    setTimeout(() => {
        element.classList.remove('grow');
    }, 500);
}

// ==================== تأثير الاهتزاز الأفقي ====================
function wobbleEffect(element) {
    element.classList.add('wobble');
    setTimeout(() => {
        element.classList.remove('wobble');
    }, 1000);
}

// ==================== تأثير العد ====================
function countUpEffect(element) {
    element.classList.add('count-up');
}

// ==================== تأثير التموج ====================
function rippleEffect(element) {
    element.classList.add('ripple');
}

// ==================== تأثير الخط المرسوم ====================
function drawLineEffect(element) {
    element.classList.add('draw-line');
}

// ==================== تأثير التحويل ====================
function transformEffect(element) {
    element.classList.add('transform');
}

// ==================== تأثير التحول ====================
function transitionEffect(element) {
    element.classList.add('transition');
}

// ==================== تأثير التحول السريع ====================
function transitionFastEffect(element) {
    element.classList.add('transition-fast');
}

// ==================== تأثير التحول البطيء ====================
function transitionSlowEffect(element) {
    element.classList.add('transition-slow');
}

// ==================== تأثير التحول المتوسط ====================
function transitionMediumEffect(element) {
    element.classList.add('transition-medium');
}

// ==================== تأثير التحول اللانهائي ====================
function transitionInfiniteEffect(element) {
    element.classList.add('transition-infinite');
}

// ==================== تأثير التحول المتكرر ====================
function transitionRepeatEffect(element) {
    element.classList.add('transition-repeat');
}

// ==================== تأثير التحول المتناوب ====================
function transitionAlternateEffect(element) {
    element.classList.add('transition-alternate');
}

// ==================== تأثير التحول العكسي ====================
function transitionReverseEffect(element) {
    element.classList.add('transition-reverse');
}

// ==================== تأثير التحول العكسي المتناوب ====================
function transitionReverseAlternateEffect(element) {
    element.classList.add('transition-reverse-alternate');
}

// ==================== تأثير التحول العكسي المتكرر ====================
function transitionReverseRepeatEffect(element) {
    element.classList.add('transition-reverse-repeat');
}

// ==================== تأثير التحول اللانهائي العكسي ====================
function transitionInfiniteReverseEffect(element) {
    element.classList.add('transition-infinite-reverse');
}

// ==================== تأثير التحول اللانهائي المتناوب ====================
function transitionInfiniteAlternateEffect(element) {
    element.classList.add('transition-infinite-alternate');
}

// ==================== تأثير التحول اللانهائي المتكرر ====================
function transitionInfiniteRepeatEffect(element) {
    element.classList.add('transition-infinite-repeat');
}

// ==================== تأثير التحول اللانهائي العكسي المتناوب ====================
function transitionInfiniteReverseAlternateEffect(element) {
    element.classList.add('transition-infinite-reverse-alternate');
}

// ==================== تأثير التحول اللانهائي العكسي المتكرر ====================
function transitionInfiniteReverseRepeatEffect(element) {
    element.classList.add('transition-infinite-reverse-repeat');
}
