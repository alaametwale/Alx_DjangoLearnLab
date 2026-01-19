# Advanced Features and Security – Django

This project is part of the ALX Back-End Web Development program.
It focuses on implementing advanced Django features related to
authentication, permissions, and security best practices.

## Project Structure

advanced_features_and_security/
├── manage.py
├── LibraryProject/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── bookshelf/
│   ├── models.py
│   ├── admin.py
│   ├── views.py
│   ├── forms.py
│   └── templates/
│       └── bookshelf/
│           ├── book_list.html
│           └── form_example.html
└── README.md

---

## Custom User Model

- The default Django user model is replaced with a custom user model.
- The custom user model extends `AbstractUser`.
- Additional fields:
  - `date_of_birth`
  - `profile_photo`
- A custom user manager is implemented with:
  - `create_user`
  - `create_superuser`

The custom user model is configured in `settings.py` using:

```python
AUTH_USER_MODEL = 'bookshelf.CustomUser'
