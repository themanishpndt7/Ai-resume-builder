## 🚨 URGENT: Password Reset OTP Not Working - Fix Required

### ❌ Current Problem:
**OTP emails are NOT being sent** on your production site because email environment variables are missing from Render.

### ✅ Root Cause:
Your `.env` file (with email credentials) is **LOCAL ONLY** and not deployed to Render (it's in `.gitignore`).

---

## 🔧 SOLUTION: Add Email Variables to Render (5 Minutes)

### 📋 Step-by-Step Instructions:

#### 1️⃣ Open Render Dashboard
Go to: **https://dashboard.render.com/**

#### 2️⃣ Select Your Service
Click on: **ai-resume-builder-6jan**

#### 3️⃣ Go to Environment Tab
Click the **"Environment"** tab in the left sidebar

#### 4️⃣ Add These 5 Variables
Click **"Add Environment Variable"** for each:

```
Variable 1:
Key:   EMAIL_HOST
Value: smtp.gmail.com

Variable 2:
Key:   EMAIL_PORT
Value: 587

Variable 3:
Key:   EMAIL_USE_TLS
Value: True

Variable 4:
Key:   EMAIL_HOST_USER
Value: mpandat0052@gmail.com

Variable 5:
Key:   EMAIL_HOST_PASSWORD
Value: ehaw vyzx zrgc ngws
```

#### 5️⃣ Save Changes
Click **"Save Changes"** button at the bottom

#### 6️⃣ Wait for Redeploy
- Render will automatically redeploy (2-3 minutes)
- Watch the deployment progress

---

## ✅ Verify It's Working:

### Method 1: Check Render Logs
1. Go to **Logs** tab in Render dashboard
2. Look for this line:
   ```
   ✅ Email configured: Real emails will be sent via SMTP
   ```
3. If you see this instead, it's NOT working yet:
   ```
   ⚠️ Email not configured: Emails will be printed to console
   ```

### Method 2: Test Password Reset
1. Go to: https://ai-resume-builder-6jan.onrender.com/accounts/password/reset/
2. Enter email: `mpandat0052@gmail.com`
3. Click "Send OTP Code"
4. Check your email inbox (should receive OTP within 1-2 minutes)

---

## 📧 Email Credentials Explained:

- **Email:** mpandat0052@gmail.com (your Gmail)
- **App Password:** `ehaw vyzx zrgc ngws` (Gmail App Password, NOT regular password)
- **SMTP Server:** smtp.gmail.com
- **Port:** 587 (TLS)

**Note:** This is a Gmail App Password generated specifically for this app. It's safe to use and can be revoked anytime from your Google Account settings.

---

## 🔍 Diagnostic Tools:

Run locally to verify your .env file:
```bash
python3 check_env_email.py
```

---

## ❓ FAQ:

**Q: Why didn't this work before?**
A: Environment variables in `.env` file are not deployed to Render. They must be added manually in Render dashboard.

**Q: Is my email password secure?**
A: Yes! This is a Gmail App Password (not your real password). It's secure and can only be used for email sending.

**Q: How long does it take for changes to apply?**
A: After saving in Render, redeploy takes 2-3 minutes. Then test immediately.

**Q: What if I still don't receive OTP?**
A: Check:
1. Render logs show "Email configured" 
2. Spam/Junk folder
3. Gmail App Password is still active
4. All 5 variables are spelled correctly (no typos)

---

## ✅ Checklist:

- [ ] Opened Render Dashboard
- [ ] Selected ai-resume-builder-6jan service
- [ ] Clicked Environment tab
- [ ] Added EMAIL_HOST
- [ ] Added EMAIL_PORT
- [ ] Added EMAIL_USE_TLS
- [ ] Added EMAIL_HOST_USER
- [ ] Added EMAIL_HOST_PASSWORD
- [ ] Clicked Save Changes
- [ ] Waited for redeploy to complete
- [ ] Checked logs show "Email configured"
- [ ] Tested password reset
- [ ] Received OTP email successfully

---

**Once completed, your password reset feature will work perfectly! 🎉**

Need help? Check the logs or test with: `python3 check_env_email.py`
