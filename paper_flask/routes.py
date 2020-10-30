from config import app
from flask import render_template
import requests
import json
import sys

@app.route('/')
def hello():
    return "<h1>Hello World</h1>"

class db_connect:
    def __init__(self, src) -> None:
        self.src = json.loads(
                requests.get("https://raw.githubusercontent.com/gadzygadz/Networking_Presentation/main/Data/user.json").text
        )
    def get(self, pointless, id):
        # because I'm not checking we are just gonna pull the closest
        min_dif = sys.maxsize 
        r = self.src[0]
        for i in self.src:
            val = 0
            for c in i["_id"]:
                val += ord(c)
            
            if abs((val - id)) < min_dif:
                r = i
        
        return r

db = db_connect()

@app.route("/user_profile/<id>")
def user_profile(id=''):
  return render_template("user_information.html", user=db.get('user', id))