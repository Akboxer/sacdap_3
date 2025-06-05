// SACDAP Website JavaScript Functions

document.addEventListener('DOMContentLoaded', function() {
    // Initialize all JavaScript functionality
    initializeFormValidation();
    initializeAnimations();
    initializeNavigation();
    initializeSearchDropdown();
    initializeTooltips();
    initializeScrollEffects();
});

// Form Validation Enhancement
function initializeFormValidation() {
    const forms = document.querySelectorAll('form');
    
    forms.forEach(form => {
        // Real-time validation
        const inputs = form.querySelectorAll('input, select, textarea');
        inputs.forEach(input => {
            input.addEventListener('blur', function() {
                validateField(this);
            });
            
            input.addEventListener('input', function() {
                if (this.classList.contains('is-invalid')) {
                    validateField(this);
                }
            });
        });
        
        // Form submission handling
        form.addEventListener('submit', function(e) {
            let isValid = true;
            
            inputs.forEach(input => {
                if (!validateField(input)) {
                    isValid = false;
                }
            });
            
            if (!isValid) {
                e.preventDefault();
                showAlert('Please correct the errors in the form before submitting.', 'danger');
                // Scroll to first invalid field
                const firstInvalid = form.querySelector('.is-invalid');
                if (firstInvalid) {
                    firstInvalid.scrollIntoView({ behavior: 'smooth', block: 'center' });
                    firstInvalid.focus();
                }
            } else {
                // Show loading state
                const submitBtn = form.querySelector('button[type="submit"]');
                if (submitBtn) {
                    showLoadingState(submitBtn);
                }
            }
        });
    });
}

// Field validation function
function validateField(field) {
    const value = field.value.trim();
    let isValid = true;
    let message = '';
    
    // Remove existing validation classes
    field.classList.remove('is-valid', 'is-invalid');
    
    // Check if field is required
    if (field.hasAttribute('required') && !value) {
        isValid = false;
        message = 'This field is required.';
    }
    
    // Specific validation rules
    if (value && field.type === 'email') {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(value)) {
            isValid = false;
            message = 'Please enter a valid email address.';
        }
    }
    
    if (value && field.type === 'tel') {
        const phoneRegex = /^[\+]?[1-9][\d]{0,15}$/;
        if (!phoneRegex.test(value.replace(/[\s\-\(\)]/g, ''))) {
            isValid = false;
            message = 'Please enter a valid phone number.';
        }
    }
    
    if (value && field.name === 'name') {
        if (value.length < 2) {
            isValid = false;
            message = 'Name must be at least 2 characters long.';
        }
    }
    
    // Apply validation result
    if (isValid) {
        field.classList.add('is-valid');
    } else {
        field.classList.add('is-invalid');
        
        // Update or create error message
        let feedback = field.parentNode.querySelector('.invalid-feedback');
        if (!feedback) {
            feedback = document.createElement('div');
            feedback.className = 'invalid-feedback';
            field.parentNode.appendChild(feedback);
        }
        feedback.textContent = message;
    }
    
    return isValid;
}

// Animation initialization
function initializeAnimations() {
    // Fade in animations for cards
    const cards = document.querySelectorAll('.card');
    cards.forEach((card, index) => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        
        setTimeout(() => {
            card.style.transition = 'all 0.6s ease';
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
        }, index * 100);
    });
    
    // Hover effects for course cards
    const courseCards = document.querySelectorAll('.course-card, .course-detail-card');
    courseCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-5px)';
            this.style.boxShadow = '0 1rem 3rem rgba(0, 0, 0, 0.175)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
            this.style.boxShadow = '';
        });
    });
}

