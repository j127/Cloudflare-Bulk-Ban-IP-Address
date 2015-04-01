# Cloudflare IP Address Banning

*WARNING:* Do not use this script unless you know exactly what it does! It is just a rough sketch that isn't finished.

## About

This simple Python 3 script bans spammer IP addresses in bulk by reporting them to [Cloudflare's API](https://www.cloudflare.com/docs/client-api.html). It was written on Ubuntu 14.10.

It reads from a text file that contains a list of IP addresses, one per line. ~~It logs results to a text file.~~

For now, this is just designed to bulk-ban IP addresses on Cloudflare. Maybe later it will have more functionality.

## Usage

1. Navigate to the directory where the script is.
2. Put IP addresses in a file called banned_ips.txt, one per line
3. Put API credentials into cf_settings.py. See the cf_settings.example.py file for an example.
4. Type `python3` to start Python
5. Import the code: `import cloudflare_ban`
6. Run the function: `cloudflare_ban.read_file_and_ban()`
7. The script will write output to the screen.
8. Check [Cloudflare](https://www.cloudflare.com/threat-control) to see the banned IPs.

