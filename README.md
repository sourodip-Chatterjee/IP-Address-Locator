# 🌐 IP Address Locator

A simple Python script to fetch geolocation details for any manually entered IP address using the `ipinfo.io` API.

## 📊 Features

* Input any IPv4 or IPv6 address manually.
* Retrieves location data including:

  * IP Address
  * City
  * Region
  * Country
  * Latitude & Longitude
  * ISP / Organization

## 🚀 How It Works

This script makes a GET request to `https://ipinfo.io/<ip>/json`, parses the JSON response, and prints the location details of the entered IP address.

## 🛠️ Requirements

* Python 3.x
* `requests` library (install via pip if not installed)

```bash
pip install requests
```

## 🔧 Usage

```bash
python ip_locator.py
```

Then, enter an IP address when prompted:

```bash
Enter an IP address: 8.8.8.8
```

Sample Output:

```
IP Address: 8.8.8.8
City: Mountain View
Region: California
Country: US
Location (Lat,Long): 37.4056,-122.0775
ISP: AS15169 Google LLC
```

## 💼 Files to Include in GitHub Repo

| File               | Purpose                                          |
| ------------------ | ------------------------------------------------ |
| `ip_locator.py`    | The main Python script                           |
| `README.md`        | Project documentation (this file)                |
| `.gitignore`       | Exclude unnecessary files                        |
| `requirements.txt` | Dependency list (for reproducibility)            |


## 📉 License

This project is licensed under the MIT License. Contributions welcome!

---

Made with ❤️ using Python & IPinfo API
