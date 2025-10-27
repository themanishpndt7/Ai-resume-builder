#!/usr/bin/env python3
"""
Update profile skills with categorized format
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from users.models import CustomUser
from resume.models import Profile

# Get the user and profile
user = CustomUser.objects.first()
profile = Profile.objects.get(user=user)

# Update skills with categorized format
profile.skills = """* Technical Skills:
Programming Languages: Python, SQL, HTML, CSS, JavaScript, C (basics)
Data Analysis & Visualization: Power BI, Tableau, Advanced Excel (Pivot Tables, VBA, DAX), Pandas, NumPy, Matplotlib
Machine Learning & AI: Deep Learning, Neural Networks, TensorFlow (basics), Scikit-learn, OpenCV
Databases: MySQL, SQLite, MS Access
Development Tools: Jupyter, Visual Studio, Git, GitHub, Android Studio, Flask

* Professional Skills:
Software Development: SDLC, Modular Programming, Error Handling, Debugging, APIs Integration
Data Analytics: Statistical Analysis, Data Manipulation, Data Visualization, Dashboard Creation, Spreadsheet Expertise
Systems: Windows, Linux, macOS, MS Office (Excel, PowerPoint, Word)

* Core Skills:
Communication, Teamwork, Adaptability, Leadership, Team and Time Management, Critical-Thinking, Problem-Solving, Data-Driven Decision Making, Quick Learning"""

profile.save()

print('✓ Profile skills updated successfully!')
print('')
print('Updated skills format:')
print('=' * 80)
print(profile.skills)
print('=' * 80)
