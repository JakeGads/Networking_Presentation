from config import app
import requests
import json

@app.route('/')
def hello():
    return "<h1>Hello World</h1>"

class db:
    def __init__(self, src) -> None:
        self.src = json.loads(
                requests.get().text
        )