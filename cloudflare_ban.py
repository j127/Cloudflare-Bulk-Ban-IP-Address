import os
import json
import time
import logging
import requests
import cf_settings

# Allow changing of environment variable names -- for later
CF_API_TOKEN = "CF_API_TOKEN"
CF_EMAIL_ADDRESS = "CF_EMAIL_ADDRESS"

# Temporary
api_token = cf_settings.api_token
api_email_address = cf_settings.api_email_address

# Configure logfile
logging.basicConfig(filename="cloudflare_bans.log", format="%(asctime)s\t%(levelname)s:\t%(message)s", level=logging.INFO)

def get_api_credentials():
    """Check if API credentials are saved in environment variables."""

    api_token = os.environ.get[CF_API_TOKEN]
    api_email_address = os.environ.get[CF_EMAIL_ADDRESS]

def save_api_tokens(save_status):
    """A way to save API credentials as environment variables on servers."""
    pass

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
    print("Printing response: ", response)
    response_dict = json.loads(response)
    if response_dict["result"] != "success":
        logging.warning("Something went wrong with the response for ", response_dict["ip"])
    else:
        logging.info("Successfully banned IP")


def read_file_and_ban():
    f = open('banned_ips.txt')
    for line in f:
        print("About to ban: ", line.strip())
        post_to_cloudflare(api_token, api_email_address, "ban", line.strip())
        time.sleep(1)
    f.close()

# save_status = input("Do you want to save your API credentials as environment variables? [y/N]")
# save_api_tokens(save_status)
# if "y" in save_status.lower():
# save_api_tokens()
