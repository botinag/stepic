sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo ln -sf /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/test
sudo ln -sf /home/box/web/etc/django_gunicorn.conf /etc/gunicorn.d/django_test
sudo /etc/init.d/gunicorn restart
sudo mysql -uroot -e "create database stepicdb"
#sudo apt-get install python2.7-mysqldb
python /home/box/web/ask/manage.py syncdb --noinput
