# Grace School Website

## Overview
Grace School is a sports school website built with Django 5.2.6. The website features information about the school's sports programs including artistic gymnastics, martial arts, dancing, and aerial gymnastics. It includes a contact form for inquiries and showcases the school's services.

## Project Architecture
- **Framework**: Django 5.2.6
- **Database**: SQLite (development), configured for PostgreSQL in production
- **Static Files**: WhiteNoise for static file serving
- **Language**: Russian (ru-ru)
- **Timezone**: Europe/Moscow

## Key Components
- **Main App**: Contains the core website functionality
  - Models: HeroImage, Service, ContactForm
  - Views: Home page, Services page, Contact form
  - Templates: HTML templates with Bootstrap styling
- **Static Files**: CSS and JavaScript assets
- **Media Files**: Hero images and uploads
- **Admin Interface**: Django admin for content management

## Development Setup
The project is configured to run on Replit with:
- Django development server on port 5000
- All hosts allowed for Replit proxy compatibility
- CSRF trusted origins configured for Replit domains
- Static files collected and served via WhiteNoise

## Deployment Configuration
- **Target**: Autoscale deployment
- **Build**: Collects static files via `python manage.py collectstatic --noinput`
- **Run**: Uses Gunicorn WSGI server `gunicorn --bind=0.0.0.0:5000 --reuse-port --workers=2 grace_website.wsgi:application`

### Required Environment Variables for Production
- **SECRET_KEY** or **SESSION_SECRET**: Required for cryptographic signing
- **ALLOWED_HOSTS**: Comma-separated list of allowed hostnames (e.g., "example.com,www.example.com")
- **CSRF_TRUSTED_ORIGINS**: Comma-separated list of trusted origins (e.g., "https://example.com,https://www.example.com")
- **DEBUG**: Set to "False" for production (defaults to "True" for development)

### Security Features
- Production mode enforces HTTPS settings, secure cookies, and HSTS
- Proxy support configured for HTTPS termination
- Host validation required in production
- Proper secret key management

## Recent Changes
- 2025-09-17: Initial Replit setup completed
  - Installed Django dependencies (Django 5.2.6, Pillow, WhiteNoise, Gunicorn)
  - Configured development server workflow on port 5000
  - Set up production-ready deployment configuration
  - Implemented production security settings
  - Added environment variable validation
  - Configured proxy support for HTTPS deployments
  - Verified application functionality

## User Preferences
- Russian language interface
- Sports school focused content
- Professional design with hero images
- Contact form for lead generation