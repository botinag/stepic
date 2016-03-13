sudo ln -sf /home/box/webetc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo ln -sf /home/box/webetc/gunicorn.conf /etc/gunicorn.d/test
sudo ln -sf /home/box/webetc/django_gunicorn.conf /etc/gunicorn.d/django_test
sudo /etc/init.d/gunicorn restart
