# Django Admin Dashboard Setup Guide

This document provides detailed instructions on how to set up and run the Django Admin Dashboard application from scratch.

---

## Prerequisites

Before starting, make sure your system meets the following requirements:

1. **Python 3.8 or higher** - [Download Python](https://www.python.org/downloads/)
2. **pip** (Python package manager)
3. **git** - [Download Git](https://git-scm.com/downloads)
4. **Django Backend API** running and accessible

---

## Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/django-admin-dashboard.git
cd django-admin-dashboard
```

---

## Step 2: Set Up Virtual Environment

### For Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### For macOS/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not available, create one with the following content:

```
django==4.2.9
requests==2.31.0
python-dotenv==1.0.0
```

---

## Step 4: Environment Configuration

Create a `.env` file in the root directory of the project with the following content:

```
DEBUG=True
SECRET_KEY=change-this-to-a-secure-random-string
API_BASE_URL=http://your-backend-api-url
```

Make sure to replace `SECRET_KEY` with a secure random string and `API_BASE_URL` with your backend API URL.

---

## Step 5: Apply Database Migrations

Although this project mainly acts as a frontend, Django still requires some basic database tables:

```bash
python manage.py migrate
```

---

## Step 6: Run Development Server

```bash
python manage.py runserver
```

The application will now be accessible at http://127.0.0.1:8000/login/

---

## Step 7: Verify Connection to Backend API

Ensure that your backend API is running and accessible from the frontend application. You can test the connection by attempting to log in using valid credentials.

---

---

## Additional Configuration

### Changing Server Port

If port 8000 is already in use, you can run the server on another port:

```bash
python manage.py runserver 8080
```

---

### Accessing from Other Devices on the Network

To access the server from other devices on the same network:

```bash
python manage.py runserver 0.0.0.0:8000
```

Then, access using your computer's IP address, e.g., http://192.168.1.100:8000

---

### Configuring Static Files for Production

For production environments, run:

```bash
python manage.py collectstatic
```

---

## Required Backend API Structure

The backend API should provide the following endpoints:

1. **Authentication**
   - POST `/auth/login/` - For logging in (accepts username and password, returns a token)
   - POST `/auth/logout/` - For logging out (optional)

2. **Dashboard Data**
   - GET `/dashboard/data/` - To get main dashboard data

Each API endpoint should return responses in JSON format.

---

## Troubleshooting

### API Connection Issues

If you encounter issues connecting to the backend API:

1. Check if the API URL is correct in the `.env` file
2. Ensure the backend API is running
3. Check for CORS issues by enabling CORS on the backend

---

### Static Files Not Loading

If static files are not loading correctly:

1. Check the `STATIC_URL` and `STATICFILES_DIRS` configuration in `settings.py`
2. Make sure the files are in the correct location
3. Run `python manage.py collectstatic`

---

### Error "ModuleNotFoundError"

If you see this error, make sure all dependencies are installed:

```bash
pip install -r requirements.txt
```

---

## Production Deployment

For production deployment, the following additional steps are recommended:

1. Change `DEBUG=False` in the `.env` file
2. Use a WSGI server like Gunicorn:
   ```bash
   pip install gunicorn
   gunicorn admin_dashboard.wsgi:application
   ```
3. Configure Nginx or Apache as a reverse proxy
4. Enable HTTPS using SSL certificates
5. Configure static files to be served by the web server

---

## Additional Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Django REST framework Documentation](https://www.django-rest-framework.org/) (for backend)
- [Bootstrap Documentation](https://getbootstrap.com/docs/)

---

## Support and Contact

If you encounter issues not covered in this guide, please contact:

- Email: ikbaltaqyudin@gmail.com
- GitHub Issues: Create a new issue on the repository

---

Happy coding! 🚀