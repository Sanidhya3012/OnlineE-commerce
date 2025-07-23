# E-Commerce Django Project

This is an E-Commerce web application built with Django.

## Features
- User authentication
- Product categories
- Shopping cart
- Product detail and listing pages

## Requirements
- Python 3.8+
- pip

## Setup Instructions

### 1. Clone the repository
```
git clone <your-repo-url>
cd E-Commerce_backup
```

### 2. Create and activate a virtual environment (optional but recommended)
On Windows:
```
python -m venv pyVenv
pyVenv\Scripts\activate
```

### 3. Install dependencies
```
pip install Django==3.1 asgiref==3.2.10 pytz==2025.2 sqlparse==0.5.3 tzdata==2025.2
```

### 4. Apply migrations
```
python manage.py migrate
```

### 5. Create a superuser (admin account)
```
python manage.py createsuperuser
```

### 6. Run the development server
```
python manage.py runserver
```

Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

## Project Structure
- `accounts/` - User accounts and authentication
- `category/` - Product categories
- `store/` - Product listings and details
- `carts/` - Shopping cart functionality
- `templates/` - HTML templates
- `static/` - Static files (CSS, JS, images)

## Notes
- The default database is SQLite (see `onlineECommerce/settings.py`).
- For production, set `DEBUG = False` and configure `ALLOWED_HOSTS`.
- Static files are served automatically in development. For production, use Django's static files handling.

## License
This project is for educational purposes. 