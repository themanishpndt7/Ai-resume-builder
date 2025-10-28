# Render Deployment Checklist - AI Resume Builder

## Pre-Deployment (5 minutes)

### 1. Verify Local Changes
```bash
# Ensure all migrations are created
python manage.py makemigrations
python manage.py migrate

# Test locally
python manage.py runserver
# Visit http://localhost:8000/accounts/login/
# Test login, signup, password reset
```

### 2. Commit and Push Changes
```bash
git add .
git commit -m "Fix authentication: login, signup, OTP password reset"
git push origin main
```

---

## Render Dashboard Setup (10 minutes)

### 1. Environment Variables

**Navigate to:** Render Dashboard → Your Service → Environment

**Add these variables:**

#### Required - Security
```
SECRET_KEY=<generate-new-secret-key>
DEBUG=False
ALLOWED_HOSTS=<your-app-name>.onrender.com
RENDER_EXTERNAL_HOSTNAME=<your-app-name>.onrender.com
```

#### Required - Database
```
DATABASE_URL=<automatically-set-by-render-postgres>
```

#### Required - Email (for OTP)
```
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your.email@gmail.com
EMAIL_HOST_PASSWORD=<16-char-app-password>
DEFAULT_FROM_EMAIL=your.email@gmail.com
```

#### Optional - Media Storage
```
CLOUDINARY_CLOUD_NAME=<your-cloudinary-name>
CLOUDINARY_API_KEY=<your-api-key>
CLOUDINARY_API_SECRET=<your-api-secret>
```

#### Optional - AI Features
```
OPENAI_API_KEY=<your-openai-key>
```

### 2. Build Command
```bash
./build.sh
```

**Or if build.sh doesn't exist:**
```bash
pip install -r requirements.txt && python manage.py collectstatic --no-input && python manage.py migrate
```

### 3. Start Command
```bash
gunicorn core.wsgi:application
```

---

## Gmail App Password Setup (5 minutes)

### Option 1: Gmail with App Password (Recommended for Testing)

1. **Enable 2-Factor Authentication:**
   - Go to https://myaccount.google.com/security
   - Enable 2-Step Verification

2. **Generate App Password:**
   - Visit https://myaccount.google.com/apppasswords
   - Select "Mail" and "Other (Custom name)"
   - Name it "AI Resume Builder"
   - Copy the 16-character password (no spaces)

3. **Set on Render:**
   ```
   EMAIL_HOST_USER=your.email@gmail.com
   EMAIL_HOST_PASSWORD=abcd efgh ijkl mnop  (remove spaces: abcdefghijklmnop)
   ```

### Option 2: SendGrid (Recommended for Production)

1. **Sign up:** https://sendgrid.com (Free tier: 100 emails/day)

2. **Create API Key:**
   - Settings → API Keys → Create API Key
   - Full Access → Create & View

3. **Set on Render:**
   ```
   EMAIL_HOST=smtp.sendgrid.net
   EMAIL_PORT=587
   EMAIL_USE_TLS=True
   EMAIL_HOST_USER=apikey
   EMAIL_HOST_PASSWORD=<your-sendgrid-api-key>
   DEFAULT_FROM_EMAIL=noreply@yourdomain.com
   ```

---

## Deployment Steps (5 minutes)

### 1. Trigger Deployment
- **Automatic:** Push to main branch (if auto-deploy enabled)
- **Manual:** Render Dashboard → Manual Deploy → Deploy latest commit

### 2. Monitor Build Logs
Watch for:
```
✅ Installing dependencies...
✅ Collecting static files...
✅ Running migrations...
✅ Build succeeded
```

### 3. Check Application Logs
Look for:
```
✅ Email configured: Real emails will be sent via SMTP
✅ Cloudinary configured (if using)
⚠️  Email not configured (if EMAIL_HOST_USER not set)
```

---

## Post-Deployment Testing (10 minutes)

