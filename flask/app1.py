from flask import Flask, render_template, request
import requests
import json
import ip

app = Flask(__name__)


count = 0
@app.route('/')
def hello():
    global count
    num = request.args.get('num', 0)
    if num == 0:
        count += 1
        num = count
    
    return f"""<h1>Hello Visitor #{num}!</h1>
    <h3>connect by going to {ip.ip}:5000</h3>
    <h3>alt-connect: {ip.alt}
    <br><br>
    <ul>
        <li>"<a href={{ url_for('Phanatic', num='{count}') }}"Phillies</a></li>
        <li><a href="{{ url_for('E_A_G_L_E_S', num='{count}') }}">Eagles</a></li>
        <li><a href="{{ url_for('dogs', num='{count}') }}">Dogs</a></li>
    </ul> 
    """

app.route("Phillies")
def Phanatic(num=0):
    if num == 0:
        num = request.args.get('num', 1)

    object = json.loads(requests.get("https://raw.githubusercontent.com/gadzygadz/Networking_Presentation/main/Data/phillies.json").text)

    object = object[num % len(object)]

    return render_template("template1", title="Phillies", num=num, phil=object)

app.route("fly")
def E_A_G_L_E_S(num=0):
    if num == 0:
        num = request.args.get('num', 1)

    object = json.loads(requests.get("https://raw.githubusercontent.com/gadzygadz/Networking_Presentation/main/Data/eagles.json").text)

    object = object[num % len(object)]


    return render_template("template2", title="Eagles", num=num, eagle=object)

app.route("doggos")
def dogs(num=0):
    if num == 0:
        num = request.args.get('num', 1)

    object = json.loads(requests.get("https://raw.githubusercontent.com/gadzygadz/Networking_Presentation/main/Data/dogs.json").text)

    object = object[num % len(object)]


    return render_template("template3", title="Dogs", num=num)


if __name__ == '__main__':
    app.run(debug=True)

