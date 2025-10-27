# 🚀 Deployment Guide - Get Your Live Link!

## Option 1: Render (Recommended - FREE) ⭐

### Step-by-Step Instructions:

1. **Sign Up for Render**
   - Go to: https://render.com
   - Click "Get Started for Free"
   - Sign up with your GitHub account

2. **Create Web Service**
   - Click "New +" button (top right)
   - Select "Web Service"
   - Click "Connect account" for GitHub
   - Find and select: `themanishpndt7/Ai-resume-builder`
   - Click "Connect"

3. **Configure Your Service**
   Fill in these details:
   - **Name:** `ai-resume-builder` (or any name you like)
   - **Region:** Choose closest to you
   - **Branch:** `main`
   - **Runtime:** Python 3
   - **Build Command:** `./build.sh`
   - **Start Command:** `gunicorn core.wsgi:application`
   - **Instance Type:** Free

4. **Add Environment Variables**
   Click "Advanced" → "Add Environment Variable"
   
   Add these one by one:
   
   ```
   SECRET_KEY = django-insecure-CHANGE-THIS-TO-RANDOM-STRING
   DEBUG = False
   OPENAI_API_KEY = your-openai-api-key-here
   EMAIL_HOST_USER = your-email@gmail.com
   EMAIL_HOST_PASSWORD = your-gmail-app-password
   ```

5. **Create PostgreSQL Database**
   - In Render Dashboard, click "New +" → "PostgreSQL"
   - Name: `ai-resume-builder-db`
   - Choose Free plan
   - Click "Create Database"
   - Copy the "Internal Database URL"
   - Go back to your Web Service
   - Add new environment variable:
     ```
     DATABASE_URL = [paste the internal database URL]
     ```

6. **Update ALLOWED_HOSTS**
   - After your service is created, you'll get a URL like:
     `https://ai-resume-builder-xxxx.onrender.com`
   - Add environment variable:
     ```
     ALLOWED_HOSTS = ai-resume-builder-xxxx.onrender.com
     ```

7. **Deploy!**
   - Click "Create Web Service"
   - Wait 5-10 minutes for first deployment
   - Your app will be live! 🎉

8. **Your Live Link:**
   ```
   https://ai-resume-builder-xxxx.onrender.com
   ```

### Important Notes for Render:
- ✅ Free tier includes 750 hours/month
- ⚠️ App sleeps after 15 minutes of inactivity
- ⏱️ First request after sleep takes ~30 seconds
- 💾 Free PostgreSQL: 1GB storage

---

## Option 2: Railway (Alternative - FREE) 🚂

1. **Sign Up**
   - Go to: https://railway.app
   - Sign up with GitHub

2. **Deploy**
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose: `themanishpndt7/Ai-resume-builder`
   - Railway auto-detects Django and sets up PostgreSQL!

3. **Add Environment Variables**
   - Click on your service
   - Go to "Variables" tab
   - Add same variables as Render

4. **Get Your Link**
   - Go to "Settings" → "Generate Domain"
   - Your live link: `https://your-app.up.railway.app`

### Important Notes for Railway:
- ✅ $5 free credit per month
- ✅ No sleep/cold starts
- ✅ Automatic PostgreSQL setup

---

## Option 3: PythonAnywhere (Alternative) 🐍

1. **Sign Up**
   - Go to: https://www.pythonanywhere.com
   - Create free account

2. **Upload Code**
   - Open Bash console
   - Clone your repo:
     ```bash
     git clone https://github.com/themanishpndt7/Ai-resume-builder.git
     ```

3. **Set Up Virtual Environment**
   ```bash
   cd Ai-resume-builder
   mkvirtualenv --python=/usr/bin/python3.10 myenv
   pip install -r requirements.txt
   ```

4. **Configure Web App**
   - Go to "Web" tab
   - Click "Add a new web app"
   - Choose "Manual configuration"
   - Python 3.10
   - Set WSGI file path

5. **Your Link**
   ```
   https://yourusername.pythonanywhere.com
   ```

---

## Option 4: Heroku (Paid but Reliable) 💳

1. **Sign Up**
   - Go to: https://heroku.com
   - Note: No longer has free tier (~$5/month minimum)

2. **Install Heroku CLI**
   ```bash
   curl https://cli-assets.heroku.com/install.sh | sh
   ```

3. **Deploy**
   ```bash
   heroku login
   heroku create ai-resume-builder
   git push heroku main
   heroku run python manage.py migrate
   ```

4. **Your Link**
   ```
   https://ai-resume-builder.herokuapp.com
   ```

---

## Getting Your OpenAI API Key 🔑

1. Go to: https://platform.openai.com
2. Sign up/Login
3. Click your profile → "View API Keys"
4. Click "Create new secret key"
5. Copy and save it (you won't see it again!)

---

## Getting Gmail App Password 📧

1. Go to Google Account Settings
2. Security → 2-Step Verification (enable it)
3. App Passwords → Generate
4. Select "Mail" and "Other"
5. Copy the 16-character password
6. Use this in EMAIL_HOST_PASSWORD

---

## Troubleshooting 🔧

### Build Failed?
- Check build logs in Render dashboard
- Make sure all environment variables are set
- Verify DATABASE_URL is correct

### App not loading?
- Check if ALLOWED_HOSTS includes your domain
- Verify DEBUG=False for production
- Check application logs

### Database errors?
- Make sure migrations ran: `python manage.py migrate`
- Check DATABASE_URL is correct
- Ensure PostgreSQL database is created

---

## After Deployment Checklist ✅

- [ ] App loads successfully
- [ ] Can register new user
- [ ] Can login
- [ ] Can create resume
- [ ] Can generate PDF
- [ ] Email functionality works
- [ ] OpenAI integration works

---

## Need Help? 💬

If you encounter any issues:
1. Check the deployment logs
2. Verify all environment variables
3. Check the GitHub issues
4. Contact: themanishpndt7@gmail.com

---

**Recommended for beginners:** Start with **Render** - it's free, easy, and has good documentation!

Good luck with your deployment! 🚀
