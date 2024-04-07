#!/usr/bin/env bash
# Script that sets up web servers for the deployment of web_static

# Update package lists
sudo apt-get update

# Install nginx
sudo apt-get -y install nginx

# Allow Nginx through the firewall
sudo ufw allow 'Nginx HTTP'

# Create necessary directories
sudo mkdir -p /data/web_static/{releases/test/,shared/}

# Create a simple HTML file for testing
sudo touch /data/web_static/releases/test/index.html
sudo echo "
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html >/dev/null

# Create symbolic link
sudo ln -s -f /data/web_static/releases/test/ /data/web_static/current

# Change ownership of /data folder
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default

# Restart Nginx to apply changes
sudo service nginx restart
