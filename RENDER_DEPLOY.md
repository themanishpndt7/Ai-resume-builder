# Render deployment guide — AI Resume Builder

This document describes the recommended steps and Render-specific configuration to deploy the AI Resume Builder project to Render.com.

IMPORTANT: Do NOT commit secrets to the repository. Store all secrets in Render's Environment section.

## 1. Summary

- Set required environment variables in Render (SECRET_KEY, DATABASE_URL, EMAIL credentials, Cloudinary keys).
- Set `DEBUG=false` in Render environment for production.
- Attach a Render PostgreSQL instance and use its `DATABASE_URL` value.
- Ensure the build step runs migrations and `collectstatic`.
- Create a superuser in Render Web Shell and verify admin and auth flows.

## 2. Environment variables to set (Render → Environment)

Set the following variables (values shown are examples; replace with your secure values):

- SECRET_KEY: a strong random string (do not commit)
- DEBUG: false
- DATABASE_URL: provided by the Render PostgreSQL service (starts with `postgres://`)
- RENDER_EXTERNAL_HOSTNAME: (optional) Render sets this automatically

Email (Gmail example — use 2FA + app password):
- EMAIL_HOST_USER: mpandat0052@gmail.com
- EMAIL_HOST_PASSWORD: <your_gmail_app_password>
- EMAIL_HOST: smtp.gmail.com
- EMAIL_PORT: 587
- EMAIL_USE_TLS: True

Cloudinary (if using Cloudinary):
- CLOUDINARY_CLOUD_NAME: dud3f00ay
- CLOUDINARY_API_KEY: 764652939378289
- CLOUDINARY_API_SECRET: gu7Rwmz8jB4I0vsI3VYZNC3Ri0Q

Other useful env:
- OPENAI_API_KEY: <your-openai-key>
- DEFAULT_FROM_EMAIL / SERVER_EMAIL: e.g. "AI Resume Builder <mpandat0052@gmail.com>"

## Complete list of environment variables (what the app reads)

Below is a comprehensive list of environment variables that the project reads or that are recommended to configure for a production deploy on Render. Set these in Render → Environment.

- SECRET_KEY — string — REQUIRED in production. Example: a long random string. Do NOT commit to source.
- SECRET_KEY — string — REQUIRED in production. Example: a long random string. Do NOT commit to source.

If you currently see the value `django-insecure-pu3b0yc-...` (or any `django-insecure-...`) in Render's Environment, treat it as insecure and rotate it immediately:

1. Generate a new secret locally (one-liners):

```bash
python3 - <<'PY'
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
PY
```

or

```bash
python3 - <<'PY'
import secrets
print(secrets.token_urlsafe(50))
PY
```

or

```bash
openssl rand -base64 48
```

2. Update Render Environment → set `SECRET_KEY` to the newly generated value and remove any insecure placeholder.

3. Restart the service / redeploy. Note: rotating SECRET_KEY will invalidate existing sessions and signed data (password reset tokens, etc.). Plan for this accordingly.

4. Verify the app starts with no `ImproperlyConfigured` errors (the settings now require SECRET_KEY in production). If you get an error after removing the old key, ensure you set the new value correctly in Render env and redeploy.

Security note: keep the secret only in Render's Environment variables (or a secret manager). Do not commit it or paste it in public chat logs.
- DEBUG — boolean — Set to `False` in production. Example: `False`.
- ALLOWED_HOSTS — comma-separated hostnames — Optional: if set, will override defaults. Example: `ai-resume-builder-6jan.onrender.com,localhost`.
- RENDER_EXTERNAL_HOSTNAME — optional, provided by Render for convenience.
- DATABASE_URL — REQUIRED for Postgres on Render. Example: `postgres://user:pass@host:port/dbname` (Render provides this).

Email (SMTP) — required to send real emails (signup, OTP, password reset):
- EMAIL_BACKEND — optional, default `django.core.mail.backends.smtp.EmailBackend`.
- EMAIL_HOST — default `smtp.gmail.com`.
- EMAIL_PORT — default `587`.
- EMAIL_USE_TLS — default `True`.
- EMAIL_HOST_USER — your SMTP username (e.g. Gmail address).
- EMAIL_HOST_PASSWORD — your SMTP password (Gmail requires an app password when 2FA is enabled).
- DEFAULT_FROM_EMAIL — email used as From address for outgoing mails.
- SERVER_EMAIL — address for server-generated messages (error emails).

