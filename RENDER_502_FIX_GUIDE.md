# 502 Error Fix Guide - AI Resume Builder

## 🚨 Current Issues

1. **502 Bad Gateway** on `/accounts/signup/`, `/accounts/password/reset/`
2. **Login fails** for registered users
3. **OTP emails not sent**
4. **Database not updating** (users not saved)
5. **Premature validation warnings** on signup

---

## 🔍 Root Cause Analysis

### 502 Errors = Application Crash
- Gunicorn worker crashes when Django raises uncaught exceptions
- Common causes:
  - Database connection timeout
  - Email SMTP timeout (blocking operation)
  - Missing environment variables causing AttributeError
  - Unhandled exceptions in views

### Database Issues
- Migrations not applied on Render PostgreSQL
- DATABASE_URL not set or incorrect
- App connecting to local SQLite instead of PostgreSQL

### Email Issues
- EMAIL_HOST_USER/EMAIL_HOST_PASSWORD not set
- Gmail blocking connection (need App Password)
- SMTP timeout causing worker to hang

---

## ✅ Immediate Fixes Applied

The code already has these fixes from the previous session:
- ✅ Custom login view with error handling
- ✅ Custom signup view with atomic transactions
- ✅ Rate limiting on OTP requests
- ✅ Comprehensive logging

---

## 🔧 Critical Render Configuration

### Step 1: Environment Variables (MUST SET)

Go to **Render Dashboard → Your Service → Environment**

```bash
# CRITICAL - Security
SECRET_KEY=<generate-new-50-char-random-string>
DEBUG=False

# CRITICAL - Hosting
ALLOWED_HOSTS=ai-resume-builder-6jan.onrender.com
RENDER_EXTERNAL_HOSTNAME=ai-resume-builder-6jan.onrender.com

# CRITICAL - Database (auto-set by Render, verify it exists)
DATABASE_URL=postgresql://user:pass@host/dbname

# CRITICAL - Email (for OTP)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your.email@gmail.com
EMAIL_HOST_PASSWORD=<16-char-app-password>
DEFAULT_FROM_EMAIL=your.email@gmail.com
```

### Step 2: Gmail App Password Setup

**IMPORTANT:** You CANNOT use your regular Gmail password!

1. **Enable 2-Factor Authentication:**
   - Visit: https://myaccount.google.com/security
   - Turn on 2-Step Verification

2. **Generate App Password:**
   - Visit: https://myaccount.google.com/apppasswords
   - Select "Mail" and "Other (Custom name)"
   - Name it: "AI Resume Builder Render"
   - **Copy the 16-character password** (e.g., `abcd efgh ijkl mnop`)
   - **Remove spaces:** `abcdefghijklmnop`

3. **Set on Render:**
   ```
   EMAIL_HOST_USER=your.email@gmail.com
   EMAIL_HOST_PASSWORD=abcdefghijklmnop
   ```

### Step 3: Database Migrations

**Via Render Shell:**

```bash
# Open Render Dashboard → Shell (or use SSH)
python manage.py showmigrations
python manage.py migrate
python manage.py createsuperuser  # Create admin user
```

**Check if migrations applied:**
```bash
python manage.py dbshell
\dt  # List all tables
SELECT * FROM users_customuser LIMIT 5;  # Check users
\q  # Exit
```

---

## 🐛 Debugging 502 Errors

### Check Render Logs

**Render Dashboard → Logs → Filter by "Error"**

Look for these patterns:

#### Pattern 1: Database Connection Error
```
django.db.utils.OperationalError: could not connect to server
```
**Fix:** Verify DATABASE_URL is set and PostgreSQL instance is running

#### Pattern 2: Email Timeout
```
SMTPServerDisconnected: Connection unexpectedly closed
TimeoutError: [Errno 110] Connection timed out
```
**Fix:** Set EMAIL_HOST_USER and EMAIL_HOST_PASSWORD correctly

#### Pattern 3: Missing Environment Variable
```
AttributeError: 'NoneType' object has no attribute 'split'
KeyError: 'SOME_VARIABLE'
```
**Fix:** Add missing environment variable on Render

