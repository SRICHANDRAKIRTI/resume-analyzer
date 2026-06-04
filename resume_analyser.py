import pdfplumber
import re

def analyze_resume(filepath):

    # Read PDF
    with pdfplumber.open(filepath) as pdf:
        text = ""

        for page in pdf.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    # Name Extraction
    lines = text.split("\n")

    candidate_name = "Not Found"

    for line in lines:
        line = line.strip()

        if len(line) > 3:
            candidate_name = line
            break

    # Email Extraction
    email_pattern = r'[\w\.-]+@[\w\.-]+\.\w+'

    emails = re.findall(email_pattern, text)

    email = emails[0] if emails else "Not Found"

    # Phone Number Extraction
    phone_pattern = r'\b\d{10}\b'

    phones = re.findall(phone_pattern, text)

    phone = phones[0] if phones else "Not Found"

    # Convert Text to Lowercase
    lower_text = text.lower()

    # Skills Extraction
    skills_db = [
        "python",
        "java",
        "aws",
        "sql",
        "machine learning",
        "react",
        "nodejs",
        "docker",
        "git"
    ]

    found_skills = []

    for skill in skills_db:
        if skill in lower_text:
            found_skills.append(skill)

    # Education Extraction
    education = []

    education_keywords = [
        "b.tech",
        "b.e",
        "m.tech",
        "m.e",
        "bsc",
        "msc",
        "bca",
        "mca",
        "information technology",
        "computer science"
    ]

    for keyword in education_keywords:
        if keyword in lower_text:
            education.append(keyword)

    # Project Extraction
    projects = []

    if "resume analyzer" in lower_text:
        projects.append("Resume Analyzer")

    if "food spoilage" in lower_text:
        projects.append("Food Spoilage Detection")

    if "machine learning" in lower_text:
        projects.append("Machine Learning Project")

    # Score Calculation
    score = len(found_skills) * 10

    if score > 100:
        score = 100
    if score >= 80:
        rating = "Excellent Resume"
    elif score >= 60:
        rating = "Good Resume"
    else:
        rating = "Average Resume"

    # Suggestions
    suggestions = []

    if len(found_skills) < 5:
        suggestions.append("Add more technical skills")

    if "project" not in lower_text:
        suggestions.append("Add projects section")

    if "certification" not in lower_text:
        suggestions.append("Add certifications")

    if "experience" not in lower_text:
        suggestions.append("Add experience section")

    # Interview Questions
    questions = []

    if "python" in lower_text:
        questions.append("What is Python?")
        questions.append("Explain OOP concepts in Python")

    if "aws" in lower_text:
        questions.append("What is Amazon S3?")
        questions.append("What is AWS Lambda?")

    if "sql" in lower_text:
        questions.append("What is SQL JOIN?")

    # Return Result
    return {
        "name": candidate_name,
        "email": email,
        "phone": phone,
        "skills": found_skills,
        "education": education,
        "projects": projects,
        "score": score,
        "rating":rating,
        "suggestions": suggestions,
        "questions": questions
    }