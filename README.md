#  My Portfolio Website

[![Python](https://img.shields.io/badge/Python-3.14-3776AB?logo=python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.0-092E20?logo=django)](https://www.djangoproject.com/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-7952B3?logo=bootstrap)](https://getbootstrap.com/)

> A professional, responsive portfolio website built with Django to showcase my skills, projects, and experience.

---

## 🌟 Overview

This is a personal portfolio website featuring a modern design with a home page, about section, skills showcase, and a fully functional contact form. Built with Django on the backend and Bootstrap 5 on the frontend.

---

## ✨ Features

- 🏠 **Home Page** - Hero section with profile image and top skills preview
- 👤 **About Page** - Professional bio, services, and background
- 🎯 **Skills Page** - Dynamic skill bars with proficiency levels
- 📬 **Contact Form** - Fully functional form with database storage
- 📱 **Fully Responsive** - Looks great on mobile, tablet, and desktop
- 🎨 **Modern Design** - Clean UI with Bootstrap 5 and Font Awesome icons
- 🔐 **Admin Panel** - Easy content management via Django admin

---

## 🛠️ Tech Stack

- **Backend:** Django 5.0, Python 3.14
- **Frontend:** HTML5, CSS3, Bootstrap 5, Font Awesome
- **Database:** SQLite (development)
- **Tools:** VS Code, Git, GitHub

---

## 🚀 Quick Start

### Prerequisites
- Python 3.10 or higher
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/DeGoshen/My-Portfolio-Website.git
   cd My-Portfolio-Website





#Create a virtual environment
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # Mac/Linux
   python3 -m venv venv
   source venv/bin/activate

#Dependencies
   pip install django Pillow


#Run Migrations
   python manage.py makemigrations
   python manage.py migrate

#Create a Super User
   python manage.py createsuperuser

#Run Development Server
   python manage.py runserver

#Open Browser 
Main site: http://127.0.0.1:8000/
Admin panel: http://127.0.0.1:8000/admin/

#Project Structure
portfolio_website/
├── portfolio/              # Main app
│   ├── migrations/         # Database migrations
│   ├── templates/          # HTML templates
│   │   ├── base.html
│   │   └── pages/
│   │       ├── home.html
│   │       ├── about.html
│   │       ├── skills.html
│   │       └── contact.html
│   ├── admin.py            # Admin configuration
│   ├── forms.py            # Contact form
│   ├── models.py           # Database models
│   ├── urls.py             # URL routing
│   └── views.py            # View logic
├── static/                 # Static files (images, CSS)
│   └── images/
├── templates/              # Global templates
├── media/                  # Uploaded files
├── manage.py
└── README.md

📝 Usage
Adding Skills
Login to admin panel at /admin
Go to Skills → Add Skill
Enter name, level (0-100), and category
Save and view on the skills page
Managing Contact Messages
Go to Contact Messages in admin
View all submissions
Mark messages as read
🌐 Live Demo
🔗 [Add your live website link here]
📧 Contact
[Your Name]
📧 Email: your.email@example.com
💼 LinkedIn: linkedin.com/in/yourprofile
💻 GitHub: github.com/DeGoshen
📄 License
This project is open source and available under the MIT License.
<div align="center">
Made with ❤️ by <strong>[Your Name]</strong>
</div>



---

## 🎯 Quick Setup Steps

1. **Create the file:**
   - In your project root (where `manage.py` is), create a file named `README.md`

2. **Copy the template above** and paste it into the file

3. **Replace these placeholders:**
   - `[Your Name]` → Your actual name
   - `your.email@example.com` → Your email
   - `linkedin.com/in/yourprofile` → Your LinkedIn URL
   - `[Add your live website link here]` → Your deployed website URL (or remove this section)

4. **Save and commit:**
   ```bash
   git add README.md
   git commit -m "Add README"
   git push origin main

