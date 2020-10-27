import requests
import socket
alt = "Jake you absolute buffoon you forgot to check the Laptop IP address"
ip = requests.get('https://api.ipify.org').text
hostname = socket.gethostname()

with open(f"../Data/{hostname}.ip", "w+") as f:
    f.write(ip)

if hostname == "bluemoon":
    from os import system
    system("git add -A")
    system('git commit -m "pushing IP"')
    system("git push")
