# 🎓 Student Performance Tracker

The **Student Performance Tracker** is a web-based application developed using **Python (Flask)** and **SQLite**.  
Its primary goal is to help teachers and institutions easily manage student records such as roll numbers, names, subjects, and marks.  
The system allows teachers to **add, view, update, and analyze** student performance in a structured way.  

---

# 📌 Project Overview  

The Student Performance Tracker is a **Flask-based web application** that helps teachers manage student academic records.  
It allows:  
- ➕ Adding students and their subject marks  
- 📝 Updating and managing student data  
- 👀 Viewing student performance  
- 📊 Calculating **overall averages**  
- 🏆 Displaying **subject-wise toppers**  
- 🏅 Displaying the **overall topper**  
- 💾 **Exporting data** to CSV for backup (extra feature)  

The project uses **SQLite** for database storage and can be deployed to **Heroku / Railway / Render** for online access.  

---

# ✨ Features  

- 👩‍🎓 **Add Students**  
  Register students with **Roll Number** & **Name**  

- 📚 **Subject & Marks Entry**  
  Enter **multiple subjects** with marks (**0–100**)  

- 🏆 **Subject-Wise Toppers**  
  Highlight top performer in each subject  

- 🏅 **Overall Topper**  
  Display the best-performing student in the entire class  

- 📊 **Performance Analysis**  
  Show each student’s **average marks**  

- 💾 **Data Persistence & Backup**  
  Store records in **SQLite** + Export to **CSV**  

- 🔍 **Search & Edit** (extra)  
  Quickly find or update student details  

- 🌐 **Deployment Ready**  
  Configured for **Heroku / Render** deployment  

---

# 🛠 Tech Stack  

- **Backend**: Python (Flask)  
- **Database**: SQLite (extendable to MySQL/PostgreSQL)  
- **Frontend**: HTML, CSS, Bootstrap, Jinja2 templates  
- **Deployment**: Heroku / Render / Railway  

---

# 📂 Project Structure  

```bash
student-performance-tracker/
│── app.py              # Flask application
│── db.py               # Database connection helpers
│── models.py           # Student & Tracker classes (OOP)
│── tracker.py          # Core logic for managing students
│── requirements.txt    # Python dependencies
│── Procfile            # Deployment configuration (Heroku)
│── README.md           # Project documentation
│── students.db         # SQLite database (auto-created)
│── students_export.csv # CSV backup (extra feature)
│── templates/          # HTML templates
│   ├── base.html
│   ├── home.html
│   ├── add_student.html
│   ├── add_grade.html
│   ├── list_students.html
│   ├── view_student.html
│   ├── subject_topper.html
│   ├── class_average.html
│   ├── overall_topper.html
│   ├── edit_student.html
│   ├── search.html
│── static/             # CSS, images, JS
│   └── style.css
```
# 🔄 Workflow  

1. Teacher **opens the website**.  
2. Navigates to **Add Student** → enters roll number, name, subjects, and marks.  
3. Data gets stored in **SQLite database**.  
4. Teacher can **View Student List** with averages.  
5. Teacher can **Update / Delete** entries.  
6. Teacher can view **Toppers & Class Average**.  
7. Data can also be **exported to CSV backup**.  

## requirements.txt
- **This file lists all Python dependencies your app needs**:
-**Flask==2.2.5**
-**Flask-SQLAlchemy==2.5.1**
-**SQLAlchemy==1.4.46**
-**gunicorn==20.1.0**

## Procfile
This tells Heroku/Render how to run your app:
web: gunicorn app:app

# Installation & Setup  
### 1. Clone the repository  

- **git clone https://github.com/Nagalakshmi-NU/Student-performance-tracker.git**
- **cd Student-performance-tracker**


### 2. Create environment
- **python -m venv venv**
- **venv\Scripts\activate     # Windows**
- **source venv/bin/activate  # Mac/Linux**

### 3. Install dependencies
- **pip install -r requirements.txt**

### 4. Run the apllication locally
- **python app.py**

### 5. Database Setup
- **The SQLite database (students.db) will be auto-created when you first run app.py.**
- **CSV backup will be available as students_export.csv.**

### Deployment
- **Push to GitHub**
- **Use Heroku/Render for free deployment**
### Heroku Deployment
- **1.Login to Heroku**
- **2.heroku login**
- **3.Create app**
- **heroku create student-performance-tracker**
### Push code
- **git add .**
- **git commit -m "Initial commit"**
- **git push heroku main**
### Open app in browser
- **heroku open**

### Author
- **Nagalakshmi N U**
- **Vault Of Codes Internship Project**