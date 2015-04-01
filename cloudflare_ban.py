import os
import json
import time
import logging
import requests
import cf_settings

# Get the API credentials from cf_settings.py
api_token = cf_settings.api_token
api_email_address = cf_settings.api_email_address

# Configure logfile -- comment this out if you don't want a logfile
logging.basicConfig(filename="cloudflare_bans.log", format="%(asctime)s\t%(levelname)s:\t%(message)s", level=logging.INFO)

def post_to_cloudflare(api_token, api_email_address, action, ip_address):                     
    """Post the the Cloudflare API.
    
    Don't post more than 1,200 times in five minutes.

    tkn -- API token
    email -- the email address associated with the Cloudflare account
    a -- action can be whitelist ("wl"), ban ("ban"), or remove ("nul")
    key -- the IP address to act on
    
    """
    payload = {
        "tkn": api_token,
        "email": api_email_address,
        "a": action,
        "key": ip_address
    }

    r = requests.post("https://www.cloudflare.com/api_json.html", data=payload)
    response = r.text
    response_dict = json.loads(response)
    print("Printing response: ", response)

    if response_dict["result"] != "success":
        logging.warning("Something went wrong with the response for ", response_dict["ip"])
    else:
        logging.info("Successfully banned IP", response_dict["ip"])

def read_file_and_ban():
    f = open('banned_ips.txt')
    for line in f:
        cleaned_line = line.strip()
        print("About to ban: ", cleaned_line)
        post_to_cloudflare(api_token, api_email_address, "ban", cleaned_line)
        time.sleep(0.5) # ensure that it stays under 1,200 requests in five minutes. This limits it to 600.
    f.close()

