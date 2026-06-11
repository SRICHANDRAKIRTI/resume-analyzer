from flask import Flask, render_template, request, send_file
import os
import json
from resume_analyser import analyze_resume
#from aws_config import s3, BUCKET_NAME
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():

    resume = request.files["resume"]

    filepath = os.path.join(
        app.config["UPLOAD_FOLDER"],
        resume.filename
    )

    resume.save(filepath)

    s3.upload_file(
    filepath,
    BUCKET_NAME,
    resume.filename
)

    print("Resume uploaded to S3 successfully")

    result = analyze_resume(filepath)

    return render_template(
        "result.html",
        name=result["name"],
        email=result["email"],
        phone=result["phone"],
        score=result["score"],
        rating=result["rating"],
        skills=result["skills"],
        ats_score=result["ats_score"],
        job_roles=result["job_roles"],
        missing_skills=result["missing_skills"],
        education=result["education"],
        projects=result["projects"],
        suggestions=result["suggestions"],
        questions=result["questions"],
        ai_analysis=result["ai_analysis"],
        strengths=result["strengths"],
        weaknesses=result["weaknesses"],
        ai_missing_skills=result["ai_missing_skills"],
        ai_job_roles=result["ai_job_roles"],
        ai_questions=result["ai_questions"]
    )


@app.route("/download")
def download():
    pdf_file = "resume_report.pdf"

    doc = SimpleDocTemplate(pdf_file)

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "AI Resume Analysis Report",
            styles["Title"]
        )
    )

    content.append(Spacer(1, 20))

    content.append(
        Paragraph(
            "Generated Successfully by AI Resume Analyzer",
            styles["Normal"]
        )
    )

    content.append(Spacer(1, 20))

    content.append(
        Paragraph(
            "This report contains AI-based resume analysis results.",
            styles["Normal"]
        )
    )

    content.append(Spacer(1, 20))

    content.append(
        Paragraph(
            "Features Included:",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            "- Resume Score<br/>"
            "- ATS Score<br/>"
            "- Skills Analysis<br/>"
            "- Missing Skills Detection<br/>"
            "- Job Role Suggestions<br/>"
            "- AI Interview Questions",
            styles["Normal"]
        )
    )

    doc.build(content)

    return send_file(
        pdf_file,
        as_attachment=True
    )


if __name__ == "__main__":
    app.run(debug=True)