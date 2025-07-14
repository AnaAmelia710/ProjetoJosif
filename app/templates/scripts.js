document.addEventListener('DOMContentLoaded', function() {
    
    // Elementos do DOM
    const backToTopBtn = document.getElementById('back-to-top');
    const sections = document.querySelectorAll('.section');
    const navLinks = document.querySelectorAll('nav ul li a');
    const heroButton = document.querySelector('.hero-content button');
    
    // Função para mostrar/esconder botão "voltar ao topo"
    function toggleBackToTopButton() {
        if (window.pageYOffset > 300) {
            backToTopBtn.classList.add('visible');
        } else {
            backToTopBtn.classList.remove('visible');
        }
    }
    
    // Função para animar seções quando entram na viewport
    function animateOnScroll() {
        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.clientHeight;
            const windowHeight = window.innerHeight;
            const scrollTop = window.pageYOffset;
            
            // Se a seção está visível na viewport
            if (scrollTop > (sectionTop - windowHeight + 100)) {
                section.classList.add('visible');
            }
        });
    }
    
    // Função para scroll suave para uma seção específica
    function scrollToSection(targetId) {
        const targetSection = document.querySelector(targetId);
        if (targetSection) {
            const headerHeight = document.querySelector('header').offsetHeight;
            const targetPosition = targetSection.offsetTop - headerHeight;
            
            window.scrollTo({
                top: targetPosition,
                behavior: 'smooth'
            });
        }
    }
    
    // Função para destacar link ativo no menu
    function updateActiveNavLink() {
        const scrollPosition = window.pageYOffset + 100;
        
        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.clientHeight;
            const sectionId = section.getAttribute('id');
            
            if (scrollPosition >= sectionTop && scrollPosition < sectionTop + sectionHeight) {
                // Remove classe ativa de todos os links
                navLinks.forEach(link => {
                    link.classList.remove('active');
                });
                
                // Adiciona classe ativa ao link correspondente
                const activeLink = document.querySelector(`nav ul li a[href="#${sectionId}"]`);
                if (activeLink) {
                    activeLink.classList.add('active');
                }
            }
        });
    }
    
    // Event listeners para scroll
    window.addEventListener('scroll', function() {
        toggleBackToTopButton();
        animateOnScroll();
        updateActiveNavLink();
    });
    
    // Event listener para botão "voltar ao topo"
    backToTopBtn.addEventListener('click', function() {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
    
    // Event listeners para links de navegação
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            scrollToSection(targetId);
        });
    });
    
    // Event listener para botão "Saiba mais" na seção hero
    if (heroButton) {
        heroButton.addEventListener('click', function() {
            scrollToSection('#sobre-nos');
        });
    }
    
    // Animação inicial das seções visíveis
    animateOnScroll();
    
    // Efeito de parallax suave no header
    window.addEventListener('scroll', function() {
        const scrolled = window.pageYOffset;
        const header = document.querySelector('header');
        
        if (scrolled > 50) {
            header.style.backgroundColor = 'rgba(46, 125, 50, 0.95)';
            header.style.backdropFilter = 'blur(10px)';
        } else {
            header.style.backgroundColor = '#2e7d32';
            header.style.backdropFilter = 'none';
        }
    });
    
    // Animação de hover para cards de funcionalidades
    const functionalityCards = document.querySelectorAll('#funcionalidades ul li');
    functionalityCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-10px) scale(1.02)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) scale(1)';
        });
    });
    
    // Animação de hover para valores
    const valueItems = document.querySelectorAll('#valores ul li');
    valueItems.forEach(item => {
        item.addEventListener('mouseenter', function() {
            this.style.transform = 'scale(1.1) rotate(2deg)';
        });
        
        item.addEventListener('mouseleave', function() {
            this.style.transform = 'scale(1) rotate(0deg)';
        });
    });
    
    // Efeito de digitação para o título principal
    function typeWriter(element, text, speed = 100) {
        let i = 0;
        element.innerHTML = '';
        
        function type() {
            if (i < text.length) {
                element.innerHTML += text.charAt(i);
                i++;
                setTimeout(type, speed);
            }
        }
        
        type();
    }
    
    // Aplicar efeito de digitação ao título principal após um pequeno delay
    setTimeout(() => {
        const heroTitle = document.querySelector('.hero-content h1');
        if (heroTitle) {
            const originalText = heroTitle.textContent;
            typeWriter(heroTitle, originalText, 50);
        }
    }, 500);
    
    // Contador animado para estatísticas (se houver)
    function animateCounter(element, target, duration = 2000) {
        let start = 0;
        const increment = target / (duration / 16);
        
        function updateCounter() {
            start += increment;
            if (start < target) {
                element.textContent = Math.floor(start);
                requestAnimationFrame(updateCounter);
            } else {
                element.textContent = target;
            }
        }
        
        updateCounter();
    }
    
    // Adicionar classe CSS para link ativo
    const style = document.createElement('style');
    style.textContent = `
        nav ul li a.active {
            color: #e8f5e8 !important;
        }
        nav ul li a.active::after {
            width: 100% !important;
        }
    `;
    document.head.appendChild(style);
    
    // Lazy loading para imagens
    const images = document.querySelectorAll('img');
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.style.opacity = '0';
                img.style.transition = 'opacity 0.5s ease';
                
                img.onload = () => {
                    img.style.opacity = '1';
                };
                
                observer.unobserve(img);
            }
        });
    });
    
    images.forEach(img => {
        imageObserver.observe(img);
    });
    
    // Adicionar efeito de ripple aos botões
    function createRipple(event) {
        const button = event.currentTarget;
        const circle = document.createElement('span');
        const diameter = Math.max(button.clientWidth, button.clientHeight);
        const radius = diameter / 2;
        
        circle.style.width = circle.style.height = `${diameter}px`;
        circle.style.left = `${event.clientX - button.offsetLeft - radius}px`;
        circle.style.top = `${event.clientY - button.offsetTop - radius}px`;
        circle.classList.add('ripple');
        
        const ripple = button.getElementsByClassName('ripple')[0];
        if (ripple) {
            ripple.remove();
        }
        
        button.appendChild(circle);
    }
    
    // Aplicar efeito ripple aos botões
    const buttons = document.querySelectorAll('button');
    buttons.forEach(button => {
        button.addEventListener('click', createRipple);
    });
    
    // CSS para efeito ripple
    const rippleStyle = document.createElement('style');
    rippleStyle.textContent = `
        button {
            position: relative;
            overflow: hidden;
        }
        
        .ripple {
            position: absolute;
            border-radius: 50%;
            background-color: rgba(255, 255, 255, 0.6);
            transform: scale(0);
            animation: ripple-animation 0.6s linear;
            pointer-events: none;
        }
        
        @keyframes ripple-animation {
            to {
                transform: scale(4);
                opacity: 0;
            }
        }
    `;
    document.head.appendChild(rippleStyle);
});

// Função para detectar se o usuário está em um dispositivo móvel
function isMobile() {
    return window.innerWidth <= 768;
}

// Ajustar comportamentos para dispositivos móveis
if (isMobile()) {
    // Reduzir animações em dispositivos móveis para melhor performance
    document.documentElement.style.setProperty('--animation-duration', '0.3s');
} else {
    document.documentElement.style.setProperty('--animation-duration', '0.6s');
}