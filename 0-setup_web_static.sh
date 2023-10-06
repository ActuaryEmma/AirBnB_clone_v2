#!/usr/bin/env bash
# sets up web servers for the deployment of web_static

apt -y update
apt install -y nginx
service nginx start
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared
mkdir -p /data/web_static/releases/test/
echo "Test data for task 1" > /data/web_static/releases/test/index.html
rm /data/web_static/current
ln -s /data/web_static/releases/test /data/web_static/current
chown -R ubuntu:ubuntu /data/
config_file="/etc/nginx/sites-available/default"
nginx_config="location /hbnb_static/ {
    alias /data/web_static/current/;
}"
sed -i "/server_name _;/a\\        location /hbnb_static/ {alias /data/web_static/current/;}" "$config_file" > /dev/null
# sed -i "/server_name _;/a $nginx_config" "$config_file"
service nginx restart
