# 🌥️ Cloudinary Setup Guide

## Why Cloudinary?

Render's free tier uses **ephemeral storage** - uploaded files are deleted when the service restarts. Cloudinary provides free, persistent cloud storage for your images.

## Free Tier Benefits
- ✅ **25 GB** storage
- ✅ **25 GB** bandwidth/month
- ✅ **Persistent** storage (files never deleted)
- ✅ **Fast CDN** delivery
- ✅ **Image optimization** built-in

---

## 🚀 Setup Instructions

### Step 1: Create Cloudinary Account

1. Visit: https://cloudinary.com/users/register_free
2. Sign up with email (or use Google/GitHub)
3. Verify your email address
4. Login to your dashboard

### Step 2: Get Your Credentials

After logging in, you'll see your dashboard with:

```
Cloud Name: your-cloud-name
API Key: 123456789012345
API Secret: AbCdEfGhIjKlMnOpQrStUvWxYz
```

**Important:** Keep these credentials secret!

### Step 3: Add to Render Environment Variables

1. Go to your Render dashboard
2. Select your **Ai-resume-builder** service
3. Click **Environment** tab
4. Add these 3 new environment variables:

```
CLOUDINARY_CLOUD_NAME = your-cloud-name
CLOUDINARY_API_KEY = 123456789012345
CLOUDINARY_API_SECRET = AbCdEfGhIjKlMnOpQrStUvWxYz
```

**Replace with your actual values from Cloudinary dashboard!**

### Step 4: Deploy

After adding the environment variables:
1. Render will automatically redeploy
2. Wait 2-3 minutes for deployment to complete
3. Check logs - you should see: `✅ Cloudinary configured: Media files will be stored in the cloud`

---

## ✅ Testing

### Upload a New Project Image

1. Go to: https://ai-resume-builder-6jan.onrender.com/projects/add/
2. Upload a project with a thumbnail image
3. Save the project
4. View projects list - image should load

### Verify on Cloudinary

1. Go to Cloudinary Dashboard
2. Click **Media Library**
3. You should see your uploaded images
4. Images are stored at: `https://res.cloudinary.com/your-cloud-name/image/upload/...`

---

## 🔄 Migration (Optional)

If you have existing projects with broken images, you'll need to:
1. Re-upload the images for those projects
2. Edit each project and add the thumbnail again

---

## 🎯 Benefits After Setup

- ✅ Images persist across service restarts
- ✅ Fast loading from Cloudinary CDN
- ✅ Automatic image optimization
- ✅ No storage limits (within free tier)
- ✅ Professional image delivery

---

## 📝 Local Development

For local development, you can either:
1. Use the same Cloudinary credentials (recommended)
2. Or leave them empty to use local storage

The app automatically detects Cloudinary credentials and switches storage accordingly.

---

## 🆘 Troubleshooting

### Images Still Not Loading?

1. **Check environment variables** in Render:
   - All 3 variables set correctly?
   - No typos in credentials?

2. **Check deployment logs**:
   - Look for: `✅ Cloudinary configured`
   - If you see: `⚠️ Cloudinary not configured` - credentials are missing

3. **Re-upload images**:
   - Old images stored locally won't migrate automatically
   - Edit projects and re-upload thumbnails

4. **Clear browser cache**:
   - Hard refresh: `Ctrl + Shift + R` (Chrome/Edge)
   - Or use incognito mode

### Need Help?

Contact Cloudinary support: https://support.cloudinary.com/

---

## 📊 Monitor Usage

Check your Cloudinary usage at:
https://cloudinary.com/console/usage

Free tier limits:
- Storage: 25 GB
- Bandwidth: 25 GB/month
- Transformations: 25,000/month

For a resume builder, this is **more than enough**!

---

**That's it! Your images will now be stored permanently in the cloud.** ☁️✨
