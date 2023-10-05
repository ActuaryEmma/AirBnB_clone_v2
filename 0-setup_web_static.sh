#!/usr/bin/env bash
# sets up web servers for the deployment of web_static

sudo apt -y update
sudo apt install -y nginx
sudo service nginx start
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared
sudo mkdir -p /data/web_static/releases/test/
sudo echo "Test data for task 1" | sudo tee /data/web_static/releases/test/index.html > /dev/null 2>&1
sudo rm /data/web_static/current
sudo ln -s /data/web_static/releases/test /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
config_file="/etc/nginx/sites-available/default"
nginx_config="location /hbnb_static/ {
    alias /data/web_static/current/;
}"
if ! grep -q "$nginx_config" "$config_file"; then
	sudo sed -i "/server_name _;/a $nginx_config" "$config_file"
fi

sudo service nginx restart
exit 0
