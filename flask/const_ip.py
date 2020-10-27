import requests
import socket
alt = requests.get("https://raw.githubusercontent.com/gadzygadz/Networking_Presentation/main/Data/bluemoon.ip").text
ip = requests.get('https://api.ipify.org').text
hostname = socket.gethostname()

with open(f"../Data/{hostname}.ip", "w+") as f:
    f.write(ip)

# only fires if on laptop
if hostname == "bluemoon":
    from os import system
    system("git add -A")
    system('git commit -m "pushing IP"')
    system("git push")
