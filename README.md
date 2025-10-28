# AI Resume Builder 🚀

A powerful Django-based web application that helps users create professional resumes and cover letters using AI technology.

## Features ✨

- 🤖 AI-powered resume and cover letter generation
- 📝 Multiple professional templates
- 👤 User authentication and profile management
- 📄 PDF export functionality
- 🎨 Modern, responsive UI
- 🔐 Secure password reset with OTP
- 📊 Dashboard for managing resumes and projects

## Tech Stack 🛠️

- **Backend:** Django 4.2.7
- **Frontend:** HTML, CSS, JavaScript, Bootstrap 5
- **Database:** PostgreSQL (Production) / SQLite (Development)
- **AI:** OpenAI API
- **PDF Generation:** WeasyPrint
- **Authentication:** Django Allauth
- **Deployment:** Gunicorn + WhiteNoise

## Live Demo 🌐

[Your Live Demo Link Here]

## Local Development Setup 💻

### Prerequisites

- Python 3.10+
- pip
- virtualenv

### Installation Steps

1. **Clone the repository**
```bash
git clone https://github.com/themanishpndt7/Ai-resume-builder.git
cd Ai-resume-builder
```

2. **Create and activate virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Create .env file**
```bash
cp .env.example .env
```

Edit `.env` and add your configuration:
```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
OPENAI_API_KEY=your-openai-api-key
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

5. **Run migrations**
```bash
python manage.py migrate
```

6. **Create superuser**
```bash
python manage.py createsuperuser
```

7. **Run development server**
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` in your browser.

## Deployment to Render 🚀

### Quick Deploy

1. **Sign up for Render**
   - Go to [render.com](https://render.com)
   - Sign up with your GitHub account

2. **Create New Web Service**
   - Click "New +" → "Web Service"
   - Connect your GitHub repository: `themanishpndt7/Ai-resume-builder`
   - Click "Connect"

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
