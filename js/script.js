// Glavna JavaScript funkcionalnost

// Smooth scroll za navigacione linkove
function scrollToSection(sectionId) {
    document.getElementById(sectionId).scrollIntoView({
        behavior: 'smooth'
    });
}

// Otvaranje modala za kontakt
function openContact(packageName) {
    document.getElementById('selectedPackage').textContent = packageName;
    document.getElementById('contactModal').style.display = 'block';
}

// Zatvaranje modala
function closeModal() {
    document.getElementById('contactModal').style.display = 'none';
}

// Kontakt forma submit
document.getElementById('contactForm').addEventListener('submit', function(e) {
    e.preventDefault();
    
    const formData = {
        name: document.getElementById('name').value,
        phone: document.getElementById('phone').value,
        package: document.getElementById('package').value,
        message: document.getElementById('message').value
    };
    
    // Simulacija slanja podataka
    console.log('Form data:', formData);
    alert('Hvala na upitu! Kontaktiraćemo vas uskoro.');
    this.reset();
});

// Zatvaranje modala klikom van njega
window.addEventListener('click', function(e) {
    const modal = document.getElementById('contactModal');
    if (e.target === modal) {
        closeModal();
    }
});

// Dodavanje active klase na navigacione linkove
window.addEventListener('scroll', function() {
    const sections = document.querySelectorAll('section');
    const navLinks = document.querySelectorAll('.nav-link');
    
    let current = '';
    
    sections.forEach(section => {
        const sectionTop = section.offsetTop;
        const sectionHeight = section.clientHeight;
        if (scrollY >= (sectionTop - 100)) {
            current = section.getAttribute('id');
        }
    });
    
    navLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href').substring(1) === current) {
            link.classList.add('active');
        }
    });
});

// Animacija za package kartice
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver(function(entries) {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, observerOptions);

// Primena animacije na package kartice
document.addEventListener('DOMContentLoaded', function() {
    const packages = document.querySelectorAll('.package-card');
    packages.forEach(package => {
        package.style.opacity = '0';
        package.style.transform = 'translateY(20px)';
        package.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(package);
    });
});

console.log('TVInternetSBB website loaded successfully!');
