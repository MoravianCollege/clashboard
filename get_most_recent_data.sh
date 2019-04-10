#!/usr/bin/env bash

current_date=$(date +%Y%m%d)
url="https://aact.ctti-clinicaltrials.org/static/static_db_copies/daily/${current_date}_clinical_trials.zip"
response=$(curl -sL -w "%{http_code}" -I ${url} -o /dev/null)

echo "Searching for update for today ($(date +%m-%d-%Y))..."
if [[ ${response} = '200' ]]; then
    echo "Most recent data found."
    results=$(wget ${url})
else
    echo "No update for today."
fi