// Navigation enhancements
function initializeNavigation() {
    // Smooth scrolling for anchor links
    const anchors = document.querySelectorAll('a[href^="#"]');
    anchors.forEach(anchor => {
        anchor.addEventListener('click', function(e) {
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
    
    // Navbar scroll effect
    const navbar = document.querySelector('.navbar');
    if (navbar) {
        window.addEventListener('scroll', function() {
            if (window.scrollY > 50) {
                navbar.classList.add('shadow');
            } else {
                navbar.classList.remove('shadow');
            }
        });
    }
    
    // Mobile menu auto-close
    const navbarToggler = document.querySelector('.navbar-toggler');
    const navbarCollapse = document.querySelector('.navbar-collapse');
    const navLinks = document.querySelectorAll('.nav-link');
    
    navLinks.forEach(link => {
        link.addEventListener('click', () => {
            if (window.innerWidth < 992) {
                const bsCollapse = new bootstrap.Collapse(navbarCollapse, {
                    toggle: false
                });
                bsCollapse.hide();
            }
        });
    });
}

// Search dropdown enhancement
function initializeSearchDropdown() {
    const searchSelect = document.querySelector('select[name="course"]');
    if (searchSelect) {
        // Add search functionality
        const courses = Array.from(searchSelect.options).slice(1); // Skip first option
        
        searchSelect.addEventListener('change', function() {
            if (this.value) {
                // Add visual feedback
                this.style.borderColor = '#dc3545';
                this.style.backgroundColor = '#fff5f5';
                
                // Auto-submit after a short delay
                setTimeout(() => {
                    this.form.submit();
                }, 300);
            }
        });
        
        // Enhanced keyboard navigation
        searchSelect.addEventListener('keydown', function(e) {
            if (e.key === 'Enter' && this.value) {
                this.form.submit();
            }
        });
    }
}

// Initialize tooltips and popovers
function initializeTooltips() {
    // Initialize Bootstrap tooltips
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
    
    // Add custom tooltips for course cards
    const courseCards = document.querySelectorAll('.course-card');
    courseCards.forEach(card => {
        const enrollBtn = card.querySelector('.btn');
        if (enrollBtn) {
            enrollBtn.setAttribute('title', 'Click to enroll in this course');
            new bootstrap.Tooltip(enrollBtn);
        }
    });
}

// Scroll effects and lazy loading
function initializeScrollEffects() {
    // Intersection Observer for scroll animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);
    
    // Observe elements for scroll animations
    const animateElements = document.querySelectorAll('.card, .btn, .alert');
    animateElements.forEach(el => {
        observer.observe(el);
    });
    
    // Scroll to top button
    createScrollToTopButton();
}

// Create scroll to top button
function createScrollToTopButton() {
    const scrollBtn = document.createElement('button');
    scrollBtn.innerHTML = '<i class="fas fa-arrow-up"></i>';
    scrollBtn.className = 'btn btn-danger position-fixed';
    scrollBtn.style.cssText = `
        bottom: 20px;
        right: 20px;
        z-index: 1050;
        width: 50px;
        height: 50px;
        border-radius: 50%;
        display: none;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        transition: all 0.3s ease;
    `;
    
    scrollBtn.addEventListener('click', () => {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });
    
    window.addEventListener('scroll', () => {
        if (window.scrollY > 300) {
            scrollBtn.style.display = 'block';
        } else {
            scrollBtn.style.display = 'none';
        }
    });
    
    document.body.appendChild(scrollBtn);
}

// Utility functions
function showAlert(message, type = 'info') {
    const alertContainer = document.querySelector('.container');
    if (!alertContainer) return;
    
    const alert = document.createElement('div');
    alert.className = `alert alert-${type} alert-dismissible fade show mt-3`;
    alert.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    
    alertContainer.insertBefore(alert, alertContainer.firstChild);
    
    // Auto-dismiss after 5 seconds
    setTimeout(() => {
        if (alert.parentNode) {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }
    }, 5000);
}

function showLoadingState(button) {
    const originalText = button.innerHTML;
    button.innerHTML = '<span class="loading me-2"></span>Processing...';
    button.disabled = true;
    
    // Reset after 10 seconds (fallback)
    setTimeout(() => {
        button.innerHTML = originalText;
        button.disabled = false;
    }, 10000);
}

// Form auto-save functionality (for longer forms)
function initializeFormAutoSave() {
    const enrollmentForm = document.querySelector('#enrollmentForm');
    if (!enrollmentForm) return;
    
    const formData = {};
    const inputs = enrollmentForm.querySelectorAll('input, select, textarea');
    
    // Load saved data
    inputs.forEach(input => {
        const savedValue = localStorage.getItem(`sacdap_form_${input.name}`);
        if (savedValue && input.type !== 'submit') {
            input.value = savedValue;
        }
    });
    
    // Save data on input
    inputs.forEach(input => {
        input.addEventListener('input', () => {
            if (input.type !== 'submit') {
                localStorage.setItem(`sacdap_form_${input.name}`, input.value);
            }
        });
    });
    
    // Clear saved data on successful submission
    enrollmentForm.addEventListener('submit', () => {
        inputs.forEach(input => {
            localStorage.removeItem(`sacdap_form_${input.name}`);
        });
    });
}

// Initialize auto-save if enrollment form exists
document.addEventListener('DOMContentLoaded', initializeFormAutoSave);

// Accessibility enhancements
function enhanceAccessibility() {
    // Add ARIA labels to form elements
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        const inputs = form.querySelectorAll('input, select, textarea');
        inputs.forEach(input => {
            if (!input.getAttribute('aria-label') && !input.getAttribute('aria-labelledby')) {
                const label = form.querySelector(`label[for="${input.id}"]`);
                if (label) {
                    input.setAttribute('aria-labelledby', label.id || 'label-' + input.id);
                }
            }
        });
    });
    
    // Keyboard navigation for custom dropdowns
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Tab') {
            // Ensure focus is visible
            document.body.classList.add('keyboard-navigation');
        }
    });
    
    document.addEventListener('mousedown', () => {
        document.body.classList.remove('keyboard-navigation');
    });
}

// Initialize accessibility enhancements
document.addEventListener('DOMContentLoaded', enhanceAccessibility);

// Performance monitoring
function initializePerformanceMonitoring() {
    // Track page load time
    window.addEventListener('load', () => {
        const loadTime = performance.now();
        console.log(`Page loaded in ${loadTime.toFixed(2)}ms`);
        
        // Log slow loading elements
        if (loadTime > 3000) {
            console.warn('Page load time is slow. Consider optimizing resources.');
        }
    });
    
    // Track JavaScript errors
    window.addEventListener('error', (e) => {
        console.error('JavaScript error:', e.message, 'at', e.filename, ':', e.lineno);
    });
}

// Initialize performance monitoring in development
if (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1') {
    initializePerformanceMonitoring();
}

// Export functions for testing
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        validateField,
        showAlert,
        showLoadingState
    };
}
