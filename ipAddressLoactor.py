import requests

def get_location_by_ip(ip_address):
    url = f'https://ipinfo.io/{ip_address}/json'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print("IP Address:", data.get("ip"))
        print("City:", data.get("city"))
        print("Region:", data.get("region"))
        print("Country:", data.get("country"))
        print("Location (Lat,Long):", data.get("loc"))
        print("ISP:", data.get("org"))
    else:
        print("Error fetching location. Please check the IP address.")

# Ask user to input the IP address
ip_input = input("Enter an IP address: ")
get_location_by_ip(ip_input)
