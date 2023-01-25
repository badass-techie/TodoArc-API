# TodoArc

A Django-based to-do list app that helps you stay organized and on top of your tasks

## Features

- [ ] User authentication and authorization
- [x] Create, read, update, and delete tasks
- [x] Assign due dates to tasks
- [x] Mark tasks as complete
- [x] View completed tasks

## Installation

1. Clone this repository and navigate into the project directory.

```bash
git clone https://github.com/YOUR_USERNAME/TodoArc.git
cd TodoArc
```

2. Create a virtual environment and activate it.

```bash
python -m venv venv
source venv/bin/activate
```

3. Install the required packages.

```bash
pip install -r requirements.txt
```

4. Apply the migrations.

```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create a superuser.

```bash
python manage.py createsuperuser
```

6. Run the development server.

```bash
python manage.py runserver 8080
```

## License

This project is licensed under the MIT License
