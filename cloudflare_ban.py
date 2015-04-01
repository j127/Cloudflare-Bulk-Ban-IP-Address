import os
import logging
import requests

api_token_variable_name = "CF_API_TOKEN"
api_email_address_variable_name = "CF_EMAIL_ADDRESS"

# Move to end
save_status = input("Do you want to save API credentials as environment variables?")
save_api_tokens(save_status)

def get_api_credentials():
    """Check if API credentials are saved in environment variables."""

    api_token = os.environ[api_token_variable_name]
    api_email_address = os.environ[api_email_address_variable_name]

def save_api_tokens(save_status):
    """A way to save API credentials as environment variables on servers."""

    if "y" in save_status.lower():
        save_api_tokens()


def post_to_cloudflare(api_token, api_email_address, action, ip_address):                     
    """Post the the Cloudflare API.

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
    print(r.text)

def read_file():
    f = open('banned_ips.txt')
    for line in f:
        print f

