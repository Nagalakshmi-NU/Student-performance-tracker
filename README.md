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
