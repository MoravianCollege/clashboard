#!/bin/bash

sudo apt update
sudo apt install -y python3-pip
sudo apt install -y postgresql
sudo apt install -y unzip
cd clashboard
sudo pip3 install -r requirements.text
sudo pip3 install -e .
sudo echo -e "hostname=localhost\nport=5432\ndatabase=aact\nusername=postgres\npassword=your_password" > .env
