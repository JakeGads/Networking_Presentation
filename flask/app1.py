from flask import Flask, render_template, request, url_for
import requests
import json
import const_ip as ip

app = Flask(__name__)


count = 0

@app.route("/phils/<num>")
def phillies(num=1):
    
    object = requests.get("https://raw.githubusercontent.com/gadzygadz/Networking_Presentation/main/Data/phillies.json")
    object = json.loads(object.text)
    index = (int(num) % len(object)) + 1
    object = object[str(index)]

    return f"<h1>{index} We in Philly baby</h1>"
    # return render_template("template1", title="Phillies", num=num, phil=object)

@app.route("/fly/<num>")
def eagle(num=1):
    if num == 0:
        num = request.args.get('num', 1)

    object = requests.get("https://raw.githubusercontent.com/gadzygadz/Networking_Presentation/main/Data/eagles.json")
    object = json.loads(object.text)
    index = (int(num) % len(object)) + 1
    object = object[str(index)]

    return render_template("template2", title="Eagles", num=num, eagle=object)

@app.route("/doggo/<num>")
def dogs(num=1):
    object = requests.get("https://raw.githubusercontent.com/gadzygadz/Networking_Presentation/main/Data/dogs.json")
    object = json.loads(object.text)
    index = (int(num) % len(object)) + 1
    object = object[str(index)]

    return render_template("template3", title="Dogs", num=num, dog=object)


@app.route('/')
def hello():
    global count
    count += 1
    link = url_for('phillies', num=count)
    
    return f"""<h1>Hello Visitor #{count}!</h1>
    <h3>connect by going to {ip.ip}:5000</h3>
    <h3>alt-connect: {ip.alt}
    <br><br>
    <ul>
        <li><a href="{url_for('phillies', num=count)}">Phillies</a></li>
        <li><a href="{url_for('eagle', num=count)}">Eagles</a></li>
        <li><a href="{url_for('dogs', num=count)}">Dogs</a></li>
    </ul> 
    """

if __name__ == '__main__':
    # app.run()
    app.run(debug=True)

