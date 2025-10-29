# AI Resume Builder

A Django-based application to create professional resumes and cover letters using AI-powered tools. This repository contains the web application, authentication (custom user model), email utilities, deployment config (Render / Procfile), and UI templates with enhanced frontend interactions.

---

## Quick overview

- Framework: Django 4.x (project configured for Python 3.10 in `runtime.txt`)
- WSGI server: Gunicorn (used in `Procfile` / `render.yaml`)
- Storage: Local `media/` by default; optional Cloudinary integration via environment variables
- Database: SQLite by default (development). PostgreSQL can be configured using `DATABASE_URL`.

Features
- AI-powered resume and cover letter generation (OpenAI integration placeholder via `OPENAI_API_KEY`).
- Custom authentication with email-first `CustomUser` model and support for username.
- OTP models for signup and password reset flows.
- Accessible, animated signup and login templates with client-side password strength checks and progressive enhancement.
- Utilities and scripts for email testing and deployment helper scripts.

---

## Repository layout (important files)

- `manage.py` - Django CLI entrypoint
- `core/` - Django project settings and WSGI/ASGI
  - `core/settings.py` - main settings (env-driven)
- `users/` - custom user app (models, forms, adapters, auth backends)
- `resume/` - main resume app (templates, models, views)
- `templates/` - project-level templates (account, resume, base)
- `static/` - development static assets
- `staticfiles/` - collected static artifacts
- `media/` - uploaded media (profile photos, resumes)
- `requirements.txt` - pinned Python dependencies
- `Procfile` - run command for Heroku/Render: `gunicorn core.wsgi:application`
- `render.yaml` - Render.com service & DB config
- `runtime.txt` - pinned Python runtime for Render (python-3.10.0)
- `db.sqlite3` - development SQLite database (if present)

---

## Prerequisites

- Python 3.10 (project `runtime.txt` uses 3.10.0)
- pip (or pipx/virtualenv)
- (Optional) PostgreSQL if you want a production-like DB locally

---

## Local setup (development)

1. Create and activate a virtual environment (recommended):

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Copy environment variables (create a `.env` file at project root) and set the values you need. Example entries:

```env
SECRET_KEY=replace-with-a-secret
DEBUG=True
DATABASE_URL=                  # optional, leave blank for SQLite
EMAIL_HOST_USER=                 # optional: SMTP email user
EMAIL_HOST_PASSWORD=             # optional: SMTP email password
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
DEFAULT_FROM_EMAIL=noreply@airesume.com
OPENAI_API_KEY=                  # optional: OpenAI API key if using AI features
CLOUDINARY_CLOUD_NAME=           # optional: to enable Cloudinary
CLOUDINARY_API_KEY=
CLOUDINARY_API_SECRET=
```

4. Run migrations and create a superuser:

```bash
python manage.py migrate
python manage.py createsuperuser
```

5. Collect static files (optional during development):

```bash
python manage.py collectstatic --noinput
```

6. Run the dev server:

```bash
python manage.py runserver
```

Open http://127.0.0.1:8000/ (or the configured host) and try the signup/login flows.

---

## Environment variables (summary)

The project is environment-driven using `python-dotenv`. Important variables:

- `SECRET_KEY` — Django secret key (generate for production)
- `DEBUG` — set to `False` in production
- `DATABASE_URL` — optional; when present, used by `dj_database_url` (Postgres recommended)
- `RENDER_EXTERNAL_HOSTNAME` — used to add allowed host in production (Render)
- `CLOUDINARY_CLOUD_NAME`, `CLOUDINARY_API_KEY`, `CLOUDINARY_API_SECRET` — enable Cloudinary for media
- `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`, `EMAIL_HOST`, `EMAIL_PORT`, `EMAIL_USE_TLS` — SMTP settings; if missing, emails are printed to console
- `DEFAULT_FROM_EMAIL`, `OPENAI_API_KEY`

Note: Default behavior in absence of email credentials: `EMAIL_BACKEND` is `console.EmailBackend` (helpful for local dev).

---

## Testing

Run Django's test suite:

```bash
python manage.py test
```

There are several test helpers and scripts in the repo (`test_*` files) used for email/OTP diagnostics. Adjust and run them as needed.

---

## Deployment notes

- `Procfile` and `render.yaml` are present for deployment to Render (or Heroku-like platforms). The `Procfile` uses Gunicorn.
- `render.yaml` defines a managed PostgreSQL database and environment variables to be generated on Render.
- The project uses WhiteNoise for static file serving and has optional Cloudinary integration for persistent media storage. Be careful when deploying to platforms with ephemeral storage (files saved to disk may be lost on restart).

Recommended production steps
- Set `DEBUG=False`, provide a secure `SECRET_KEY`, configure `DATABASE_URL` (Postgres), and set up SMTP credentials.
- Configure Cloudinary or another permanent storage for media files.
- Run `python manage.py collectstatic` during build.

---

## Important implementation notes (from codebase)

- Custom user model: `users.models.CustomUser` (AUTH_USER_MODEL configured in `core/settings.py`).
  - Uses email as `USERNAME_FIELD`. `username` is still required in `REQUIRED_FIELDS`.
  - `DeletedEmail` stores emails of deleted users to prevent immediate reuse (30-day rule).
  - `SignupOTP` and `PasswordResetOTP` are used for OTP-based flows with short expiry (5 minutes).

- Authentication: project includes a custom backend `users.auth_backends.EmailOrUsernameBackend` and `allauth` integration for additional account flows. Check `users/` for adapters and forms.

- Frontend: templates under `templates/account/` include the signup and login pages with animated SVGs, password strength indicators, and accessible password-toggle buttons. Client-side validation complements server-side checks (server-side validation still authoritative).

- Email helper scripts: there are several utilities in the project root for diagnosing email configuration (e.g., `test_gmail_credentials.py`, `test_email_sending.py`, `check_email_config.py`, `verify_deployment.py`). Use them to debug email delivery in development.

---

## Troubleshooting & common pitfalls

- Cloudinary not configured: By default the project will use local `media/` storage. To persist user uploads in production, set the Cloudinary environment variables.
- Emails not sending: If `EMAIL_HOST_USER` and `EMAIL_HOST_PASSWORD` are not set, emails will be printed to console. Verify SMTP settings and allow less-secure access (or use app passwords) for providers like Gmail.
- Static files missing in production: Ensure `collectstatic` runs during your build and WhiteNoise is configured correctly. The settings use `CompressedManifestStaticFilesStorage`.
- Database migrations: When switching from SQLite to Postgres, run makemigrations/migrate; if migrating existing data, plan for data migration.

---

## Contributing

If you'd like to contribute:

1. Fork the repo and create a feature branch.
2. Add tests for new behavior.
3. Open a PR with clear description and testing steps.

---

## License

No license file is included in the repository. Add a `LICENSE` file to specify licensing terms if you plan to open-source the project.

---

## Contact / Next steps

If you want, I can:
- Add a CI configuration (GitHub Actions) to run tests on PRs.
- Add an `example.env` file with recommended env var values (non-sensitive placeholders).
- Add a simple `Makefile` for frequent tasks (runserver, test, shell).

---

Generated from repository content on 2025-10-29.
