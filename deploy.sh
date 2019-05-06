#!/bin/bash

source /home/ubuntu/venv/bin/activate

echo 'Be sure to run with sudo'

echo '** Pulling latest version'
git pull

echo '** Installing changed pip packages'
pip install -q -r /home/ubuntu/computation_hist/requirements.txt

echo '** Collecting static'
python /home/ubuntu/computation_hist/manage.py collectstatic --noinput || exit 1

echo '** Stopping nginx'
service nginx stop 

echo '** Stopping computation_hist'
supervisorctl stop computation_hist

echo '** Copying nginx.conf to /etc'
cp /home/ubuntu/computation_hist/config/deploy/nginx.conf /etc/nginx/sites-available/computation_hist

echo '** Copying supervisor conf to /etc'
cp /home/ubuntu/computation_hist/config/deploy/supervisor.conf /etc/supervisor/conf.d/computation_hist.conf

supervisorctl reread
supervisorctl update

echo '** Restarting gunicorn/django'
supervisorctl start computation_hist

echo '** starting nginx'
service nginx start
service nginx status
