document.addEventListener('DOMContentLoaded', function() {
    const burgerMenu = document.getElementById('burgerMenu');
    const navMenu = document.getElementById('navMenu');
    const menuClose = document.getElementById('menuClose');
    
    // Создаем overlay для затемнения фона
    const overlay = document.createElement('div');
    overlay.className = 'overlay';
    document.body.appendChild(overlay);
    
    function openMenu() {
        burgerMenu.classList.add('hidden');
        navMenu.classList.add('active');
        overlay.classList.add('active');
        document.body.style.overflow = 'hidden';
    }
    
    function closeMenu() {
        burgerMenu.classList.remove('hidden');
        navMenu.classList.remove('active');
        overlay.classList.remove('active');
        document.body.style.overflow = '';
    }
    
    // Открытие по клику на бургер
    burgerMenu.addEventListener('click', function(event) {
        event.stopPropagation();
        openMenu();
    });
    
    // Закрытие по клику на крестик
    menuClose.addEventListener('click', function(event) {
        event.stopPropagation();
        closeMenu();
    });
    
    // Закрытие по клику на overlay
    overlay.addEventListener('click', function() {
        closeMenu();
    });
    
    // Закрытие по клику на ссылку
    const navLinks = document.querySelectorAll('.site-navigation-item a');
    navLinks.forEach(link => {
        link.addEventListener('click', function() {
            closeMenu();
        });
    });
    
    // Закрытие по клавише Escape
    document.addEventListener('keydown', function(event) {
        if (event.key === 'Escape' && navMenu.classList.contains('active')) {
            closeMenu();
        }
    });
});
