# replit.md

## Overview

Grace School is a Django-based website for a sports development school focused on children's training. The platform serves as a modern, SEO-optimized website featuring a content management system for hero images and services, contact form functionality, and a chocolate-themed design aesthetic. The site emphasizes a gentle approach to children's development through various sports disciplines including artistic gymnastics, martial arts, dance, and aerial gymnastics.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend Architecture
The frontend uses a traditional server-side rendering approach with Django templates, enhanced by Bootstrap 5 for responsive design and modern UI components. The design follows a chocolate color scheme with CSS custom properties for consistent theming. JavaScript is minimal and focuses on essential UX enhancements like smooth scrolling and automatic alert dismissal.

**Key Frontend Decisions:**
- **Bootstrap 5**: Chosen for rapid development and responsive design capabilities
- **Custom CSS Variables**: Implements a chocolate color scheme for brand consistency
- **Font Awesome Icons**: Provides scalable vector icons for UI elements
- **Minimal JavaScript**: Keeps client-side complexity low while maintaining good UX

### Backend Architecture
Built on Django 5.2.6 following the MVT (Model-View-Template) pattern. The application uses a single Django app called 'main' that handles all functionality including content management, contact forms, and SEO features.

**Core Models:**
- **HeroImage**: Manages carousel images with ordering, activation status, and automatic image optimization
- **Service**: Handles service/direction listings with descriptions and ordering
- **ContactForm**: Stores contact form submissions with service association

**Key Backend Decisions:**
- **Single App Structure**: Appropriate for the current scope while allowing future modularization
- **Image Optimization**: Automatic image resizing and compression using PIL for performance
- **SEO Integration**: Built-in sitemap generation and meta tag management
- **Form Validation**: Django's built-in form system with custom styling and AJAX support

### Data Storage
Uses Django's default SQLite database for development with clear migration structure. The models include proper verbose names in Russian, indicating the target audience locale.

**Database Design Decisions:**
- **SQLite**: Suitable for development and small-scale deployment
- **Ordering Fields**: Built-in ordering capabilities for hero images and services
- **File Upload Management**: Organized media file structure with validation
- **Soft Deletion**: Uses is_active flags instead of hard deletion for content management

### SEO and Performance Features
Implements comprehensive SEO features including XML sitemaps, robots.txt, and meta tag management. The system includes automatic image optimization and proper semantic HTML structure.

**SEO Architecture:**
- **Django Sitemaps Framework**: Automatic sitemap generation for static pages and services
- **Meta Tag Management**: Context-based meta descriptions and keywords
- **Image Optimization**: Automatic resizing and compression for hero images
- **Robots.txt**: Proper search engine directive management

## External Dependencies

### Core Framework
- **Django 5.2.6**: Web framework providing ORM, templating, and admin interface
- **Pillow (PIL)**: Image processing library for automatic image optimization
- **WhiteNoise**: Static file serving middleware for production deployment

### Frontend Libraries
- **Bootstrap 5.3.0**: CSS framework for responsive design and UI components
- **Font Awesome 6.4.0**: Icon library for consistent iconography

### Deployment Dependencies
- **WhiteNoise Middleware**: Handles static file serving in production environments
- **ASGI/WSGI Configuration**: Standard Django deployment interfaces

### Development Tools
- **Django Admin**: Built-in content management system for hero images, services, and contact forms
- **Django Forms**: Form handling and validation system with custom styling
- **Django Static Files**: Asset management and serving system

### Third-Party Integrations
Currently, the application operates as a standalone system without external API integrations. Future integrations may include:
- Email service providers for contact form notifications
- Analytics platforms for user behavior tracking
- Payment gateways if enrollment features are added