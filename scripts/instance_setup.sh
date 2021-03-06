#!/bin/bash
RECENT_DATA_SCRIPT="./scripts/get_most_recent_data.sh"
# This script is working, but still prompts for your password and the original
# password is embedded in the command creating the .env file.

apt update
apt install -y python3-pip
apt install -y postgresql
apt install -y unzip
cd clashboard
pip3 install -r requirements.txt
pip3 install -e .
#read -sp "Enter new postgres password for PSQL: " PSQLpassword
#echo
echo "hostname=localhost\nport=5432\ndatabase=aact\nusername=postgres\npassword=PSQLpassword" > .env
sudo -u postgres psql template1 -c "ALTER USER postgres with password 'PSQLpassword';"
# manually enter password
sed -i 's/local   all             postgres                                peer/local   all             postgres                                md5/g' /etc/postgresql/10/main/pg_hba.conf
systemctl restart postgresql.service
# manually enter password x3
(exec "$RECENT_DATA_SCRIPT")
sudo -u postgres psql aact -c "alter role postgres in database aact set search_path = ctgov, public;"
# manually enter password
cp ./scripts/clashboard.service /etc/systemd/system
sudo systemctl start clashboard
sudo systemctl enable clashboard
