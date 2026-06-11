import pdfplumber
import re
import google.generativeai as genai
import os

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-1.5-flash")

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

    # ATS Score

    ats_score = score + 20

    if ats_score > 100:
        ats_score = 100


    # Job Role Matching

    job_roles = []

    if "python" in found_skills:
        job_roles.append("Python Developer")

    if "aws" in found_skills:
        job_roles.append("AWS Cloud Engineer")

    if "machine learning" in found_skills:
        job_roles.append("Machine Learning Engineer")

    if "sql" in found_skills:
        job_roles.append("Database Developer")

    if len(job_roles) == 0:
        job_roles.append("General Software Developer")


    # Missing Skills Detection

    required_skills = [
        "python",
        "sql",
        "git",
        "docker",
        "aws",
        "kubernetes"
    ]

    missing_skills = []

    for skill in required_skills:
        if skill not in found_skills:
            missing_skills.append(skill)
    
    strengths = []
    weaknesses = []
    ai_missing_skills = []
    ai_job_roles = []
    ai_questions = []

    ai_analysis = "AI Analysis Not Available"

    # AI Resume Analysis

    try:

            prompt = f"""
                Analyze this resume and return ONLY in this format:

                STRENGTHS:
                - point 1
                - point 2

                WEAKNESSES:
                - point 1
                - point 2

                MISSING_SKILLS:
                - point 1
                - point 2

                JOB_ROLES:
                - role 1
                - role 2

                INTERVIEW_QUESTIONS:
                - question 1
                - question 2

                Resume:
                {text}
                """

            response = model.generate_content(prompt)

            ai_analysis = response.text

            # Parse AI Response

            strengths = []
            weaknesses = []
            ai_missing_skills = []
            ai_job_roles = []
            ai_questions = []

            current_section = None

            for line in ai_analysis.split("\n"):

                line = line.strip()

                if "STRENGTHS" in line.upper():
                    current_section = "strengths"
                    continue

                elif "WEAKNESSES" in line.upper():
                    current_section = "weaknesses"
                    continue

                elif "MISSING_SKILLS" in line.upper():
                    current_section = "missing_skills"
                    continue

                elif "JOB_ROLES" in line.upper():
                    current_section = "job_roles"
                    continue

                elif "INTERVIEW_QUESTIONS" in line.upper():
                    current_section = "questions"
                    continue

                if line.startswith("-"):

                    item = line.replace("-", "").strip()

                    if current_section == "strengths":
                        strengths.append(item)

                    elif current_section == "weaknesses":
                        weaknesses.append(item)

                    elif current_section == "missing_skills":
                        ai_missing_skills.append(item)

                    elif current_section == "job_roles":
                        ai_job_roles.append(item)

                    elif current_section == "questions":
                        ai_questions.append(item)

    except Exception as e:

        ai_analysis = str(e)

        strengths = [str(e)]
        weaknesses = [str(e)]

        ai_missing_skills = []
        ai_job_roles = []
        ai_questions = []
    # Return Result
    return {
    "name": candidate_name,
    "email": email,
    "phone": phone,
    "skills": found_skills,
    "education": education,
    "projects": projects,
    "score": score,
    "ats_score": ats_score,
    "rating": rating,
    "job_roles": job_roles,
    "missing_skills": missing_skills,
    "suggestions": suggestions,
    "questions": questions,
    "ai_analysis": ai_analysis,
    "strengths": strengths,
    "weaknesses": weaknesses,
    "ai_missing_skills": ai_missing_skills,
    "ai_job_roles": ai_job_roles,
    "ai_questions": ai_questions
}