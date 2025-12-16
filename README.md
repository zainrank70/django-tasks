# Django Practice Blog

Simple Django blog used to practice models, forms, templates, and admin. Posts support categories, tags, and a status choice (Draft/Published).

## Quick Start
1) Activate the virtualenv (project preference):  
   `env\Scripts\activate`
2) Apply migrations:  
   `python manage.py makemigrations`  
   `python manage.py migrate`
3) Run the dev server:  
   `python manage.py runserver`

## Features Implemented
- Models: `Post` with `title`, `content`, `status` (choices), optional `category`, and optional many-to-many `tags`; helpers `summary()` and `word_count`.
- Admin: `Post`, `Category`, and `Tag` registered for easy data entry.
- Forms: `PostForm` (ModelForm) exposes title/content/category/tags/status; category and tags are optional, tags use checkboxes.
- Views/Templates:  
  - `/` lists posts and shows status, category, and tags.  
  - `/add/` renders the ModelForm to create posts.  
  - Base template loads static and includes nav links.

## Creating Sample Data
- Via admin: start the server, go to `/admin/`, add categories/tags, then create posts.
- Via form: go to `/add/`, fill in title/content, choose category/tags/status.

## Notes
- `get_status_display` is available because `Post.status` uses `choices`.
- `.gitignore` lives at project root (`myproject/.gitignore`) to cover venv, sqlite DB, cache, and OS cruft.
