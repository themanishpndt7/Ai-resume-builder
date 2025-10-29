#!/usr/bin/env python3
"""
Test the rewrite_skills_section function
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from users.models import CustomUser
from resume.utils import rewrite_skills_section

# Get the user
user = CustomUser.objects.first()

# Test with sample AI-generated resume content
test_resume = """# Manish Sharma

Email: user@example.com | Phone: +91 7982682852

## Career Objective

Aspiring AI & Machine Learning Engineer...

## Skills

- Python
- SQL
- HTML
- C (Basics)
- Power BI
- Tableau
- Advanced Excel

## Education

Bachelor's Degree in Computer Applications...
"""

print("=== ORIGINAL RESUME (AI Generated) ===")
print(test_resume)
print("\n" + "=" * 80 + "\n")

# Apply the rewrite function
rewritten = rewrite_skills_section(user, test_resume)

print("=== REWRITTEN RESUME (With Profile Skills) ===")
print(rewritten)
print("\n" + "=" * 80 + "\n")

# Check if the skills were replaced
if "* Technical Skills:" in rewritten:
    print("✓ SUCCESS: Skills section was rewritten with categorized format!")
else:
    print("✗ FAILED: Skills section was NOT rewritten")