#### Pattern 4: Migration Error
```
django.db.utils.ProgrammingError: relation "users_customuser" does not exist
```
**Fix:** Run `python manage.py migrate` on Render

---

## 🧪 Testing Procedure

### Test 1: Health Check
```bash
# Visit your app URL
https://ai-resume-builder-6jan.onrender.com/

# Should load without 502
# Check Render logs for startup messages
```

### Test 2: Signup
```bash
1. Visit /accounts/signup/
2. Should load cleanly (no red warnings)
3. Fill form with valid data:
   - First Name: Test
   - Last Name: User
   - Email: testuser@example.com
   - Password: TestPass123!
   - Confirm Password: TestPass123!
4. Submit → Should redirect to login
5. Check Render logs for: "User successfully created: testuser@example.com"
```

### Test 3: Database Verification
```bash
# Via Render Shell
python manage.py shell

from users.models import CustomUser
users = CustomUser.objects.all()
print(f"Total users: {users.count()}")
for user in users:
    print(f"- {user.email} (ID: {user.id})")
```

### Test 4: Login
```bash
1. Visit /accounts/login/
2. Enter credentials from signup
3. Check "Remember me"
4. Submit → Should redirect to dashboard
5. Check Render logs for: "Session set to persist for 2 weeks"
```

### Test 5: Password Reset
```bash
1. Visit /accounts/password/reset/
2. Enter registered email
3. Submit → Should see "OTP sent" message
4. Check email inbox (and spam folder)
5. Check Render logs for: "✅ OTP email sent successfully"
6. Enter OTP → Should redirect to set password page
7. Set new password → Should show success
8. Login with new password → Should work
```

---

## 🚨 Common Issues & Solutions

### Issue: "502 Bad Gateway" persists

**Diagnosis Steps:**

1. **Check if service is running:**
   - Render Dashboard → Service Status
   - Should show "Live" (green)

2. **Check recent deployments:**
   - Render Dashboard → Events
   - Look for failed builds or crashes

3. **Check logs immediately after 502:**
   ```bash
   # Look for traceback or error message
   # Common patterns:
   - "Worker timeout"
   - "Application error"
   - "Connection refused"
   ```

**Solutions:**

A. **If database error:**
```bash
# Via Render Shell
python manage.py migrate --run-syncdb
```

B. **If email timeout:**
```bash
# Temporarily disable email (for testing)
# Add to Render environment:
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
```

C. **If worker timeout:**
```bash
# Increase timeout in Render settings
# Or optimize slow database queries
```

### Issue: "Login fails for registered user"

**Possible Causes:**

1. **Password not hashed correctly**
   ```bash
   # Via Render Shell
   from users.models import CustomUser
   user = CustomUser.objects.get(email='test@example.com')
   user.set_password('YourPassword123!')
   user.save()
   ```

2. **Wrong database being queried**
   ```bash
   # Verify DATABASE_URL points to PostgreSQL
   # Not sqlite3
   ```

3. **Authentication backend mismatch**
   ```python
   # Already configured in settings.py:
   AUTHENTICATION_BACKENDS = [
       'users.auth_backends.EmailOrUsernameBackend',
       'django.contrib.auth.backends.ModelBackend',
       'allauth.account.auth_backends.AuthenticationBackend',
   ]
   ```

### Issue: "OTP email not received"

**Checklist:**

- [ ] EMAIL_HOST_USER set correctly
- [ ] EMAIL_HOST_PASSWORD is App Password (not regular password)
- [ ] 2FA enabled on Gmail account
- [ ] Check spam folder
- [ ] Check Render logs for email sending confirmation
- [ ] Try alternative email provider (SendGrid)

**Test email manually:**
```bash
# Via Render Shell
python manage.py shell

from django.core.mail import send_mail
send_mail(
    'Test Email',
    'This is a test message.',
    'your.email@gmail.com',
    ['recipient@example.com'],
    fail_silently=False,
)
# Should print "1" if successful
```

### Issue: "User not saved to database"

