from flask import Flask, render_template, request, send_file
import os
import json
from resume_analyser import analyze_resume

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

    result = analyze_resume(filepath)

    return render_template(
        "result.html",
        name=result["name"],
        email=result["email"],
        phone=result["phone"],
        score=result["score"],
        rating=result["rating"],
        skills=result["skills"],
        education=result["education"],
        projects=result["projects"],
        suggestions=result["suggestions"],
        questions=result["questions"]
    )


@app.route("/download")
def download():

    report = {
        "name": "Resume Candidate",
        "status": "Resume Analyzed Successfully"
    }

    with open("resume_report.json", "w") as file:
        json.dump(report, file, indent=4)

    return send_file(
        "resume_report.json",
        as_attachment=True
    )


if __name__ == "__main__":
    app.run(debug=True)