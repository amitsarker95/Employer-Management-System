﻿# 🏢 Employer Management System (Django REST Framework)

A simple RESTful API for managing employers, built using Django and Django REST Framework (DRF). This project includes custom user authentication (via email and password) and JWT-based authorization using Simple JWT.

---

## 📋 Features

- 🔐 Custom user model (email login, no username)
- 🛡 JWT authentication (access and refresh tokens)
- ✅ User registration, login, logout, profile
- 🏢 Full CRUD API for managing Employers
- 🔒 Secure employer access (user-specific permissions)
- ⚙️ Clean structure using DRF best practices (serializers, viewsets, routers)

---
### 1. Clone the Repository

```
https://github.com/amitsarker95/Employer-Management-System.git
cd employer-management-system

```
## 2 Create a Virtual Environment
<pre> <code>

python -m venv venv 
venv/scripts/activate 

</code> </pre>

## 3 Install Dependencies

```
pip install -r requirements.txt

```

## 4 Apply Migrations

```
python manage.py makemigrations
python manage.py migrate

```
## 5 Run the server

## Authorization: JWT <your_access_token>

### API Endpoints

# Authentication

| Method | Endpoint             | Description              |
| ------ | -------------------- | ------------------------ |
| POST   | `/api/auth/signup/`  | Register a new user      |
| POST   | `/api/auth/login/`   | Login and get tokens     |
| POST   | `/api/auth/logout/`  | Logout (blacklist token) |
| GET    | `/api/auth/profile/` | Get current user profile |

# Employer

| Method | Endpoint               | Description                  |
| ------ | ---------------------- | ---------------------------- |
| POST   | `/api/employers/`      | Create a new employer        |
| GET    | `/api/employers/`      | List all your employers      |
| GET    | `/api/employers/<id>/` | Retrieve a specific employer |
| PUT    | `/api/employers/<id>/` | Update a specific employer   |
| DELETE | `/api/employers/<id>/` | Delete a specific employer   |

## User Create Demo Json Data
```
{
  "full_name": "John Doe",
  "email": "johndoe@example.com",
  "password": "StrongPassword123",
  "password2": "StrongPassword123"
}
```
## Employer Create Demo Json Data

```
{
  "user": 1,
  "company_name": "Softvance",
  "contact_person_name": "Amit Sarker",
  "email": "amitsarker95@gmail.com",
  "phone_number": "+8801718332515",
  "address": "Hospital Road, Netrakona"
}

```



