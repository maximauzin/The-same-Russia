const swup = new Swup({
    containers: ['#header-container', '#content-container'],
    plugins: [new SwupHeadPlugin()],
    rules: [
        {
            from: '/news/',
            to: '/news/',
            containers: ['#content-container']
        }
    ]
});

// --- MENU ACTIONS (called by event listeners) ---
function openMenu() {
    document.getElementById('navMenu')?.classList.add('active');
    document.querySelector('.overlay')?.classList.add('active');
    document.body.classList.add('menu-open');
}

function closeMenu() {
    document.getElementById('navMenu')?.classList.remove('active');
    document.querySelector('.overlay')?.classList.remove('active');
    document.body.classList.remove('menu-open');
}


// --- PAGE-SPECIFIC LOGIC (runs on every page view) ---
function initPage() {
    const stickyHeader = document.getElementById('sticky-header');
    const mainHeader = document.getElementById('header-container');
    const headerElement = document.querySelector('#header-container header');

    // 1. Update Sticky Header Color based on the new page's data attribute
    if (stickyHeader && headerElement) {
        const colorMap = { main: 'grey', news: 'red', team: 'blue' };
        const pageType = headerElement.dataset.pageType || 'main';
        
        Object.values(colorMap).forEach(colorClass => stickyHeader.classList.remove(colorClass));
        if (colorMap[pageType]) {
            stickyHeader.classList.add(colorMap[pageType]);
        }
    }

    // 2. Immediately check scroll position to show/hide sticky header
    if (stickyHeader && mainHeader) {
        if (window.scrollY > mainHeader.offsetHeight) {
            stickyHeader.classList.add('visible');
        } else {
            stickyHeader.classList.remove('visible');
        }
    }
}


// --- PERMANENT SETUP (runs only once) ---
function setupPermanentListeners() {
    // Ensure menu overlay exists
    if (!document.querySelector('.overlay')) {
        const overlay = document.createElement('div');
        overlay.className = 'overlay';
        document.body.appendChild(overlay);
    }
    
    // Permanent click listener for opening/closing the menu
    document.body.addEventListener('click', function(event) {
        if (event.target.closest('#burgerMenu') || event.target.closest('#stickyBurgerMenu')) {
            openMenu();
        } else if (event.target.closest('#menuClose') || event.target.matches('.overlay')) {
            closeMenu();
        }
    });

    // Permanent keydown listener for closing the menu
    document.addEventListener('keydown', (event) => {
        if (event.key === 'Escape' && document.getElementById('navMenu')?.classList.contains('active')) {
            closeMenu();
        }
    });

    // Permanent scroll listener for the sticky header
    const stickyHeader = document.getElementById('sticky-header');
    const mainHeader = document.getElementById('header-container'); // Note: This element persists
    
    if (stickyHeader && mainHeader) {
         window.addEventListener('scroll', () => {
            // We read offsetHeight on every scroll to handle different header sizes
            const currentMainHeader = document.getElementById('header-container');
            if (window.scrollY > currentMainHeader.offsetHeight) {
                stickyHeader.classList.add('visible');
            } else {
                stickyHeader.classList.remove('visible');
            }
        }, { passive: true });
    }
}


// --- SWUP HOOKS ---

// Use 'page:view' - the official hook for running scripts on new pages
swup.hooks.on('page:view', initPage);

// Safety hook to ensure body is scrollable before any transition
swup.hooks.on('visit:start', () => {
    document.body.classList.remove('menu-open');
});

// Hook to close menu before navigating
swup.hooks.on('link:click', (context) => {
    if (document.getElementById('navMenu')?.classList.contains('active')) {
        return new Promise(resolve => {
            closeMenu();
            setTimeout(resolve, 400); // Wait for menu closing animation
        });
    }
});


// --- INITIALIZATION ---
setupPermanentListeners();
initPage();
