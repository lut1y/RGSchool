# Grace School Django Website

## Overview
Grace School is a Django-based website for a sports development school focused on children's training. The platform serves as a modern, SEO-optimized website featuring a content management system for hero images and services, contact form functionality, and a chocolate-themed design aesthetic. The site emphasizes a gentle approach to children's development through various sports disciplines including artistic gymnastics, martial arts, dance, and aerial gymnastics.

## Project Status
- **Current State**: Fully operational Django website running on Replit
- **Setup Date**: September 17, 2025
- **Import Status**: Successfully imported from GitHub and configured for Replit environment

## User Preferences
- Preferred communication style: Simple, everyday language
- Language: Russian (ru-ru)
- Timezone: Europe/Moscow

## Recent Changes
- **September 17, 2025**: 
  - Imported from GitHub repository
  - Configured uv package manager and dependencies
  - Set up Django development server on port 5000
  - Collected static files with WhiteNoise
  - Configured deployment with Gunicorn
  - All pages tested and working correctly

## Project Architecture

### Frontend Architecture
The frontend uses a traditional server-side rendering approach with Django templates, enhanced by Bootstrap 5 for responsive design and modern UI components. The design follows a chocolate color scheme with CSS custom properties for consistent theming.

**Key Frontend Decisions:**
- **Bootstrap 5**: Chosen for rapid development and responsive design capabilities
- **Custom CSS Variables**: Implements a chocolate color scheme for brand consistency
- **Font Awesome Icons**: Provides scalable vector icons for UI elements
- **Minimal JavaScript**: Keeps client-side complexity low while maintaining good UX

### Backend Architecture
Built on Django 5.2.6 following the MVT (Model-View-Template) pattern. The application uses a single Django app called 'main' that handles all functionality.

**Core Models:**
- **HeroImage**: Manages carousel images with ordering, activation status, and automatic image optimization
- **Service**: Handles service/direction listings with descriptions and ordering
- **ContactForm**: Stores contact form submissions with service association

**Key Backend Decisions:**
- **Single App Structure**: Appropriate for current scope while allowing future modularization
- **Image Optimization**: Automatic image resizing and compression using PIL
- **SEO Integration**: Built-in sitemap generation and meta tag management
- **Form Validation**: Django's built-in form system with custom styling and AJAX support

### Data Storage
Uses Django's default SQLite database with proper migration structure. The models include proper verbose names in Russian for the target audience.

### Development Environment Setup
- **Package Manager**: uv (ultrafast Python package installer)
- **Dependencies**: Django 5.2.6, Pillow 11.3.0, WhiteNoise 6.10.0, Gunicorn 23.0.0
- **Static Files**: Collected and served via WhiteNoise middleware
- **Development Server**: Running on 0.0.0.0:5000 for Replit compatibility

### Production Deployment Configuration
- **Deployment Type**: Autoscale (suitable for stateless website)
- **Build Command**: `uv run python manage.py collectstatic`
- **Run Command**: `uv run gunicorn --bind=0.0.0.0:5000 --reuse-port grace_website.wsgi:application`
- **Static File Handling**: WhiteNoise middleware for efficient static file serving

## External Dependencies

### Core Framework
- **Django 5.2.6**: Web framework providing ORM, templating, and admin interface
- **Pillow (PIL)**: Image processing library for automatic image optimization
- **WhiteNoise**: Static file serving middleware for production deployment
- **Gunicorn**: WSGI HTTP server for production deployment

### Frontend Libraries (CDN)
- **Bootstrap 5.3.0**: CSS framework for responsive design and UI components
- **Font Awesome 6.4.0**: Icon library for consistent iconography

### Development Tools
- **uv**: Modern Python package installer and virtual environment manager
- **Django Admin**: Built-in content management system for hero images, services, and contact forms
- **Django Forms**: Form handling and validation system with custom styling

## File Structure
```
├── grace_website/          # Django project configuration
│   ├── settings.py        # Main Django settings
│   ├── urls.py           # Root URL configuration
│   ├── wsgi.py           # WSGI application entry point
│   └── asgi.py           # ASGI application entry point
├── main/                  # Main Django application
│   ├── models.py         # Database models (HeroImage, Service, ContactForm)
│   ├── views.py          # View functions for pages
│   ├── urls.py           # URL routing for main app
│   ├── forms.py          # Django forms
│   ├── admin.py          # Admin interface configuration
│   ├── sitemaps.py       # SEO sitemap configuration
│   └── templates/        # HTML templates
├── static/               # Static files (CSS, JS, robots.txt)
├── media/                # User uploaded files (hero images)
├── staticfiles/          # Collected static files for production
├── pyproject.toml        # uv project configuration
├── requirements.txt      # Python dependencies
├── uv.lock              # uv lock file
├── db.sqlite3           # SQLite database
└── manage.py            # Django management script
```

## Key Features
1. **Multi-page Website**: Home, Services, and Contact pages
2. **Content Management**: Admin interface for managing hero images and services
3. **Contact Form**: AJAX-enabled contact form with server-side validation
4. **SEO Optimization**: XML sitemaps, robots.txt, meta tags
5. **Responsive Design**: Mobile-first Bootstrap 5 layout
6. **Image Optimization**: Automatic image processing for hero carousel
7. **Static File Serving**: Efficient serving via WhiteNoise

## Admin Access
The Django admin interface is available at `/admin/` for content management. Use Django's built-in user management system to create admin accounts.

## Maintenance Notes
- Static files are automatically collected during deployment
- Database migrations are already applied
- All dependencies are locked in uv.lock for reproducible builds
- Images uploaded through admin are automatically optimized