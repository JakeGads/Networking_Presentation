from flask import Flask, render_template, request
import socket
import ip

app = Flask(__name__)


count = 0
@app.route('/')
def hello():
    global count
    count += 1
    
    return f"""<h1>Hello Visitor #{count}!</h1>
    <h3>connect by going to {ip.ip}:5000</h3>
    <h3>alt-connect: {ip.alt}
    <br><br>
    <ul>
        <li>"<a href={{ url_for('Phanatic', num='{count}') }}"Phillies</a></li>
        <li><a href="/FLY">Eagles</a></li>
        <li><a href="/DoGgOs">Dogs</a></li>
    </ul> 
    """

app.route("Phillies")
def Phanatic(num=0):
    if num == 0:
        request.args.get('num', 1)

    return render_template("template1", title="Phillies", num=num)

app.route("fly")
def E_A_G_L_E_S(num=0):
    if num == 0:
        request.args.get('num', 1)

    return render_template("template2", title="Eagles", num=num)

app.route("doggos")
def dogs(num=0):
    if num == 0:
        request.args.get('num', 1)
    return render_template("template3", title="Dogs", num=num)


if __name__ == '__main__':
    app.run(debug=True)

