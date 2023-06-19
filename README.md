# ADEF Camps Platform

The ADEF Education Camp Platform is a web application designed for trainers, trainees, and managers to create workshops
and manage enrollments. It provides a centralized platform for organizing educational events and tracking the progress
of trainees.

## Features

- User roles: Trainers, trainees, and managers.
- Workshop management: Create, update, and delete workshops.
- Enrollment tracking: Keep track of trainees enrolled in each workshop.
- User authentication: Secure login and registration using Django's built-in authentication system.
- SQLite database: Uses a lightweight SQLite database for data storage.

## Requirements

- Python 3.9 or later
- Django 4.2 or later
- SQLite database

## Getting Started

Follow these step-by-step instructions to clone and run the web app in a Linux environment:

1. Clone the repository:

```
$ git clone https://github.com/AhmedRS97/adef-camps.git
```

2. Change into the project directory:

```
$ cd adef-camps
```

3. Set up a virtual environment:

```
$ python3 -m venv venv
$ source venv/bin/activate
```

4. Install the project dependencies:

```
$ pip install -r requirements.txt
```

5. Apply the database migrations:

```
$ python manage.py migrate
```

6. Create a super user:

```
$ python manage.py createsuperuser
```

7. Start the development server:

```
$ python manage.py runserver
```

8. Open your web browser and visit http://localhost:8000 to access the web app.

## Configuration

The default configuration settings should work for a local development environment. However, if you need to customize
the configuration, you can do so in the `config/settings.py` file.

## Deployment

For deployment in a production environment, it is recommended to follow the Django deployment best practices. This
includes configuring a more robust database backend, setting up static and media file serving, and securing the
application using HTTPS.

## Contributing

Contributions to the ADEF Education Camp Platform are welcome! If you find a bug or have suggestions for improvements, please
open an issue or submit a pull request on the GitHub repository.

## License

This project is licensed under the [MIT License](LICENSE).
