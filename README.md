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
# 🔄 Workflow  

1. Teacher **opens the website**.  
2. Navigates to **Add Student** → enters roll number, name, subjects, and marks.  
3. Data gets stored in **SQLite database**.  
4. Teacher can **View Student List** with averages.  
5. Teacher can **Update / Delete** entries.  
6. Teacher can view **Toppers & Class Average**.  
7. Data can also be **exported to CSV backup**.  

---

# ⚙️ Installation & Setup  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/Nagalakshmi-NU/Student-performance-tracker.git
cd Student-performance-tracker
### 2️⃣ Create Virtual Environment  

Run the following command to create a virtual environment:  
```bash
python -m venv venv
