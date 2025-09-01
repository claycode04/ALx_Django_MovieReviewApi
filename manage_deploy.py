#!/usr/bin/env python
import os
import sys

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movie_review.settings')
    
    from django.core.management import execute_from_command_line
    
    # Run migrations and collect static files for deployment
    if 'runserver' not in sys.argv:
        if os.getenv('RAILWAY_ENVIRONMENT'):
            # We're on Railway, run setup commands
            execute_from_command_line(['manage.py', 'migrate', '--noinput'])
            execute_from_command_line(['manage.py', 'collectstatic', '--noinput'])
    
    execute_from_command_line(sys.argv)
