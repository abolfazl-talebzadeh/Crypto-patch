from os import name
from flask import Flask,redirect,url_for, render_template,request
def spl(data):
    temp=''
    res=[]
    for i in range(0, len(data), 8):
        temp=data[i:i+8]
        res.append(temp)
    return res

def bin_to_int(k):
        result=0
        g=0
        for i in range(len(k)-1,-1,-1):
            a=((len(k)-1)-i)
            g=2**(int(i))*int(k[a])
            result+=g
        return result
    

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/cal_data', methods=['GET'])
def cal_data():
    k1="1111101010"
    k2="0101011111"
    temp=""
    a=request.args.get(key="name")
    o=spl(a)

if __name__=="__main__":
    app.run(debug=True)