Cloudinary (for persistent media storage):
- CLOUDINARY_CLOUD_NAME
- CLOUDINARY_API_KEY
- CLOUDINARY_API_SECRET

Third-party / optional:
- OPENAI_API_KEY — for OpenAI integration (if used).
- PYTHON_VERSION — Render setting for runtime, e.g. `3.10.0`.

Notes:
- Do not store secrets in the repo. Use Render's encrypted environment variables.
- If `ALLOWED_HOSTS` is provided, the application will parse it as a comma-separated list and use it directly.
- The settings file enforces `ssl_require=True` when parsing `DATABASE_URL` to ensure TLS connections to Postgres on Render.

## 3. Render service settings

- Runtime: Python 3 (use the same version as your local dev environment). The repo contains `runtime.txt`.
- Build Command (example):

```bash
pip install -r requirements.txt
python3 manage.py migrate --noinput
python3 manage.py collectstatic --noinput
```

- Start Command (example):

```bash
gunicorn core.wsgi --log-file -
```

Adjust the start command to match your preferred WSGI server; the repo includes `Procfile` which may be used by Render.

## 4. Database and SSL

- Attach a managed Postgres instance in Render and copy the `DATABASE_URL` into environment variables for the web service.
- The application has `dj_database_url.config(..., ssl_require=True)` enabled to enforce SSL for Render Postgres.

## 5. Static & Media files

- Static files are served by WhiteNoise from `STATIC_ROOT` (the project sets `STATIC_ROOT = BASE_DIR / 'staticfiles'`). Running `collectstatic` is required.
- Media files should be stored on Cloudinary (recommended for Render since the filesystem is ephemeral). Configure Cloudinary keys in environment variables.

## 6. Recommended deploy sequence

1. Push code to your Git remote (connected to Render) or trigger a manual deploy.
2. In Render Dashboard → Service → Environment, set the variables listed above.
3. Ensure the Build Command includes `migrate` and `collectstatic` (see example above).
4. Deploy. If the build succeeds, open Render Web Shell and run:

```bash
# Ensure migrations are applied (if not already run during build)
python3 manage.py migrate --noinput
# Create an admin user
python3 manage.py createsuperuser
# Example admin credentials (change to secure values):
# username: mani
# email: mpandat214@gmail.com
# password: 123456
```

> Note: Use a secure password in production.

## 7. Post-deploy checks

- Admin: https://ai-resume-builder-6jan.onrender.com/admin/ — log in with the admin account.
- Test signup/login/forgot-password flows from the public site.
- Trigger an OTP or password-reset email and check Render logs for SMTP activity. The app config includes email logger set to DEBUG which helps diagnose problems.

## 8. Troubleshooting

- Emails not sending:
  - Verify `EMAIL_HOST_USER` and `EMAIL_HOST_PASSWORD` (Gmail requires 2FA + app password).
  - Check Render logs for SMTP debug output.
- Database connection errors:
  - Confirm the `DATABASE_URL` is correct and that the Postgres service is attached to your web service.
  - Ensure `ssl_require=True` (already enforced by settings) and that the URL is not malformed.
- Static files missing or 404:
  - Ensure `collectstatic` ran successfully during the build. Check `staticfiles` directory created on the filesystem.
- Media files disappearing after restart:
  - Render's filesystem is ephemeral; use Cloudinary or another remote storage for persistent media.

## 9. Security notes

- Never commit `SECRET_KEY`, `EMAIL_HOST_PASSWORD`, or Cloudinary API secret to the repository.
- Rotate app passwords and API keys if they are exposed.
- Keep `DEBUG=false` in production.

## 10. Optional improvements

- Configure a CI/CD pipeline to automatically run migrations and `collectstatic` before or during deploy.
- Use Render's `render.yaml` for reproducible infra-as-code (not included here).

---

If you want, I can:
- Remove the hardcoded demo secrets from `core/settings.py` and require env variables only (recommended),
- Create a `render.yaml` snippet for this service,
- Add a small health check endpoint for Render to use.
