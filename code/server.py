from flask import Flask,redirect,url_for, render_template,request
import sys
import requests
import DH, SDES
n=90
enc_session={"status":False,"p":0,'z':[],"g":0,"a":0,"y":0,"k":0,"key_dec":0,"key_bin":"","p_q":0}
home={"name":"","port":""}
connected={"status":"","port":"","user":""}
d_port=""
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    global port
    name=request.form.get('name')
    home['name']=name
    home['port']=port
    return render_template('apply.html', server=home['port'], name=home['name'] )

@app.route('/search', methods=['POST'])
def search():
    global home
    global d_port
    d_port=request.form.get('port')
    payload={'message':'connection_request','port':home["port"]}
    r=requests.post(f'http://127.0.0.1:{d_port}/connection',data=payload)
    r1=r.json()
    return render_template('communicate.html', user=r1['name'], port=r1['port'] )
    
@app.route('/connection', methods=['POST'])
def connection():
    message=request.form.get('message')
    return home

@app.route('/message',methods=['POST'])
def message():
    global n
    global d_port
    global enc_session
    if not enc_session["status"]:
        key=DH.DH(n)
        key.g_calculator()
        key.secret_number_generattor()
        enc_session['p']=key.p
        enc_session['g']=key.g 
        enc_session['a']=key.a 
        enc_session['y']=key.ya 
        enc_session['p_q']=key.q_times_p
        payload={'status':True,'p':enc_session['p'],'g':enc_session['g'],'y':enc_session['y'],'p_q':enc_session['p_q']}
        r=requests.post(f'http://127.0.0.1:{d_port}/setparam',data=payload)
        if r==500:
            return f"Error in receiving data from port {d_port} occured"
        r1=r.json()
        key.yb=r1['yb']
        key.k_generator()
        key.bss()
        enc_session['k']=key.k
        enc_session['key_dec']=key.f_k_dec
        enc_session['key_bin']=key.f_k_bin
        enc_session['status']=True
        return enc_session
    return enc_session
@app.route('/setparam',methods=["POST"])
def setparam():
    global enc_session
    key=DH.DH(n)
    d=request.form.to_dict()
    enc_session['status']=True  
    key.p=int(d['p'])
    key.g=int(d['g'])
    key.secret_number_generattor()
    key.yb=int(d['y'])
    key.k_generator()
    key.q_times_p=int(d['p_q'])
    key.bss()
    enc_session['k']=key.k
    enc_session['p']=key.p
    enc_session['g']=key.g
    enc_session['a']=key.a
    enc_session['y']=key.ya
    enc_session['key_dec']=key.f_k_dec
    enc_session['key_bin']=key.f_k_bin
    enc_session['p_q']=key.q_times_p
    return {'yb':key.ya}
if __name__ == "__main__":
    global port
    port=False
    if len(sys.argv)<2:
        while not port:
            port=input("enter port:")
    else:
        port=sys.argv[1]
    app.run('127.0.0.1',port,debug=True)