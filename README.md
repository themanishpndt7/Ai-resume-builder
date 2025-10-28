# 🚀 AI Resume & Portfolio Builder

<div align="center">

![Python Version](https://img.shields.io/badge/python-3.10-blue.svg)
![Django Version](https://img.shields.io/badge/django-4.2.7-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

**A powerful Django-based web application that leverages OpenAI to create professional resumes, cover letters, and portfolios**

[Features](#-features) • [Tech Stack](#️-tech-stack) • [Installation](#-installation) • [Documentation](#-documentation) • [Deployment](#-deployment)

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Tech Stack](#️-tech-stack)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [API Endpoints](#-api-endpoints)
- [Database Models](#-database-models)
- [Deployment](#-deployment)
- [Utilities & Scripts](#-utilities--scripts)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🎯 Overview

The **AI Resume & Portfolio Builder** is a comprehensive web application designed to help job seekers and professionals create stunning, ATS-friendly resumes and cover letters using artificial intelligence. Built with Django and powered by OpenAI's GPT models, this platform offers an intuitive interface for managing professional profiles, education history, work experience, and projects.

### Key Highlights

- **AI-Powered Generation**: Leverage OpenAI GPT models to generate tailored resumes and cover letters
- **Multiple Professional Templates**: 6 unique templates (Modern, Classic, Creative, Minimal, Executive, Technical)
- **PDF Export**: High-quality PDF generation using WeasyPrint
- **User Management**: Complete authentication system with email/username login
- **Secure Password Reset**: OTP-based password reset via email
- **Responsive Design**: Mobile-first, Bootstrap 5-powered interface
- **Dark/Light Theme**: WCAG AA compliant theme toggle
- **Cloud Storage**: Optional Cloudinary integration for media files
- **Production Ready**: Configured for deployment on Render, Heroku, or any WSGI server

---

## ✨ Features

### Core Features

#### 🤖 AI-Powered Resume Generation
- Intelligent resume creation using OpenAI GPT models
- Context-aware content generation based on user profile
- Automatic formatting and optimization for ATS systems
- Multiple resume versions with different templates

#### 📝 Cover Letter Generation
- AI-generated cover letters tailored to specific job positions
- Company and role-specific customization
- Professional tone and formatting
- Template selection for different industries

#### 👤 Profile Management
- Comprehensive user profile with photo upload
- Contact information with international phone code support
- Social links (LinkedIn, GitHub, Portfolio)
- Professional summary and career objectives
- Skills management with advanced parsing

#### 🎓 Education Tracking
- Multiple education entries
- Degree types (High School, Associate, Bachelor's, Master's, Ph.D., Certificate, Diploma)
- Date ranges with "Currently Studying" option
- GPA/Grade tracking
- Detailed descriptions and achievements

#### 💼 Experience Management
- Work history with multiple entries
- Employment types (Full-time, Part-time, Contract, Internship, Freelance, Volunteer)
- Company details and job descriptions
- Date tracking with "Currently Working" support
- Location information

#### 🚀 Project Portfolio
- Project showcase with descriptions
- Technology stack tracking
- Live demo and repository links
- Project thumbnails (with Cloudinary support)
- Date tracking for project timelines

#### 🎨 Professional Templates
1. **Modern**: Clean design with blue accents
2. **Classic**: Traditional, formal serif format
3. **Creative**: Bold, eye-catching layout
4. **Minimal**: Elegant white space design
5. **Executive**: Premium C-level format
6. **Technical**: Structured with skills matrix

#### 📄 PDF Export
- High-quality PDF generation
- Template-specific styling
- Professional typography
- Optimized for printing

#### 🔐 Authentication & Security
- Django Allauth integration
- Email or username login
- Custom OTP-based password reset (6-digit code)
- Session management
- CSRF protection
- Secure password validation

#### 🎨 UI/UX Features
- Light/Dark theme toggle with persistence
- Responsive Bootstrap 5 design
- Select2 integration for searchable dropdowns
- Country and state selection with dynamic loading
- International phone code support
- Real-time form validation
- Toast notifications for user feedback

#### ☁️ Cloud Integration
- Cloudinary support for persistent media storage
- WhiteNoise for static file serving
- Environment-based configuration

---

## 🛠️ Tech Stack

### Backend
- **Framework**: Django 4.2.7
- **Python**: 3.10.0
- **Authentication**: Django Allauth 0.58.2
- **Database**: PostgreSQL (Production) / SQLite (Development)
- **ORM**: Django ORM
- **API**: OpenAI API (GPT models)

### Frontend
- **UI Framework**: Bootstrap 5.3.2
- **Icons**: Bootstrap Icons 1.11.1
- **JavaScript**: Vanilla JS with jQuery
- **CSS**: Custom CSS with theme system
- **Forms**: Crispy Forms with Bootstrap5

### PDF Generation
- **Library**: WeasyPrint 58.1
- **Fonts**: System fonts + custom web fonts
- **Styling**: Template-specific CSS

### Storage & Media
- **Static Files**: WhiteNoise 6.6.0
- **Media Storage**: Cloudinary (optional) / Local filesystem
- **Cloud Storage**: django-cloudinary-storage 0.3.0

### Deployment
- **WSGI Server**: Gunicorn 21.2.0
- **Database Adapter**: psycopg2-binary 2.9.9
- **Configuration**: python-dotenv 1.0.0
- **Database URL**: dj-database-url 3.0.1

### Key Dependencies
```
Django==4.2.7
openai==1.3.5
weasyprint==58.1
django-allauth==0.58.2
django-crispy-forms==2.1
crispy-bootstrap5==2023.10
gunicorn==21.2.0
whitenoise==6.6.0
psycopg2-binary==2.9.9
Pillow==10.1.0
cloudinary==1.44.1
python-dotenv==1.0.0
```

---

## 📁 Project Structure

```
ai-resume-builder/
├── core/                          # Django project configuration
│   ├── __init__.py
│   ├── settings.py               # Main settings file
│   ├── urls.py                   # Root URL configuration
│   ├── wsgi.py                   # WSGI application
│   └── asgi.py                   # ASGI application
│
├── users/                         # User authentication app
│   ├── models.py                 # CustomUser, PasswordResetOTP
│   ├── forms.py                  # CustomSignupForm, UserProfileForm
│   ├── views.py                  # User-related views
│   ├── adapters.py               # Custom Allauth adapter
│   ├── auth_backends.py          # Email/Username authentication
│   ├── admin.py                  # User admin configuration
│   └── migrations/               # Database migrations
│
├── resume/                        # Main resume app
│   ├── models.py                 # Profile, Education, Experience, Project, GeneratedResume, CoverLetter
│   ├── views.py                  # All view functions (756 lines)
│   ├── forms.py                  # All model forms (364 lines)
│   ├── urls.py                   # App URL patterns
│   ├── services.py               # AIResumeGenerator service (783 lines)
│   ├── utils.py                  # PDF generation utilities (982 lines)
│   ├── admin.py                  # Admin configuration
│   ├── admin_config.py           # Detailed admin customization
│   ├── context_processors.py    # Theme context processor
│   ├── countries_data.py         # Countries, states, phone codes data
│   ├── password_reset_views.py  # Custom OTP password reset
│   ├── email_check_view.py      # Email configuration checker
│   ├── diagnostic_views.py      # Production debugging views
│   └── migrations/               # Database migrations
│
├── templates/                     # Django templates
│   ├── base.html                 # Base template with navbar
│   ├── account/                  # Authentication templates
│   │   ├── login.html
│   │   ├── logout.html
│   │   ├── password_reset.html
│   │   ├── password_reset_verify_otp.html
│   │   ├── password_reset_confirm.html
│   │   └── password_reset_complete.html
│   └── resume/                   # Resume app templates
│       ├── home.html             # Landing page
│       ├── dashboard.html        # User dashboard
│       ├── profile_edit.html     # Profile editing
│       ├── education_list.html   # Education management
│       ├── education_form.html
│       ├── experience_list.html  # Experience management
│       ├── experience_form.html
│       ├── project_list.html     # Project management
│       ├── project_form.html
│       ├── generate_resume.html  # Resume generation
│       ├── resume_list.html      # Resume history
│       ├── resume_view.html      # Resume preview
│       ├── generate_cover_letter.html
│       ├── cover_letter_list.html
│       ├── cover_letter_view.html
│       ├── portfolio.html        # Portfolio view
│       └── templates_gallery.html
│
├── static/                        # Static files
│   ├── css/
│   │   ├── style.css            # Main styles (508 lines)
│   │   └── theme.css            # Theme system with dark/light mode
│   ├── js/
│   │   └── theme.js             # Theme toggle functionality (213 lines)
│   └── images/                   # Static images
│
├── staticfiles/                   # Collected static files (production)
│
├── media/                         # User-uploaded files
│   ├── profile_photos/
│   ├── project_thumbnails/
│   └── resumes/
│
├── utilities/                     # Helper scripts
│   ├── create_superuser.py      # Create admin user
│   ├── check_email_config.py    # Email configuration checker
│   ├── check_email_settings.py  # Email settings validator
│   ├── check_env_email.py       # Environment email checker
│   ├── configure_email.py       # Email setup assistant
│   ├── diagnose_email.sh        # Email diagnostics script
│   ├── generate_app_password.py # Gmail app password guide
│   ├── setup_email.sh           # Email setup script
│   ├── test_email_sending.py   # Email sending test
│   ├── test_forgot_password.py # Password reset test
│   ├── test_gmail_credentials.py # Gmail credentials test
│   ├── test_otp_email.py       # OTP email test
│   ├── test_otp_system.py      # OTP system test
│   ├── update_skills.py        # Skills data updater
│   └── generate_project_documentation.py
│
├── deployment/                    # Deployment configuration
│   ├── build.sh                 # Build script for Render
│   ├── render.yaml              # Render configuration
│   ├── Procfile                 # Process file for Heroku/Render
│   ├── runtime.txt              # Python version specification
│   └── restart_server.sh        # Server restart script
│
├── .env                          # Environment variables (not in git)
├── requirements.txt              # Python dependencies
├── manage.py                     # Django management script
├── db.sqlite3                    # SQLite database (development)
└── README.md                     # This file
```

---

## 🚀 Installation

### Prerequisites

- Python 3.10 or higher
- pip (Python package manager)
- virtualenv (recommended)
- Git
- OpenAI API key (for AI features)
- Gmail account with App Password (for email features)

### Step-by-Step Setup

#### 1. Clone the Repository

```bash
git clone https://github.com/themanishpndt7/Ai-resume-builder.git
cd Ai-resume-builder
```

#### 2. Create Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Linux/Mac:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

#### 3. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

#### 4. Environment Configuration

Create a `.env` file in the project root:

```bash
touch .env
```

Add the following configuration:

```env
# Django Settings
SECRET_KEY=your-secret-key-here-generate-a-random-string
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost

# Database (leave blank for SQLite in development)
DATABASE_URL=

# OpenAI API
OPENAI_API_KEY=your-openai-api-key-here

# Email Configuration (Gmail)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password-here
DEFAULT_FROM_EMAIL=your-email@gmail.com
SERVER_EMAIL=your-email@gmail.com

# Cloudinary (Optional - for persistent media storage)
CLOUDINARY_CLOUD_NAME=
CLOUDINARY_API_KEY=
CLOUDINARY_API_SECRET=

# Render (Production)
RENDER_EXTERNAL_HOSTNAME=
```

**Note**: To generate a secure `SECRET_KEY`:
```bash
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

#### 5. Database Setup

```bash
# Run migrations
python manage.py migrate

# Create superuser account
python manage.py createsuperuser
# OR use the utility script:
python create_superuser.py
```

#### 6. Collect Static Files

```bash
python manage.py collectstatic --noinput
```

#### 7. Run Development Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` in your browser.

### 🔑 Getting API Keys

#### OpenAI API Key
1. Go to [OpenAI Platform](https://platform.openai.com/)
2. Sign up or log in
3. Navigate to API Keys section
4. Create a new secret key
5. Copy and add to `.env` file

#### Gmail App Password
1. Enable 2-Factor Authentication on your Google account
2. Go to [Google App Passwords](https://myaccount.google.com/apppasswords)
3. Select "Mail" and your device
4. Generate password
5. Copy the 16-character password (without spaces)
6. Add to `.env` as `EMAIL_HOST_PASSWORD`

#### Cloudinary (Optional)
1. Sign up at [Cloudinary](https://cloudinary.com/)
2. Go to Dashboard
3. Copy Cloud Name, API Key, and API Secret
4. Add to `.env` file

---

## ⚙️ Configuration

### Email Configuration

The application supports two email backends:

1. **SMTP (Production)**: Sends real emails via Gmail or other SMTP servers
2. **Console (Development)**: Prints emails to console for testing

Email backend is automatically selected based on environment variables. If `EMAIL_HOST_USER` and `EMAIL_HOST_PASSWORD` are set, SMTP is used; otherwise, console backend is used.

**Test Email Configuration**:
```bash
python check_email_config.py
python test_email_sending.py
```

### Database Configuration

**Development** (SQLite):
```env
# Leave DATABASE_URL empty
DATABASE_URL=
```

**Production** (PostgreSQL):
```env
DATABASE_URL=postgresql://user:password@host:port/database
```

### Cloudinary Configuration

For persistent media storage (recommended for production):

```env
CLOUDINARY_CLOUD_NAME=your-cloud-name
CLOUDINARY_API_KEY=your-api-key
CLOUDINARY_API_SECRET=your-api-secret
```

### Security Settings

In production (`DEBUG=False`), the following security features are automatically enabled:

- SSL redirect
- Secure cookies
- HSTS headers
- XSS protection
- Content type sniffing protection
- Clickjacking protection

---

## 💡 Usage

### For End Users

#### 1. **Create Account**
- Visit the homepage
- Click "Sign Up"
- Fill in your details (email, password, name)
- Verify email (if enabled)

#### 2. **Build Your Profile**
- Navigate to Dashboard
- Click "Edit Profile"
- Add personal information, skills, and social links
- Upload profile photo

#### 3. **Add Experience**
- Go to "Experience" section
- Click "Add Experience"
- Fill in job details, dates, and responsibilities
- Save entry

#### 4. **Add Education**
- Go to "Education" section
- Add your degrees and certifications
- Include GPA and achievements

#### 5. **Add Projects**
- Go to "Projects" section
- Add portfolio projects
- Include technologies used and project links

#### 6. **Generate Resume**
- Click "Generate Resume"
- Select a template (Modern, Classic, Creative, etc.)
- AI generates tailored content
- Preview and download PDF

#### 7. **Generate Cover Letter**
- Go to "Generate Cover Letter"
- Enter company name and position
- Optionally add job description
- AI generates personalized cover letter
- Download as PDF

### For Developers

#### Custom Template Creation

To add a new resume template:

1. **Add template CSS** in `resume/utils.py`:
```python
def get_template_css(template='modern'):
    # Add your template styles
    if template == 'your_template':
        return '''
        /* Your custom CSS */
        '''
```

2. **Add template instructions** in `resume/services.py`:
```python
template_instructions = {
    'your_template': 'Description of your template style...'
}
```

3. **Update template choices** in `resume/models.py`:
```python
template = models.CharField(
    max_length=50,
    choices=[
        # ... existing choices
        ('your_template', 'Your Template Name'),
    ]
)
```

#### Extending Models

To add new fields to models:

```python
# In resume/models.py
class Profile(models.Model):
    # Add new field
    your_field = models.CharField(max_length=200, blank=True)
```

Then create and run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 🌐 API Endpoints

### Main Routes

| URL Pattern | View | Description |
|------------|------|-------------|
| `/` | `home` | Landing page |
| `/dashboard/` | `dashboard` | User dashboard |
| `/accounts/login/` | Allauth | Login page |
| `/accounts/signup/` | Allauth | Registration page |
| `/accounts/logout/` | Allauth | Logout |

### Profile Management

| URL Pattern | View | Description |
|------------|------|-------------|
| `/profile/edit/` | `profile_edit` | Edit user profile |

### Education

| URL Pattern | View | Description |
|------------|------|-------------|
| `/education/` | `education_list` | List all education entries |
| `/education/add/` | `education_add` | Add new education |
| `/education/<id>/edit/` | `education_edit` | Edit education entry |
| `/education/<id>/delete/` | `education_delete` | Delete education entry |

### Experience

| URL Pattern | View | Description |
|------------|------|-------------|
| `/experience/` | `experience_list` | List all experiences |
| `/experience/add/` | `experience_add` | Add new experience |
| `/experience/<id>/edit/` | `experience_edit` | Edit experience |
| `/experience/<id>/delete/` | `experience_delete` | Delete experience |

### Projects

| URL Pattern | View | Description |
|------------|------|-------------|
| `/projects/` | `project_list` | List all projects |
| `/projects/add/` | `project_add` | Add new project |
| `/projects/<id>/edit/` | `project_edit` | Edit project |
| `/projects/<id>/delete/` | `project_delete` | Delete project |

### Resume Generation

| URL Pattern | View | Description |
|------------|------|-------------|
| `/generate/` | `generate_resume` | AI resume generation |
| `/resumes/` | `resume_list` | List generated resumes |
| `/resumes/<id>/` | `resume_view` | View resume |
| `/resumes/<id>/download/` | `resume_download_pdf` | Download as PDF |
| `/resumes/<id>/delete/` | `resume_delete` | Delete resume |
| `/templates/` | `templates_gallery` | Template gallery |

### Cover Letters

| URL Pattern | View | Description |
|------------|------|-------------|
| `/cover-letters/generate/` | `generate_cover_letter` | Generate cover letter |
| `/cover-letters/` | `cover_letter_list` | List cover letters |
| `/cover-letters/<id>/` | `cover_letter_view` | View cover letter |
| `/cover-letters/<id>/download/` | `cover_letter_download_pdf` | Download PDF |
| `/cover-letters/<id>/delete/` | `cover_letter_delete` | Delete cover letter |

### Portfolio

| URL Pattern | View | Description |
|------------|------|-------------|
| `/portfolio/` | `portfolio_view` | View portfolio |
| `/portfolio/download/` | `portfolio_download_pdf` | Download portfolio PDF |

### Password Reset (Custom OTP)

| URL Pattern | View | Description |
|------------|------|-------------|
| `/accounts/password/reset/` | `PasswordResetRequestView` | Request OTP |
| `/accounts/password/reset/verify/` | `PasswordResetVerifyOTPView` | Verify OTP |
| `/accounts/password/reset/confirm/` | `PasswordResetConfirmView` | Set new password |
| `/accounts/password/reset/complete/` | `PasswordResetCompleteView` | Completion page |

### Diagnostic Endpoints

| URL Pattern | View | Description |
|------------|------|-------------|
| `/api/config-check/` | `config_check` | Check configuration |
| `/api/test-email/` | `test_email_quick` | Test email sending |
| `/check-email-config/` | `check_email_config` | Email config details |

### Theme

| URL Pattern | View | Description |
|------------|------|-------------|
| `/set-theme/` | `set_theme` | Toggle dark/light theme |

---

## 🗄️ Database Models

### User App Models

#### **CustomUser**
Extends Django's AbstractUser with additional fields.

```python
Fields:
- email (EmailField, unique) - Primary authentication field
- username (CharField) - Also supported for login
- first_name (CharField)
- last_name (CharField)
- phone (CharField, optional)
- profile_photo (ImageField, optional)
- created_at (DateTimeField, auto)
- updated_at (DateTimeField, auto)
```

#### **PasswordResetOTP**
Stores OTP codes for password reset.

```python
Fields:
- user (ForeignKey to CustomUser)
- otp (CharField, 6 digits)
- created_at (DateTimeField, auto)
- is_used (BooleanField)

Methods:
- is_valid() - Check if OTP is valid (not expired/used)
- generate_otp() - Generate random 6-digit OTP
```

### Resume App Models

#### **Profile**
One-to-one relationship with User. Stores professional information.

```python
Fields:
- user (OneToOneField)
- career_objective (TextField)
- summary (TextField)
- skills (TextField) - Comma-separated
- linkedin_url (URLField)
- github_url (URLField)
- portfolio_url (URLField)
- location (CharField)
- created_at (DateTimeField)
- updated_at (DateTimeField)

Methods:
- get_skills_list() - Parse skills into list
```

#### **Education**
Multiple education entries per user.

```python
Fields:
- user (ForeignKey)
- institution (CharField)
- degree (CharField) - Choices: high_school, associate, bachelor, master, phd, certificate, diploma, other
- field_of_study (CharField)
- start_date (DateField)
- end_date (DateField, optional)
- currently_studying (BooleanField)
- grade (CharField, optional)
- description (TextField, optional)
- created_at (DateTimeField)
- updated_at (DateTimeField)
```

#### **Experience**
Work experience entries.

```python
Fields:
- user (ForeignKey)
- company (CharField)
- position (CharField)
- employment_type (CharField) - Choices: full_time, part_time, contract, internship, freelance, volunteer
- location (CharField, optional)
- start_date (DateField)
- end_date (DateField, optional)
- currently_working (BooleanField)
- description (TextField)
- created_at (DateTimeField)
- updated_at (DateTimeField)
```

#### **Project**
Portfolio projects.

```python
Fields:
- user (ForeignKey)
- title (CharField)
- description (TextField)
- technologies (CharField) - Comma-separated
- project_url (URLField, optional)
- thumbnail (ImageField, optional)
- start_date (DateField)
- end_date (DateField, optional)
- currently_working (BooleanField)
- created_at (DateTimeField)
- updated_at (DateTimeField)

Methods:
- get_technologies_list() - Parse technologies into list
```

#### **GeneratedResume**
Stores AI-generated resumes.

```python
Fields:
- user (ForeignKey)
- title (CharField)
- content (TextField) - HTML content
- template (CharField) - Template used
- created_at (DateTimeField)
```

#### **CoverLetter**
Stores AI-generated cover letters.

```python
Fields:
- user (ForeignKey)
- title (CharField)
- company_name (CharField)
- position (CharField)
- job_description (TextField, optional)
- content (TextField) - HTML content
- template (CharField) - Choices: modern, classic, creative, minimal, executive, technical
- created_at (DateTimeField)
```

### Database Relationships

```
CustomUser (1) ──────┬───── (1) Profile
                     │
                     ├───── (*) Education
                     │
                     ├───── (*) Experience
                     │
                     ├───── (*) Project
                     │
                     ├───── (*) GeneratedResume
                     │
                     ├───── (*) CoverLetter
                     │
                     └───── (*) PasswordResetOTP
```

---

## 🚢 Deployment

### Deployment to Render

#### Prerequisites
- GitHub account with your repository
- Render account (free tier available)
- PostgreSQL database
- Environment variables configured

#### Quick Deploy Steps

1. **Push Code to GitHub**
```bash
git add .
git commit -m "Prepare for deployment"
git push origin main
```

2. **Create PostgreSQL Database on Render**
   - Log in to Render Dashboard
   - Click "New +" → "PostgreSQL"
   - Name: `ai-resume-builder-db`
   - Choose free tier
   - Click "Create Database"
   - Copy the "Internal Database URL"

3. **Create Web Service**
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Select `Ai-resume-builder` repository
   - Configure:
     - **Name**: `ai-resume-builder`
     - **Runtime**: Python 3
     - **Build Command**: `./build.sh`
     - **Start Command**: `gunicorn core.wsgi:application`

4. **Set Environment Variables**

In Render dashboard, add these environment variables:

```env
PYTHON_VERSION=3.10.0
SECRET_KEY=<generate-random-secret-key>
DEBUG=False
ALLOWED_HOSTS=your-app-name.onrender.com
DATABASE_URL=<paste-database-url-from-step-2>
OPENAI_API_KEY=<your-openai-api-key>
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=<your-gmail>
EMAIL_HOST_PASSWORD=<your-app-password>
DEFAULT_FROM_EMAIL=<your-gmail>
CLOUDINARY_CLOUD_NAME=<optional>
CLOUDINARY_API_KEY=<optional>
CLOUDINARY_API_SECRET=<optional>
```

5. **Deploy**
   - Click "Create Web Service"
   - Render will automatically build and deploy
   - Wait for deployment to complete
   - Visit your app at `https://your-app-name.onrender.com`

6. **Create Superuser** (after deployment)

Use Render Shell:
```bash
python create_superuser.py
```

#### Using render.yaml

Alternatively, use the included `render.yaml` for automatic setup:

```yaml
databases:
  - name: ai_resume_builder_db
    databaseName: ai_resume_builder_db
    user: ai_resume_builder_user

services:
  - type: web
    name: ai-resume-builder
    runtime: python
    buildCommand: "./build.sh"
    startCommand: "gunicorn core.wsgi:application"
    envVars:
      - key: PYTHON_VERSION
        value: 3.10.0
      - key: DATABASE_URL
        fromDatabase:
          name: ai_resume_builder_db
          property: connectionString
      - key: SECRET_KEY
        generateValue: true
      - key: DEBUG
        value: False
```

### Deployment to Heroku

#### 1. Install Heroku CLI
```bash
# Install Heroku CLI
curl https://cli-assets.heroku.com/install.sh | sh

# Login
heroku login
```

#### 2. Create Heroku App
```bash
heroku create ai-resume-builder-app

# Add PostgreSQL addon
heroku addons:create heroku-postgresql:mini
```

#### 3. Set Environment Variables
```bash
heroku config:set SECRET_KEY=<your-secret-key>
heroku config:set DEBUG=False
heroku config:set OPENAI_API_KEY=<your-key>
heroku config:set EMAIL_HOST_USER=<your-email>
heroku config:set EMAIL_HOST_PASSWORD=<your-password>
# Add other variables...
```

#### 4. Deploy
```bash
git push heroku main

# Run migrations
heroku run python manage.py migrate

# Create superuser
heroku run python create_superuser.py
```

### Production Checklist

- [ ] `DEBUG=False` in production
- [ ] Unique `SECRET_KEY` generated
- [ ] PostgreSQL database configured
- [ ] All environment variables set
- [ ] Static files collected
- [ ] HTTPS enabled
- [ ] Secure cookies enabled
- [ ] ALLOWED_HOSTS configured
- [ ] Database backups enabled
- [ ] Error logging configured
- [ ] Cloudinary configured (for persistent media)
- [ ] Email service working
- [ ] OpenAI API key valid and funded

---

## 🔧 Utilities & Scripts

### Email Configuration Scripts

#### `check_email_config.py`
Verify email configuration settings.
```bash
python check_email_config.py
```

#### `test_email_sending.py`
Test email sending functionality.
```bash
python test_email_sending.py
```

#### `configure_email.py`
Interactive email setup assistant.
```bash
python configure_email.py
```

#### `test_otp_system.py`
Test OTP generation and validation.
```bash
python test_otp_system.py
```

### Database Scripts

#### `create_superuser.py`
Automated superuser creation.
```bash
python create_superuser.py
```

#### `update_skills.py`
Update skills data for existing profiles.
```bash
python update_skills.py
```

### Deployment Scripts

#### `build.sh`
Build script for production deployment.
```bash
chmod +x build.sh
./build.sh
```

#### `restart_server.sh`
Restart the application server.
```bash
chmod +x restart_server.sh
./restart_server.sh
```

### Documentation

#### `generate_project_documentation.py`
Generate comprehensive project documentation.
```bash
python generate_project_documentation.py
```

---

## 🧪 Testing

### Run Tests

```bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test users
python manage.py test resume

# Run with verbose output
python manage.py test --verbosity=2

# Run specific test case
python manage.py test resume.tests.TestResumeGeneration
```

### Manual Testing

#### Test Email System
```bash
python test_email_sending.py
python test_otp_email.py
```

#### Test Password Reset
```bash
python test_forgot_password.py
```

#### Test Gmail Credentials
```bash
python test_gmail_credentials.py
```

---

## 🤝 Contributing

Contributions are welcome! Please follow these guidelines:

### Getting Started

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Code Style

- Follow PEP 8 for Python code
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Comment complex logic
- Keep functions small and focused

### Commit Messages

- Use present tense ("Add feature" not "Added feature")
- Use imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit first line to 72 characters
- Reference issues and pull requests

### Pull Request Process

1. Update README.md with details of changes if needed
2. Update requirements.txt if you add dependencies
3. Run tests and ensure they pass
4. Update documentation
5. Request review from maintainers

---

## 📝 License

This project is licensed under the MIT License - see below for details:

```
MIT License

Copyright (c) 2024 Manish Sharma

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 👤 Author

**Manish Sharma**
- GitHub: [@themanishpndt7](https://github.com/themanishpndt7)
- Email: mpandat0052@gmail.com

---

## 🙏 Acknowledgments

- [Django](https://www.djangoproject.com/) - Web framework
- [OpenAI](https://openai.com/) - AI API for content generation
- [Bootstrap](https://getbootstrap.com/) - Frontend framework
- [WeasyPrint](https://weasyprint.org/) - PDF generation
- [Django Allauth](https://django-allauth.readthedocs.io/) - Authentication
- [Cloudinary](https://cloudinary.com/) - Media storage
- [Render](https://render.com/) - Hosting platform

---

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/themanishpndt7/Ai-resume-builder/issues) page
2. Create a new issue with detailed information
3. Contact: mpandat0052@gmail.com

---

## 🔮 Roadmap

Future enhancements planned:

- [ ] LinkedIn profile import
- [ ] Resume parsing from PDF/DOCX
- [ ] Multiple language support
- [ ] Resume analytics and suggestions
- [ ] Job board integration
- [ ] Resume scoring system
- [ ] Interview preparation features
- [ ] Video resume support
- [ ] Resume templates marketplace
- [ ] Mobile app (React Native)

---

## ⭐ Star History

If you find this project useful, please consider giving it a star!

---

<div align="center">

**Made with ❤️ by Manish Sharma**

[⬆ Back to Top](#-ai-resume--portfolio-builder)

</div>

3. **Configure Service**
   - **Name:** ai-resume-builder
   - **Runtime:** Python 3
   - **Build Command:** `./build.sh`
   - **Start Command:** `gunicorn core.wsgi:application`

4. **Add Environment Variables**
   Click "Advanced" and add:
   - `SECRET_KEY`: (Generate a secure key)
   - `DEBUG`: `False`
   - `OPENAI_API_KEY`: Your OpenAI API key
   - `EMAIL_HOST_USER`: Your Gmail
   - `EMAIL_HOST_PASSWORD`: Your Gmail App Password
   - `ALLOWED_HOSTS`: `your-app-name.onrender.com`

5. **Create PostgreSQL Database**
   - Go to Dashboard → New → PostgreSQL
   - Name: `ai-resume-builder-db`
   - Copy the "Internal Database URL"
   - Add to Web Service as `DATABASE_URL`

6. **Deploy**
   - Click "Create Web Service"
   - Wait for build to complete (~5-10 minutes)
   - Your app will be live at: `https://your-app-name.onrender.com`

### Alternative: Deploy to Railway

1. Visit [railway.app](https://railway.app)
2. Click "Deploy from GitHub repo"
3. Select your repository
4. Add environment variables
5. Click Deploy

### Alternative: Deploy to PythonAnywhere

1. Visit [pythonanywhere.com](https://www.pythonanywhere.com)
2. Create free account
3. Upload your code
4. Configure WSGI file
5. Set up database and static files

## Environment Variables 🔐

Required environment variables for production:

```env
SECRET_KEY=your-django-secret-key
DEBUG=False
ALLOWED_HOSTS=your-domain.com
DATABASE_URL=postgresql://user:password@host:5432/dbname
OPENAI_API_KEY=sk-your-openai-key
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-gmail-app-password
```

## Project Structure 📁

```
ai-resume-builder/
├── core/                 # Project settings
├── resume/              # Resume app
├── users/               # User authentication
├── templates/           # HTML templates
├── static/              # CSS, JS, images
├── media/               # User uploads
├── requirements.txt     # Dependencies
├── manage.py           # Django management
├── build.sh            # Build script
├── render.yaml         # Render config
└── README.md           # This file
```

## Contributing 🤝

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License 📄

This project is licensed under the MIT License.

## Support 💬

For support, email themanishpndt7@gmail.com or create an issue in this repository.

## Acknowledgments 🙏

- OpenAI for the AI API
- Django community
- Bootstrap team
- All contributors

---

Made with ❤️ by [themanishpndt7](https://github.com/themanishpndt7)
