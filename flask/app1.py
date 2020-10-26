from flask import Flask, render_template
import socket
import ip

app = Flask(__name__)


count = 0
@app.route('/')
def hello():
    global count
    count += 1
    
    return f"""<h1>Hello You!</h1>
    <h2>visitor #{count}</h2>
    <h3>connect by going to {ip.ip}:5000</h3>
    <h3>alt-connect: {ip.alt}
    <br><br>
    <ul>
        <li><a href="/Phillies">Phillies</a></li>
        <li><a href="/FLY">Eagles</a></li>
        <li><a href="/DoGgOs">Dogs</a></li>
    </ul> 
    """

app.route("Phillies")
def Phanatic(num=0):
    return render_template("template1", title="Phillies", num=num)


if __name__ == '__main__':
    app.run(debug=True)

