from flask import Flask
from flask import request, redirect, url_for

app = Flask(__name__)

@app.route('/page1')
def page1():
     resp = redirect(url_for('page2'))
     resp.headers['Content-Type'] = 'application/commcare'
     return resp

@app.route('/page2')
def page2():
    return 'Hello, World'