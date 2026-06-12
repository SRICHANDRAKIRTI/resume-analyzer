# 🚀 AI Resume Analyzer

An AI-powered Resume Analyzer built using **Python, Flask, Gemini AI, AWS S3, and Render**.

This application analyzes resumes, calculates ATS scores, extracts skills, identifies missing skills, suggests suitable job roles, generates interview questions, and provides AI-powered resume insights.

---

## 🌐 Live Demo

Live Application:

https://resume-analyzer-3r32.onrender.com

---

## ✨ Features

### 📄 Resume Parsing

* Extracts Candidate Name
* Extracts Email Address
* Extracts Phone Number

### 🎯 ATS Score Analysis

* Calculates ATS Score
* Resume Rating
* Resume Strength Analysis

### 🛠 Skills Detection

* Python
* Java
* AWS
* SQL
* Machine Learning
* React
* Docker
* Git
* NodeJS

### 🎓 Education Detection

* B.E
* B.Tech
* MCA
* BCA
* Computer Science
* Information Technology

### 💡 AI Resume Insights

Using Google Gemini AI:

* Strengths Analysis
* Weakness Analysis
* Missing Skills Detection
* Suitable Job Roles
* Interview Questions Generation

### 📊 Resume Dashboard

* Professional UI
* ATS Score Progress Bar
* Skills Section
* Education Section
* Projects Section
* AI Insights Section

### ☁ Cloud Integration

* AWS S3 Resume Upload
* Cloud Storage Support

### 📑 Report Generation

* Download PDF Report

---

## 🏗 Tech Stack

### Backend

* Python
* Flask

### AI

* Google Gemini AI

### Cloud

* AWS S3

### Frontend

* HTML
* CSS
* Jinja2

### Deployment

* Render

### PDF Processing

* pdfplumber
* reportlab

---

## 📂 Project Structure

resume-analyzer/

├── app.py

├── resume_analyser.py

├── requirements.txt

├── static/

│   └── style.css

├── templates/

│   ├── index.html

│   └── result.html

├── uploads/

├── report.pdf

└── README.md

---

## ⚙ Installation

### Clone Repository

```bash
git clone https://github.com/SRICHANDRAKIRTI/resume-analyzer.git

cd resume-analyzer
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Environment Variables

Create environment variables:

```env
AWS_ACCESS_KEY=your_access_key

AWS_SECRET_KEY=your_secret_key

GEMINI_API_KEY=your_gemini_api_key
```

### Run Application

```bash
python app.py
```

Application runs at:

```text
http://127.0.0.1:5000
```

---

## 📸 Screenshots

### Home Page

* Resume Upload Interface

### Dashboard

* ATS Score
* Skills
* Missing Skills
* Job Roles
* AI Insights

### PDF Report

* Downloadable Analysis Report

---

## 🚀 Future Enhancements

* User Login & Registration
* Resume History Tracking
* Resume vs Job Description Matching
* Resume Ranking System
* Resume Comparison Tool
* MongoDB Integration
* Email Report Generation
* Admin Dashboard

---

## 👨‍💻 Author

SRICHANDRAKIRTI

GitHub:
https://github.com/SRICHANDRAKIRTI

---

## ⭐ Support

If you like this project:

⭐ Star the Repository

🍴 Fork the Repository

🚀 Share with Others

---

## 📜 License

This project is created for educational and portfolio purposes.
