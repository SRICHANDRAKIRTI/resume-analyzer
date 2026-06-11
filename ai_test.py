import ollama

resume_text = """
Python Developer
Skills: Python, AWS, SQL, Machine Learning
Projects: Resume Analyzer, Food Spoilage Detection
"""

prompt = f"""
Analyze this resume.

Resume:
{resume_text}

Give:

1. ATS Score
2. Strengths
3. Weaknesses
4. Missing Skills
5. Suitable Job Roles
6. Interview Questions
   """

response = ollama.chat(
model="llama3",
messages=[
{
"role": "user",
"content": prompt
}
]
)

print(response["message"]["content"])
