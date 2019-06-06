#!/bin/bash

apt update
apt install -y python3-pip
apt install -y postgresql
apt install -y unzip
cd clashboard
pip3 install -r requirements.txt
pip3 install -e .
echo "hostname=localhost\nport=5432\ndatabase=aact\nusername=postgres\npassword=your_password" > .env
sudo -u postgres psql template1
ALTER USER postgres with password 'your_password';
\q
