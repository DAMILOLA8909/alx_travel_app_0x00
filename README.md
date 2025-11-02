# 🧭 ALX Travel App

## Overview
**ALX Travel App** is a Django-based web application designed to manage travel listings and related data through a RESTful API.  
This project is part of the ALX backend development curriculum and demonstrates the setup of a Django REST API with proper configuration, Swagger documentation, and database integration.

---

## 🎯 Objective
To set up a Django project with the necessary dependencies, configure the database connection (initially SQLite, later MySQL), and integrate Swagger UI for automatic API documentation.

---

## 🏗️ Project Structure

```pgsql
alx_travel_app/
│
├── alx_travel_app/
│ ├── init.py
│ ├── asgi.py
│ ├── settings.py
│ ├── urls.py
│ ├── wsgi.py
│
├── listings/
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── serializers.py
│ ├── urls.py
│ └── views.py
│
├── manage.py
├── requirements.txt
└── README.md
```


---

## ⚙️ Technologies Used

| Tool | Purpose |
|------|----------|
| **Python 3.12+** | Programming language |
| **Django** | Backend web framework |
| **Django REST Framework (DRF)** | API development |
| **drf-yasg** | Swagger/OpenAPI documentation |
| **django-environ** | Environment variable management |
| **django-cors-headers** | Enable cross-origin requests |
| **Celery** | Task queue for background processing |
| **RabbitMQ** | Message broker for Celery |
| **MySQL / SQLite** | Database management |

---

## 🧩 Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/alx_travel_app.git
cd alx_travel_app
```

### 2️⃣ Create a Virtual Environment
```bash
python -m venv venv
source venv/Scripts/activate  # On Windows (Git Bash)
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Environment Variables

Create a .env file in the project root:
```bash
DEBUG=True
SECRET_KEY=your-secret-key
DB_NAME=your_database_name
DB_USER=your_mysql_username
DB_PASSWORD=your_mysql_password
DB_HOST=localhost
DB_PORT=3306
```

⚠️ When setting up locally, you can keep the SQLite database before switching to MySQL.

---

### ⚙️ Database Configuration
**Default (SQLite)**
```python
By default, the app uses SQLite for ease of development:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

**For MySQL (optional)**

To use MySQL, install the connector:
```bash
pip install mysqlclient
```

Then update your .env with the correct credentials

---

### 🚀 Run the Application
Apply migrations

```bash
python manage.py migrate
```

Start the server
```bash
python manage.py runserver
```

Your app should now be running at:
👉 http://127.0.0.1:8000/

---

### 📘 API Documentation (Swagger)

Once the server is running, open:

👉 http://127.0.0.1:8000/swagger/

This page provides interactive API documentation automatically generated using drf-yasg.

---

### 🧪 Running Tests

```bash
python manage.py test
```

---

### 🧰 Useful Commands

| Command                                   | Description                           |
| ----------------------------------------- | ------------------------------------- |
| `python manage.py runserver`              | Start the local development server    |
| `python manage.py migrate`                | Apply database migrations             |
| `python manage.py createsuperuser`        | Create an admin user                  |
| `python manage.py shell`                  | Open the Django shell                 |
| `celery -A alx_travel_app worker -l info` | Start Celery worker (if using Celery) |

---

### 🗂️ Version Control

This project is managed with Git.
Initialize and make your first commit:

```bash
git init
git add .
git commit -m "Initial project setup with Django, DRF, Swagger, and environment configuration"
git branch -M main
git remote add origin https://github.com/<your-username>/alx_travel_app.git
git push -u origin main
```

---

### 👨‍💻 Author

Damilola Ojo
Industrial Chemistry Graduate | Junior full-stack Developer (in transition to IT)
📧 [damsony.soji@gmail.com]
🌍 GitHub Profile

---

### 🧾 License

This project is licensed under the MIT License – feel free to use and modify it.