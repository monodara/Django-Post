# Django Portfolio & Blog

This project is a personal portfolio and blog website built with Django. It showcases projects, provides contact information, and features a blog for sharing articles. 

## Live Demo
This project is deployed on **Google Cloud Run**. Media files are served from **Google Cloud Storage**. 

Please feel free to explore my stories here: 
[Yuanyuan Lu's Portfolio](https://portfolio-web-django-177254561081.europe-north1.run.app)

## Features

### Portfolio
*   Display of personal projects with descriptions, images, and links (e.g., GitHub).
*   Categorization of projects into groups.
*   About, Experience, Hobbies, and Contact sections.

### Blog
*   Create, edit, and publish blog posts.
*   Rich text editing for blog content using CKEditor 5.
*   Post listing and detailed post views.

### Admin Interface
*   Full administrative control over blog posts, project groups, projects, and other content via Django's built-in admin.

## Technologies Used

*   **Backend:** Django (Python Web Framework)
*   **Database:** SQLite (local development), PostgreSQL (production via `dj-database-url`)
*   **Frontend:** HTML, CSS, JavaScript (with Bootstrap for styling)
*   **Rich Text Editor:** `django-ckeditor-5`
*   **Static Files:** `whitenoise`
*   **Media Storage:** Google Cloud Storage (`django-storages`)

