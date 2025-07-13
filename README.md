
# 🚂 KPA Form Assignment – Backend API (Django)

This is a backend project developed as part of the **KPA Form Assignment**. The objective is to implement two APIs from the provided Postman collection using Django REST Framework and PostgreSQL.

---

## 📌 Project Overview

This project implements two core APIs:

1. **POST /api/forms/wheel-specifications/**  
   ➤ Submits a new wheel specification form with detailed nested data.

2. **GET /api/forms/wheel-specifications/**  
   ➤ Retrieves filtered wheel specification forms using query parameters like `formNumber`, `submittedBy`, and `submittedDate`.

Both APIs are tested and designed as per the structure given in the [KPA Postman collection](https://app.swaggerhub.com/apis/sarvasuvidhaen/kpa-form_data/1.0.0).

---

## ⚙️ Tech Stack

| Component      | Tech                                |
|----------------|-------------------------------------|
| Language       | Python 3.10+                        |
| Framework      | Django 4.2, Django REST Framework   |
| Database       | PostgreSQL                          |
| API Testing    | Postman (Web Version)               |
| Config         | `.env` with `python-dotenv`         |

---

## 📁 Project Structure
kpa_project/
│
├── api/ # Main app
│ ├── models.py # Models for forms and nested fields
│ ├── serializers.py # Nested serializers for clean structure
│ ├── views.py # DRF API views (POST + GET)
│ ├── urls.py # App-level routing
│ └── admin.py # Admin panel config
│
├── kpa_project/ # Django settings & root config
│ ├── settings.py
│ └── urls.py
│
├── requirements.txt # Python dependencies
├── README.md # You are here!
└── manage.py



---

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Gaurav-mishra2003/Backend_Assignment/
cd projec_name
### Create Virtual Environment
python -m venv venv
source venv/bin/activate   # On Windows use: venv\\Scripts\\activate

### Install Dependencies
pip install -r requirements.txt
###  Setup Environment Variables
SECRET_KEY=your_secret_key_here
DEBUG=True
DB_NAME=kpa_db
DB_USER=postgres
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432


### Apply Migrations
python manage.py makemigrations
python manage.py migrate

### Create Superuser
python manage.py createsuperuser

 ### Start Server

python manage.py runserver


🧪 API Testing Guide (Postman Web)
Go to https://web.postman.co

Import the KPA_form_data.postman_collection.json collection

Use the following endpoints:

✅ POST - Wheel Specification Submission
URL:
POST http://localhost:8000/api/forms/wheel-specifications/

#### Body:

{
  "formNumber": "WHEEL-2025-001",
  "submittedBy": "user_id_123",
  "submittedDate": "2025-07-03",
  "fields": {
    "treadDiameterNew": "915 (900-1000)",
    "wheelGauge": "1600 (+2,-1)"
  }
}
#### Response:

{
  "success": true,
  "message": "Wheel specification submitted successfully.",
  "data": {
    "formNumber": "WHEEL-2025-001",
    "submittedBy": "user_id_123",
    "submittedDate": "2025-07-03",
    "status": "Saved"
  }
}
✅ GET - Wheel Specification Filters
URL:
GET http://localhost:8000/api/forms/wheel-specifications?formNumber=WHEEL-2025-001

#### Response:


{
  "success": true,
  "message": "Filtered wheel specification forms fetched successfully.",
  "data": [
    {
      "formNumber": "WHEEL-2025-001",
      "submittedBy": "user_id_123",
      "submittedDate": "2025-07-03",
      "fields": {
        "treadDiameterNew": "915 (900-1000)",
        "wheelGauge": "1600 (+2,-1)"
      }
    }
  ]
}
