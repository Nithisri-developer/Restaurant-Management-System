# NPP Restaurant Management System 🍽️

A full-stack restaurant management and customer ordering system developed using **Django, MySQL, HTML, CSS, JavaScript, and Bootstrap**.

The project provides a complete restaurant experience with customer-facing pages as well as administrative management features.

---

## 📌 Project Overview

NPP Restaurant Management System is designed to manage restaurant operations while providing customers with a smooth online experience.

Customers can:

- Browse the restaurant menu
- View food details and prices
- Add items to a shopping cart
- Update cart quantities
- Checkout and place orders
- Book tables online
- View their table bookings
- Send messages through the contact page
- Create an account and log in securely

Administrators can manage:

- Products
- Inventory
- Customers
- Orders
- Table bookings
- Contact messages
- Booking status

---

## ✨ Features

### 👤 Customer Features

- Customer registration
- Customer login and logout
- Professional customer homepage
- Responsive navigation bar
- Restaurant menu
- Food category filtering
- Vegetarian / Non-Vegetarian classification
- Shopping cart
- Increase and decrease cart quantities
- Remove items from cart
- Stock-aware cart system
- Checkout page
- Order placement
- Order success page
- Online table booking
- Booking confirmation system
- My Bookings page
- Booking status display
- About page
- Contact page

---

### 🔐 Authentication

The project uses Django's authentication system with a custom user model.

Authentication includes:

- User registration
- Login
- Logout
- Password authentication
- Session management
- Customer account access

The project is also designed to separate **customer functionality from administrative functionality**.

---

### 🛠️ Admin Features

Administrators can manage restaurant data through Django Admin.

Management includes:

- Products
- Product images
- Product prices
- GST
- Stock quantity
- Food style
- Food type
- Customers
- Orders
- Table bookings
- Contact messages

---

### 📅 Table Booking System

Customers can submit table booking requests by providing:

- Name
- Phone number
- Date
- Time
- Number of guests
- Special requests

Each booking initially receives:

`Pending`

Administrators can update the booking status to:

- Pending
- Confirmed
- Cancelled

Customers can view their booking status through **My Bookings**.

---

### 🛒 Shopping Cart

The shopping cart is implemented using Django sessions.

Customers can:

- Add products
- Increase quantity
- Decrease quantity
- Remove products
- View cart total
- Proceed to checkout

The cart also considers available product stock.

---

## 🧰 Technologies Used

### Frontend

- HTML5
- CSS3
- JavaScript
- Bootstrap

### Backend

- Python
- Django

### Database

- MySQL

### Development Tools

- Visual Studio Code
- MySQL Workbench
- Git
- GitHub

---

## 📂 Project Structure

```text
Djangoc/
│
├── DjangoProject/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── Inventory/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   └── admin.py
│
├── OrderManagement/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── UserManagement/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── CustomerSite/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── templates/
│   ├── customer/
│   ├── customer_base.html
│   ├── customer_navbar.html
│   ├── login.html
│   └── signup.html
│
├── static/
│   ├── css/
│   ├── js/
│   └── assets/
│
├── media/
│   └── images/
│
├── manage.py
└── README.md