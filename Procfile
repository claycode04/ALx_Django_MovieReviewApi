release: python manage.py collectstatic --noinput
web: python manage.py migrate --noinput && gunicorn movie_review.wsgi --log-file -
