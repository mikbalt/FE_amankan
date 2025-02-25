# Django Admin Dashboard

A frontend application for an admin dashboard built with Django, connected to a separate Django backend API for data management.

## Description

Django Admin Dashboard is a web application designed to provide a user-friendly admin interface. It is built with Django as the frontend framework and connected to a separate Django backend API for data management. The dashboard provides an intuitive view for system management, viewing statistical data, and performing CRUD operations.

## Features

- **Authentication System**: Secure login page with input validation
- **Interactive Dashboard**: Main view with statistics and data summaries
- **Responsive Design**: Adapts to various device sizes
- **API Integration**: Connected to a Django backend API
- **Modern UI**: Clean and intuitive user interface using Bootstrap 5
- **Security**: Session management and token authentication

## Screenshots

![Login Page](static/images/login-screenshot.png)  
![Dashboard Page](static/images/dashboard-screenshot.png)  

## Technologies Used

- Django 4.x
- Bootstrap 5
- JavaScript
- HTML5 & CSS3
- Python Requests (for API communication)
- python-dotenv (for environment variables)

## Prerequisites

- Python 3.8 or later
- pip (Python package manager)
- Running Django Backend API

## Installation and Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/django-admin-dashboard.git
   cd django-admin-dashboard
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   
   # For Windows
   venv\Scripts\activate
   
   # For Linux/Mac
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory with the following content:
   ```
   DEBUG=True
   SECRET_KEY=your-secret-key-here
   API_BASE_URL=http://your-backend-api-url
   ```

5. Run migrations:
   ```bash
   python manage.py migrate
   ```

6. Start the development server:
   ```bash
   python manage.py runserver
   ```

7. Open a browser and visit `http://127.0.0.1:8000/login/`

## Usage

1. Log in using valid credentials on the login page
2. Upon successful authentication, you will be redirected to the main dashboard
3. Use the sidebar for navigation to different parts of the application
4. Logout when you are done using the system

## Project Structure

```
admin_dashboard/
│
├── admin_dashboard/        # Main Django project directory
│   ├── __init__.py
│   ├── settings.py         # Django configuration
│   ├── urls.py             # Main URL configuration
│   └── wsgi.py             # WSGI configuration
│
├── dashboard/              # Dashboard app
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py             # Dashboard app URLs
│   └── views.py            # Dashboard app views
│
├── static/                 # Static files (CSS, JS, images)
│   ├── css/
│   │   ├── login.css
│   │   └── dashboard.css
│   ├── js/
│   │   ├── login.js
│   │   └── dashboard.js
│   └── images/
│
├── templates/              # HTML templates
│   └── dashboard/
│       ├── login.html
│       └── home.html
│
├── .env                    # Environment variables
├── .gitignore
├── manage.py
├── requirements.txt
└── README.md
```

## Development

### Adding a New Page

1. Create a new HTML template in `templates/dashboard/`
2. Add a new view in `dashboard/views.py`
3. Add a new URL in `dashboard/urls.py`
4. Add a link to the new page in the sidebar navigation

### Changing the UI

1. Edit CSS files in the `static/css/` directory
2. If needed, add a new CSS file and import it in the template

### Modifying API Connection

Edit the `call_api()` function in `dashboard/views.py` to change how the application communicates with the backend API.

## Deployment

For production deployment:

1. Set `DEBUG=False` in the `.env` file
2. Use a WSGI server like Gunicorn
3. Configure Nginx or Apache as a reverse proxy
4. Move static files using `python manage.py collectstatic`

## Contribution

Feel free to contribute to this project by following these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

M. Ikbal Taqyudin - [@ikbaltaqyudin](https://twitter.com/twitter_handle) - ikbaltaqyudin@gmail.com

Project Link: [https://github.com/yourusername/django-admin-dashboard](https://github.com/yourusername/django-admin-dashboard)