# Leather Jacket Management System

A Django web application for managing a leather jacket inventory. Users can add, view, update, and delete jacket records with image upload support.

---

## Tech Stack

- **Backend:** Python, Django
- **Database:** SQLite3
- **Frontend:** HTML Templates (Django template engine)
- **Image Handling:** Pillow (ImageField)

---

## Project Structure

```
leather_project/
├── manage.py
├── db.sqlite3
├── jacket_images/          # Uploaded jacket images
├── leather_project/        # Project settings & URLs
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── jacket/                 # Main app
│   ├── models.py           # Jacket model
│   ├── views.py            # CRUD views
│   ├── forms.py            # JacketForm
│   ├── admin.py            # Admin registration
│   ├── urls.py             # App URL routes
│   └── migrations/
└── templates/              # HTML pages
    ├── base.html
    ├── add.html
    ├── show.html
    ├── update.html
    └── message.html
```

---

## Data Model — `Jacket`

| Field         | Type          | Description                          |
|---------------|---------------|--------------------------------------|
| `j_id`        | AutoField (PK)| Auto-incremented primary key         |
| `name`        | CharField     | Jacket name                          |
| `brand`       | CharField     | Brand name                           |
| `category`    | CharField     | Men / Women / Unisex                 |
| `material`    | CharField     | Leather / Synthetic / Suede          |
| `color`       | CharField     | Jacket color                         |
| `size`        | CharField     | Size (e.g., S, M, L, XL)            |
| `price`       | FloatField    | Price in currency                    |
| `stock`       | IntegerField  | Available quantity                   |
| `description` | TextField     | Detailed product description         |
| `image`       | ImageField    | Optional product image               |

---

## Features

- **Add Jacket** — Fill a form to add a new jacket with image upload
- **View All Jackets** — Display all jacket records in a table
- **Update Jacket** — Edit an existing jacket's details
- **Delete Jacket** — Remove a jacket record by ID
- **Success Messages** — User-friendly feedback after actions

---

## URL Routes

| URL           | View         | Action              |
|---------------|--------------|---------------------|
| `/`           | `addJacket`  | Add a new jacket    |
| `/show/`      | `showAll`    | List all jackets    |
| `/delete`     | `delete`     | Delete a jacket     |
| `/update`     | `update`     | Update a jacket     |

---

## Setup & Run

```bash
# 1. Clone or extract the project
cd leather_project

# 2. Create and activate virtual environment
python -m venv .venv
.venv\Scripts\activate      # Windows
# source .venv/bin/activate  # Linux/Mac

# 3. Install dependencies
pip install django pillow

# 4. Apply migrations
python manage.py migrate

# 5. Run the development server
python manage.py runserver
```

Then open **http://127.0.0.1:8000/** in your browser.

---

## Requirements

- Python 3.10+
- Django 4.x or 5.x
- Pillow (for image uploads)
