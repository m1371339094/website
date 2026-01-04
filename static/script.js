// Load services
async function loadServices() {
    try {
        const response = await fetch('/api/services');
        const services = await response.json();
        const container = document.getElementById('servicesContainer');

        if (container) {
            container.innerHTML = services.map(service => `
                <div class="service-card">
                    <div class="service-icon">${service.icon}</div>
                    <h3>${service.title}</h3>
                    <p>${service.description}</p>
                </div>
            `).join('');
        }
    } catch (error) {
        console.error('Error loading services:', error);
        const container = document.getElementById('servicesContainer');
        if (container) {
            container.innerHTML = '<div class="loading">Error loading services. Please refresh the page.</div>';
        }
    }
}

// Load pricing plans
async function loadPricing() {
    try {
        const response = await fetch('/api/pricing');
        const plans = await response.json();
        const container = document.getElementById('pricingContainer');

        if (container) {
            container.innerHTML = plans.map(plan => `
                <div class="pricing-card ${plan.popular ? 'popular' : ''}">
                    <h3>${plan.name}</h3>
                    <div class="pricing-price">${plan.price}</div>
                    <div class="pricing-period">${plan.period}</div>
                    <ul class="pricing-features">
                        ${plan.features.map(feature => `<li>${feature}</li>`).join('')}
                    </ul>
                    <a href="/contact-us" class="cta-button primary">Get Started</a>
                </div>
            `).join('');
        }
    } catch (error) {
        console.error('Error loading pricing:', error);
        const container = document.getElementById('pricingContainer');
        if (container) {
            container.innerHTML = '<div class="loading">Error loading pricing plans. Please refresh the page.</div>';
        }
    }
}

// Handle contact form submission
function initializeContactForm() {
    const form = document.getElementById('contactForm');

    if (form) {
        form.addEventListener('submit', async (e) => {
            e.preventDefault();

            const formData = {
                name: document.getElementById('name').value,
                email: document.getElementById('email').value,
                phone: document.getElementById('phone')?.value || '',
                inquiry: document.getElementById('inquiry')?.value || '',
                message: document.getElementById('message').value,
                newsletter: document.getElementById('newsletter')?.checked || false
            };

            const submitBtn = form.querySelector('.cta-button');
            const originalText = submitBtn.textContent;
            submitBtn.textContent = 'Sending...';
            submitBtn.disabled = true;

            try {
                const response = await fetch('/api/contact', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(formData)
                });

                const result = await response.json();

                if (result.success) {
                    alert(result.message);
                    form.reset();
                } else {
                    alert('Error sending message. Please try again.');
                }
            } catch (error) {
                console.error('Error submitting form:', error);
                alert('Error sending message. Please try again or call us directly.');
            } finally {
                submitBtn.textContent = originalText;
                submitBtn.disabled = false;
            }
        });
    }
}

// Initialize smooth scrolling
function initializeSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));

            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}

// Mobile menu toggle
function initializeMobileMenu() {
    const menuBtn = document.querySelector('.mobile-menu-btn');
    const mobileMenu = document.querySelector('.mobile-menu');

    if (menuBtn && mobileMenu) {
        menuBtn.addEventListener('click', () => {
            mobileMenu.classList.toggle('active');
            // Change icon
            menuBtn.textContent = mobileMenu.classList.contains('active') ? '✕' : '☰';
        });

        // Close menu when clicking a link
        const menuLinks = mobileMenu.querySelectorAll('a');
        menuLinks.forEach(link => {
            link.addEventListener('click', () => {
                mobileMenu.classList.remove('active');
                menuBtn.textContent = '☰';
            });
        });

        // Close menu when clicking outside
        document.addEventListener('click', (e) => {
            if (!menuBtn.contains(e.target) && !mobileMenu.contains(e.target)) {
                mobileMenu.classList.remove('active');
                menuBtn.textContent = '☰';
            }
        });
    }
}

// Header scroll effect
function initializeHeaderScroll() {
    const header = document.querySelector('header');

    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            header.style.boxShadow = '0 4px 20px rgba(0,0,0,0.15)';
        } else {
            header.style.boxShadow = '0 2px 10px rgba(0,0,0,0.1)';
        }
    });
}

// Initialize everything when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    loadServices();
    loadPricing();
    initializeContactForm();
    initializeSmoothScroll();
    initializeMobileMenu();
    initializeHeaderScroll();
});