**Diagnosis:**
```bash
# Via Render Shell
python manage.py showmigrations users
# All should have [X] checkmark

python manage.py dbshell
SELECT COUNT(*) FROM users_customuser;
# Should show number of users
```

**Fix:**
```bash
# If migrations not applied:
python manage.py migrate users

# If table doesn't exist:
python manage.py migrate --run-syncdb
```

---

## 📊 Monitoring & Logs

### Key Log Messages to Watch

**✅ Success Messages:**
```
✅ Email configured: Real emails will be sent via SMTP
✅ Cloudinary configured: Media files will be stored in the cloud
✅ OTP email sent successfully to user@example.com
✅ User successfully created: user@example.com (ID: 123)
✅ OTP verified successfully for: user@example.com
Session set to persist for 2 weeks
```

**⚠️ Warning Messages:**
```
⚠️  Email not configured: Emails will be printed to console
⚠️  Cloudinary not configured: Using local media storage
⚠️  Rate limit hit for password reset: user@example.com
Too many OTP verification attempts for: user@example.com
```

**❌ Error Messages:**
```
❌ Failed to send OTP email to user@example.com
❌ Unexpected error in password reset
django.db.utils.OperationalError
SMTPAuthenticationError
```

### Render Dashboard Monitoring

1. **Metrics Tab:**
   - CPU usage (should be < 80%)
   - Memory usage (should be < 90%)
   - Response times (should be < 500ms)

2. **Logs Tab:**
   - Filter by "Error" to find issues
   - Filter by "✅" to see successful operations

3. **Events Tab:**
   - Check deployment history
   - Look for failed builds

---

## 🔒 Security Checklist

Before going live:

- [ ] DEBUG=False on Render
- [ ] SECRET_KEY is unique and strong (50+ characters)
- [ ] ALLOWED_HOSTS includes only your domain
- [ ] CSRF_TRUSTED_ORIGINS includes https:// prefix
- [ ] EMAIL_HOST_PASSWORD is App Password (not stored in code)
- [ ] Database backups enabled on Render
- [ ] SSL certificate active (automatic on Render)
- [ ] Rate limiting enabled (already implemented)
- [ ] OTP expiry set to 5 minutes (already implemented)

---

## 🚀 Deployment Workflow

### When Pushing New Code:

```bash
# 1. Test locally first
python manage.py runserver
# Visit http://localhost:8000 and test all features

# 2. Commit and push
git add .
git commit -m "Fix 502 errors and database issues"
git push origin main

# 3. Monitor Render deployment
# Dashboard → Logs → Watch build process

# 4. Test on production
# Visit https://ai-resume-builder-6jan.onrender.com
# Test signup, login, password reset

# 5. Check logs for errors
# Dashboard → Logs → Filter by "Error"
```

### Rollback if Issues:

```bash
# Via Render Dashboard
Events → Find last working deployment → Rollback

# Or via Git
git revert HEAD
git push origin main
```

---

## 📞 Support Resources

**Render Documentation:**
- https://render.com/docs/deploy-django
- https://render.com/docs/troubleshooting-deploys

**Django Documentation:**
- https://docs.djangoproject.com/en/5.0/howto/deployment/
- https://docs.djangoproject.com/en/5.0/topics/email/

**Project Documentation:**
- `AUTHENTICATION_FIX_REPORT.md` - Detailed technical report
- `RENDER_DEPLOYMENT_CHECKLIST.md` - Step-by-step guide
- `QUICK_START_GUIDE.md` - Quick reference

---

## ✅ Success Criteria

All these should work without 502 errors:

- [ ] Homepage loads (/)
- [ ] Signup page loads (/accounts/signup/)
- [ ] Signup creates user in database
- [ ] Login page loads (/accounts/login/)
- [ ] Login authenticates correctly
- [ ] Password reset page loads (/accounts/password/reset/)
- [ ] OTP email sent and received
- [ ] OTP verification works
- [ ] Set new password page loads
- [ ] Password update successful
- [ ] Dashboard accessible after login

---

**Last Updated:** 2025-01-28  
**Status:** Ready for Deployment  
**Estimated Fix Time:** 20-30 minutes
