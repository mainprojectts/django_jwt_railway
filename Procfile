web: gunicorn tutorialproject.wsgi --log-file -
worker: celery -A tutorialproject worker --loglevel=info
web: python manage.py migrate && gunicorn tutorialproject.wsgi