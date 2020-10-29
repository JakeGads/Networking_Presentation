from config import app

@app.route('/')
def hello():
    return "<h1>Hello World</h1>"