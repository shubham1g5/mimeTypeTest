from flask import Flask
from flask import request, redirect, url_for, make_response

app = Flask(__name__)

@app.route('/page1')
def page1():
     resp = redirect(url_for('page2'))
     resp.headers['content-type'] = 'application/commcare'
     return resp

@app.route('/page2')
def page2():
    resp = make_response('Hello, World')
    resp.headers['content-type'] = 'application/commcare'
    resp.headers['content-disposition'] = 'inline'
    return resp