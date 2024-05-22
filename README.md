# Online Chat Application

This is a Django-based web application for online chatting. It includes features for user registration, login, posting comments, and deleting comments.

## Features

- User registration and login
- Post and delete comments
- Simple and user-friendly interface

## Requirements

- Python 3.x
- Django 3.x or later
- Bootstrap 4.5.2 for styling (included via CDN)

## Installation

1. **Clone the repository**:
   ```bash
    git clone https://github.com/DinisRk/FreeOnlineChat.git
    cd FreeOnlineChat
    ```

3. **Create a virtual environment**:
   ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```
5. **Install the required packages**:
   ```bash 
   pip install -r requirements.txt
    ```
7. **Apply migrations**:
   ```bash
   python manage.py migrate
   ```
9. **Create a superuser (for accessing the Django admin panel)**:
 ```bash
   python manage.py createsuperuser
  ```
10. **Run the development server**:
    ```bash
     python manage.py runserver
    ```
7.** Open your browser and go to http://127.0.0.1:8000 to see the application**:

### Project Structure
```bash
online-chat-app/
│
├── myapp/
│   ├── migrations/
│   ├── templates/
│   │   └── myapp/
│   │       ├── index.html
│   │       ├── inicio.html
│   │       ├── registro.html
│   │       ├── entrada.html
│   │       └── eliminar_comentario.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── online_chat/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── manage.py
└── README.md
  ```



### Templates

- `index.html`: The homepage of the application.
- `inicio.html`: The login page.
- `registro.html`: The registration page.
- `entrada.html`: The page where users can post and view comments.
- `eliminar_comentario.html`: The confirmation page for deleting a comment.

### Models

- `Comment`: The model for storing comments.

### Forms

- `UserCreationForm`: The default Django form for user registration.
- `CommentForm`: A form for submitting comments.

### Views

- `index`: The view for rendering the homepage.
- `inicio`: The view for handling user login.
- `registro`: The view for handling user registration.
- `entrada`: The view for displaying and posting comments.
- `eliminar_comentario`: The view for deleting comments.


## Additional Notes

### Templates

- `index.html`: The homepage of the application.
- `inicio.html`: The login page.
- `registro.html`: The registration page.
- `entrada.html`: The page where users can post and view comments.
- `eliminar_comentario.html`: The confirmation page for deleting a comment.

### Models

- `Comment`: The model for storing comments.

### Forms

- `UserCreationForm`: The default Django form for user registration.
- `CommentForm`: A form for submitting comments.

### Views

- `index`: The view for rendering the homepage.
- `inicio`: The view for handling user login.
- `registro`: The view for handling user registration.
- `entrada`: The view for displaying and posting comments.
- `eliminar_comentario`: The view for deleting comments.
