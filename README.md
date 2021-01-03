# task_management
An API App for task management

Setup to configure and run the project:

1. python manage.py migrate
2. python manage.py runserver
3. sudo systemctl restart redis.service
4. celery -A app  worker -B -l info 
5. In app/email_config.py replace the EMAIL_CONFIG 'host_user' and 'password' with email and password of a valid account (Sending Email notification and weekly reports to admin)