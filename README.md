# 🚖 Om Sri Bairavar Travels

A modern taxi booking web application built with **Django**, **Python**, and **MySQL**. The platform enables customers to book rides online while allowing the administrator to efficiently manage bookings through the Django Admin dashboard.

---

## 📌 Features

- Online taxi booking form
- Booking confirmation page
- Booking status updates (Pending, Confirmed, Cancelled)
- Responsive user interface
- MySQL database integration
- Static and media file support

---

## 🛠️ Tech Stack

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

### Tools
- Git
- GitHub
- Visual Studio Code

---

## 📂 Project Structure

```
om_sri_bairavar_travels/
│
├── booking/
├── static/
├── media/
├── templates/
├── db.sqlite3 (development only)
├── manage.py
├── requirements.txt
└── README.md
```

---

## 🚀 Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/om-sri-bairavar-travels.git
```

### Move into the project

```bash
cd om-sri-bairavar-travels
```

### Create a virtual environment

Windows

```bash
python -m venv env
env\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv env
source env/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## ⚙️ Configure Database

Update the `DATABASES` section in `settings.py`.

Example:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

---

## 🗄️ Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 👤 Create Admin User

```bash
python manage.py createsuperuser
```

---

## ▶️ Run the Development Server

```bash
python manage.py runserver
```

Open:

```
http://127.0.0.1:8000/
```

Admin Panel:

```
http://127.0.0.1:8000/admin/
```

---

## 📸 Screenshots

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/11567a78-9154-4c2e-b09f-8c2b7b53788f" />


Example:

```
Home Page
Booking Form
Booking Success Page
Admin Dashboard
```

---

## 📋 Booking Workflow

1. Customer opens the website.
2. Customer fills out the booking form.
3. Booking details are stored in the MySQL database.
4. Administrator reviews the booking.
5. Admin updates the booking status.
6. Customer receives confirmation based on the booking status.

---

## 🔐 Admin Features

- View bookings
- Search bookings
- Filter bookings
- Update booking status
- Delete bookings

---

## 🌟 Future Enhancements

- User authentication
- Online payment gateway
- Live cab tracking
- Email notifications
- SMS notifications
- OTP verification
- Driver management
- Booking history
- Invoice generation
- Google Maps integration

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Push to your branch.
5. Open a Pull Request.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Developer

**Mohan P**

- Python Developer
- Django Developer
- Full Stack Web Developer

---

⭐ If you like this project, please give it a Star on GitHub.
