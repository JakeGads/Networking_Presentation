import requests
import socket
alt = "Jake you absolute buffoon you forgot to check the Laptop IP address"
ip = requests.get('https://api.ipify.org').text
hostname = socket.gethostname()