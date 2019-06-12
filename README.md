
# clashboard

A [Plot.ly Dash](https://dash.plot.ly/) dashboard to explore [ClinicalTrials.gov](https://clinicaltrials.gov/) data
stored in a PostgreSQL database hosted by
[Clinical Trials Transformation Initiative](https://aact.ctti-clinicaltrials.org/).


## Developer Setup

1. Create a virtual environment named `.venv`

    `python3 -m venv .venv`

2. Activate the virtual environment

    `source .venv/bin/activate`

3. Install required libraries

    `pip install -r requirements.txt`

4. Install source of this repo as an editable package

    `pip install -e .`

5. Create the file `.env` containing our sensitive data (This file is listed in
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

## Continuous Deployment Setup

* First we clone the production repo, not a fork, so that Travis-CI will be deploying to the correct repo.
* Create an SSH key: `ssh-keygen -b 4096 -C 'build@travis-ci.com' -f ./deploy_rsa` in that clone.
* Place the public key in the server's authorized users file.
* Encrypt the private key: `travis encrypt-file deploy_rsa --org --add`. This will use the travis-ci.org endpoint and add the appropriate line to the `.travis.yml` file. Replacing the `--org` flag with `--pro` will use the travis-ci.com endpoint.
* Edit the `.travis.yml` and change `before_install` to `before_deploy`. The generated version makes the file available during testing, which isn't necessary - and is a security risk.
* Add `deploy_rsa.enc` and the edited version of `.travis.yml` to the repo. NOT `deploy_rsa`, which is the unencrypted version!!!
* Edit both IPs in `.travis.yml` and edit the path to the `deploy.sh` script.
* Finally, add `deploy.sh` to the repo so that Travis-CI can deploy the project

```
addons:
  ssh_known_hosts:
  - 18.218.152.78
before_deploy:
- openssl aes-256-cbc -K $encrypted_49099c38b3b5_key -iv $encrypted_49099c38b3b5_iv -in deploy_rsa.enc -out deploy_rsa -d
- chmod 600 deploy_rsa
deploy:
  provider: script
  skip_cleanup: true
  script: ssh -i deploy_rsa ubuntu@18.218.152.78 'source /home/ubuntu/clashboard/scripts/deploy.sh'
```
