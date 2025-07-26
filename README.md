# E-Commerce Django Project

This is an E-Commerce web application built with Django, featuring a responsive design and modern user interface. The project implements core e-commerce functionalities with a clean, modular architecture.

## Features
- User authentication and authorization system
- Product categorization and management
- Dynamic shopping cart functionality
- Responsive product detail and listing pages
- Admin interface for content management
- Context processors for cart counter and category menu

## Technology Stack
### Backend
- **Django 3.1** - High-level Python web framework that encourages rapid development and clean, pragmatic design
- **SQLite3** - Lightweight, file-based database (default)
- **Python 3.8+** - Programming language used for backend development

### Frontend
- **Bootstrap** - Frontend framework for responsive design
- **jQuery** - JavaScript library for DOM manipulation and AJAX requests
- **Font Awesome** - Icon library and toolkit
- **Custom CSS/JS** - Custom styling and interactive features

### Development Tools
- **pip** - Python package installer
- **virtualenv** - Tool to create isolated Python environments
- **Django Template Language** - Template engine for dynamic HTML generation

## Requirements
- Python 3.8 or higher
- pip (Python package manager)
- Git (for version control)

## Setup Instructions

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd E-Commerce_backup
```

### 2. Create and activate a virtual environment (optional but recommended)
On Windows:
```bash
python -m venv pyVenv
pyVenv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install Django==3.1 asgiref==3.2.10 pytz==2025.2 sqlparse==0.5.3 tzdata==2025.2
```

### 4. Apply migrations
```bash
python manage.py migrate
```

### 5. Create a superuser (admin account)
```bash
python manage.py createsuperuser
```
Follow the prompts to create your admin account.

### 6. Run the development server
```bash
python manage.py runserver
```

Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.
Admin interface is available at [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

## Project Structure
- `accounts/` - User authentication, registration, and profile management
- `category/` - Product category models and views with context processors for menu
- `store/` - Core product-related functionality including listings and detail views
- `carts/` - Shopping cart implementation with session management
- `templates/` - HTML templates organized by app and feature
- `static/` - Static assets (CSS, JavaScript, images, fonts)
- `onlineECommerce/` - Project configuration and root URL routing

## Development Notes
- The default database is SQLite (configured in `onlineECommerce/settings.py`)
- Debug mode is enabled by default for development
- For production deployment:
  - Set `DEBUG = False` in settings.py
  - Configure `ALLOWED_HOSTS`
  - Set up a production-grade database (e.g., PostgreSQL)
  - Configure static files serving
  - Set up proper security measures (SSL, secure cookies, etc.)

## Contributing
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License
This project is created for Practice purposes. Feel free to use it as a learning resource or template for your own projects. 