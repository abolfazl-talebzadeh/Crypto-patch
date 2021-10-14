from flask import Flask,redirect,url_for, render_template,request
import sys
import requests
connected={}
d_port=""
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    global port
    name=request.form.get('name')
    connected['name']=name
    connected['port']=port
    return render_template('apply.html', server=connected['port'], name=connected['name'] )

@app.route('/test', methods=['POST'])
def test():
    global port
    d_port=request.form.get('port')
    payload={'message':'connected Users','port':port}
    r=requests.post(f'http://127.0.0.1:{d_port}/message',data=payload)
    r1=r.json()
    return render_template('communicate.html', user=r1['name'], port=r1['port'] )


@app.route('/message', methods=['POST'])
def message():
    message=request.form.get('message')
    return connected


if __name__ == "__main__":
    global port
    port=False
    if len(sys.argv)<2:
        while not port:
            port=input("enter port:")
    else:
        port=sys.argv[1]
    app.run('127.0.0.1',port)