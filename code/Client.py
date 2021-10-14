import requests
""" sample=a.DH(90)
sample.g_calculator()
sample.secret_number_generattor()
sample.bss() """
payload={'name':'bob','from':'80'}
r=requests.post('http://127.0.0.1:5000/message',data=payload)
r1=r.json()
print(r1)