### Test 1: Login Flow
```
1. Visit https://<your-app>.onrender.com/accounts/login/
2. Enter credentials
3. Check "Remember me"
4. Submit → Should redirect to dashboard
5. Close browser, reopen → Should still be logged in ✅
```

### Test 2: Signup Flow
```
1. Visit /accounts/signup/
2. Verify no error messages on page load ✅
3. Fill form with valid data
4. Submit → Should create user ✅
5. Check database (Render PostgreSQL dashboard)
6. Try duplicate email → Should show error ✅
```

### Test 3: Password Reset Flow
```
1. Visit /accounts/password/reset/
2. Enter registered email
3. Submit → Should see "OTP sent" message ✅
4. Check email inbox (and spam folder) ✅
5. Enter OTP → Should redirect to set password ✅
6. Set new password → Should show success ✅
7. Login with new password → Should work ✅
```

### Test 4: Rate Limiting
```
1. Request OTP
2. Immediately request again → Should block (2-min cooldown) ✅
3. Enter wrong OTP 5 times → Should require new OTP ✅
```

---

## Troubleshooting

### Issue: "Email backend is set to console"
**Fix:** Set EMAIL_HOST_USER and EMAIL_HOST_PASSWORD in Render environment

### Issue: "CSRF verification failed"
**Fix:** Ensure RENDER_EXTERNAL_HOSTNAME is set correctly

### Issue: "500 Internal Server Error"
**Check:**
1. Render logs for error details
2. DATABASE_URL is set
3. Migrations ran successfully
4. SECRET_KEY is set

### Issue: "OTP email not received"
**Check:**
1. Spam folder
2. Email credentials are correct
3. Gmail app password (not regular password)
4. Render logs for email sending errors

### Issue: "User not saved to database"
**Check:**
1. Migrations completed: `python manage.py showmigrations`
2. DATABASE_URL is correct
3. PostgreSQL instance is running

---

## Quick Commands

### View Logs
```bash
# Via Render Dashboard → Logs tab
# Or via Render CLI:
render logs -s <service-name>
```

### Run Migrations
```bash
# Via Render Dashboard → Shell:
python manage.py migrate
```

### Create Superuser
```bash
# Via Render Dashboard → Shell:
python manage.py createsuperuser
```

### Check Email Config
```bash
# Via Render Dashboard → Shell:
python manage.py shell
>>> from django.conf import settings
>>> print(settings.EMAIL_BACKEND)
>>> print(settings.EMAIL_HOST_USER)
```

---

## Success Criteria

- ✅ Application loads without errors
- ✅ Login works with and without "Remember me"
- ✅ Signup creates users in database
- ✅ No premature validation warnings
- ✅ OTP emails sent and received
- ✅ Password reset flow completes successfully
- ✅ Rate limiting prevents abuse
- ✅ No 500 errors in logs

---

## Rollback Plan

If deployment fails:

1. **Via Render Dashboard:**
   - Go to Events tab
   - Find last successful deployment
   - Click "Rollback to this deploy"

2. **Via Git:**
   ```bash
   git revert HEAD
   git push origin main
   ```

---

## Monitoring

### Key Metrics to Watch
- Response times (should be < 500ms)
- Error rates (should be < 1%)
- Email delivery rates (check SendGrid dashboard)
- Failed login attempts (check logs)

### Set Up Alerts
- Render Dashboard → Notifications
- Configure alerts for:
  - Deployment failures
  - High error rates
  - Service downtime

---

## Next Steps After Deployment

1. **Test all features thoroughly**
2. **Create test user accounts**
3. **Verify email delivery**
4. **Monitor logs for 24 hours**
5. **Set up custom domain (optional)**
6. **Configure SSL certificate (automatic on Render)**

---

## Support

**Render Documentation:** https://render.com/docs  
**Django Documentation:** https://docs.djangoproject.com/  
**Project Issues:** Check AUTHENTICATION_FIX_REPORT.md

---

**Estimated Total Time:** 30-35 minutes  
**Difficulty:** Medium  
**Prerequisites:** Render account, GitHub repository, Email provider

✅ **You're ready to deploy!**
