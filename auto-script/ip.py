import requests

def get_public_ip_address():
    try:
        response = requests.get('https://api.ipify.org')
        ip_address = response.text
    except requests.RequestException:
        ip_address = 'Unable to get IP address'
    return ip_address

print("Public IP Address:", get_public_ip_address())