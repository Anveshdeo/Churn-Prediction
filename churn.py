# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 11:34:45 2021

@author: Anvesh
"""

from flask import Flask,request,render_template
import joblib
model=joblib.load('lrChurnModel.save')
trans=joblib.load('project_scalar.save')

app=Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/y_predict',methods=['POST'])
def y_predict():
    p=request.form["tenure"]
    q=request.form["Gender"]
    if (q=='Female'):
        q=0
    if (q=='Male'):
        q=1
    r=request.form["SeniorCitizen"]
    if (r=='0'):
        r1,r2=1,0
    if (r=='1'):
        r1,r2=0,1
    s=request.form["Partner"]
    if (s=='Yes'):
        s1,s2=1,0
    if (s=='No'):
        s1,s2=0,1
    t=request.form["Dependents"]
    if (t=='Yes'):
        t1,t2=1,0
    if (t=='No'):
        t1,t2=0,1
    u=request.form["PhoneService"]
    if (u=='Yes'):
        u1,u2=1,0
    if (u=='No'):
        u1,u2=0,1
    v=request.form["InternetService"]
    if (v=='DSL'):
        v=0
    if (v=='Fiber optic'):
        v=1
    if (v=='No'):
        v=2
    w=request.form["OnlineSecurity"]
    if (w=='Yes'):
        w1,w2,w3=1,0,0
    if (w=='No'):
        w1,w2,w3=0,1,0
    if (w=='No internet service'):
        w1,w2,w3=0,0,1
    x=request.form["OnlineBackup"]
    if (x=='Yes'):
        x1,x2,x3=1,0,0
    if (x=='No'):
        x1,x2,x3=0,1,0
    if (x=='No internet service'):
        x1,x2,x3=0,0,1
    y=request.form["OnlineBackup"]
    if (y=='Yes'):
        y1,y2,y3=1,0,0
    if (y=='No'):
        y1,y2,y3=0,1,0
    if (y=='No internet service'):
        y1,y2,y3=0,0,1
    z=request.form["Contract"]
    if (z=='Month-to-month'):
        z1,z2,z3=1,0,0
    if (z=='One year Contract'):
        z1,z2,z3=0,1,0
    if (z=='Two year'):
        z1,z2,z3=0,0,1
    o=request.form["PaperlessBilling"]
    if (o=='Yes'):
        o1,o2=1,0
    if (o=='No'):
        o1,o2=0,1
    n=request.form["PaymentMethod"]
    if (n=='Electronic check'):
        n1,n2,n3,n4=1,0,0,0
    if (n=='Mailed check'):
        n1,n2,n3,n4=0,1,0,0
    if (n=='Bank transfer (automatic)'):
         n1,n2,n3,n4=0,0,1,0
    if (n=='Credit card (automatic)'):
         n1,n2,n3,n4=0,0,0,1
    
    
    k=[[int(p),int(o1),int(o2),int(q),int(r1),int(r2),int(s1),int(s2),int(u1),int(u2),int(t1),int(t2),int(v),int(w1),int(w2),int(w3),int(x1),int(x2),int(x3),int(y1),int(y2),int(y3),int(z1),int(z2),int(z3),int(n1),int(n2),int(n3),int(n4)]]
    k=trans.transform(k)
    a=model.predict(k)
    if (a[0]==1):
        b='Customer is LIKELY to churn'
    else: b='Customer is NOT LIKELY to churn'
    return render_template('index.html',prediction_text='Output : {}'.format(b))
    

if __name__=='__main__':
    app.run(debug=True)
        
    
