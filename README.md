
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

* Create an t2.medium EC2 instance based on Ubuntu 18
* `sudo apt-get update`
* `sudo apt-get install -y python3-pip`
* clone this repo
* `sudo pip3 install -r requirements.txt`
* Create a file `.env` with the following:

  ```
  hostname=aact-db.ctti-clinicaltrials.org
  port=5432
  database=aact
  username=your_username
  password=your_password

  ```
* sudo gunicorn app:app.server

