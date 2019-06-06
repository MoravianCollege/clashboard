#!/bin/bash expect

apt update
apt install -y python3-pip
apt install -y postgresql
apt install -y unzip
cd clashboard
pip3 install -r requirements.txt
pip3 install -e .
echo "hostname=localhost\nport=5432\ndatabase=aact\nusername=postgres\npassword=your_password" > .env
-u postgres psql template1 -c "ALTER USER postgres with password 'your_password';"
sed -i 's/local   all             postgres                                peer/local   all             postgres                                md5/g' /etc/postgresql/10/main/pg_hba.conf
systemctl restart postgresql.service
~/scripts/get_most_recent_data.sh
send "your_password"
