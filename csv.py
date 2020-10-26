import requests

f = requests.get("https://raw.githubusercontent.com/gadzygadz/Networking_Presentation/main/example.csv").text.split("\n")

for i in f:
    print(i)