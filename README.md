
# clashboard

A [Plot.ly Dash](https://dash.plot.ly/) dashboard  to explore [ClinicalTrails.gov](https://clinicaltrials.gov/) data 
stored in a PostgreSQL database hosted by 
[Clinical Traials Transformation Initiative](https://aact.ctti-clinicaltrials.org/).


## Developer Setup

1. Create a virtual environment named `.venv`

    `python3 -m venv .venv`

2. Activate the virtual environment

    `source .venv/bin/activate`
    
3. Install required libraries

    `pip install -r requirements.txt`
    
4. Install source of this repo as an editable package

    `pip install -e .`
    
5. Create the file `.env` containing our sensitive data (This file is named in
   `.gitignore` because it should never go in the repo)

  ```
  hostname=aact-db.ctti-clinicaltrials.org
  port=5432
  database=aact
  username=your_username
  password=your_password

  ```   

## Launch on AWS

* Create an t2.large EC2 instance based on Ubuntu 18. Storage should be 32+ GB.
* Make sure to open port 80.
* `sudo apt update`
* `sudo apt install -y python3-pip`
* `sudo apt install -y postgresql`
* `sudo apt install -y unzip`
* Clone this repo.
* `cd clashboard`
* `sudo pip3 install -r requirements.txt`
* Create a file `.env` with the following:

  ```
  hostname=localhost
  port=5432
  database=aact
  username=postgres
  password=your_password

  ```

* [Here](https://aact.ctti-clinicaltrials.org/snapshots) we can access a walkthrough to setting up the database and [here](https://help.ubuntu.com/stable/serverguide/postgresql.html) we can get information on configuring the database. First we want to set up the database user and password:
* `sudo -u postgres psql template1`
* `ALTER USER postgres with password 'your_password';`

* After configuring the password, edit the file `/etc/postgresql/10/main/pg_hba.conf` to use MD5 authentication with the postgres user:
`local all postgres md5`

* `sudo systemctl restart postgresql.service`

* We retrieve the most recent data with the following command `sudo ./get_most_recent_data.sh`

* To add the schema that AACT tables are saved in: `psql aact` and then `alter role your-username in database aact set search_path = ctgov, public;`

* To launch the flask application first we copy `clashboard.service` to the directory `/etc/systemd/system`. Next, we run the following commands: 
* `sudo systemctl start clashboard`
* `sudo systemctl enable clashboard`