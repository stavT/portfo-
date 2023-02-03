
from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def hello_world():
    print(url_for('static',filename='me.ico'))
    return render_template('index.html')

@app.route("/about.html")
def about():
    print(url_for('static',filename='abs.ico'))
    return render_template('about.html')

@app.route("/contact.html")
def contact():
    print(url_for('static',filename='phone.ico'))
    return render_template('contact.html')

    
# @app.route("/info")
# def info():
#     return "<p>My name is Stav Tsechanky</p>"

