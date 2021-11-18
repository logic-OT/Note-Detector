web: daphne Chat_project.asgi:application --port $PORT bind 0.0.0.0
worker: python manage.py runworker channels --settings=Chat_project.settings -v2