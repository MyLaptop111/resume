resume_data = {
    "name": "Mohab Mohamed",
    "email": "mohabeldesouky925@gmail.com.com",
    "phone": "+201555096993",
    "github": "https://github.com/MyLaptop111",
    "linkedin": "https://www.linkedin.com/in/mohab-mohamed-b9b484327?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=ios_app",
    "skills": ["Python", "Engineering", "C","Matalab","Ml"],
    "projects": [
        {"title": "Iris Recognition", "description": "MATLAB-based recognition using Sobel and histogram features."},
        {"title": "Face Recognition", "description": "Skin color segmentation and Euclidean matching in MATLAB."},
        {"title" : "Digital Clock","descriptopn": "Logic gates to make digital clock and stop watch"}
    ]
}

with open("resume.md", "w") as file:
    file.write(f"# {resume_data['name']}\n\n")
    file.write(f"**Email:** {resume_data['email']}  \n")
    file.write(f"**Phone:** {resume_data['phone']}  \n")
    file.write(f"**GitHub:** [{resume_data['github']}]({resume_data['github']})  \n")
    file.write(f"**LinkedIn:** [{resume_data['linkedin']}]({resume_data['linkedin']})\n\n")
    
    file.write("## 🛠 Skills\n\n")
    file.write("- " + "  \n- ".join(resume_data['skills']) + "\n\n")
    
    file.write("## 🏆 Projects\n\n")
    for project in resume_data['projects']:
        file.write(f"**{project['title']}**  \n- {project['description']}\n\n")
