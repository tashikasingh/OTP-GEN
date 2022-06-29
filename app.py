from flask import Flask, render_template, request,redirect
import os
import otpgenerator as og
import re

regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

generated=''
name=''
emailid=''
app=Flask(__name__)

picfolder = os.path.join('static','pics')
#ssfolder=os.path.join('static', 'css')
app.config['UPLOAD_FOLDER']=picfolder
@app.route("/")
@app.route("/home")
def home():
    im=os.path.join(app.config['UPLOAD_FOLDER'],'mobile.png')
    return render_template("base.html",image=im,error='')
    
def checkemail(emailid):
    if re.fullmatch(regex, emailid):
        return True
    else:
      return False

@app.route("/index", methods=["GET","POST"])
def index():
    im=os.path.join(app.config['UPLOAD_FOLDER'],'mobile.png')
    output=request.form.to_dict()
    namee=output["name"]
    namee=namee[0:namee.find(" ")]
    og.name=namee
    emailid=output["email"]
    og.id=emailid
    if not checkemail(emailid):
        return render_template("base.html",image=im,error='Wrong email format')
    generated=og.generate()
    og.generated=generated
    msg=og.establisconn(namee,emailid,generated)
    og.send(msg,emailid)
    return render_template("index.html",image=im,id=emailid, name=namee)     

@app.route("/resend", methods=["GET","POST"])
def resend():
    im=os.path.join(app.config['UPLOAD_FOLDER'],'mobile.png')
    namee=og.name
    emailid=og.id
    generated=og.generate()
    og.generated=generated
    msg=og.establisconn(namee,emailid,generated)
    og.send(msg,emailid)
    return render_template("index.html",image=im,id=emailid, name=namee) 

@app.route("/result", methods=["GET","POST"])
def result():
    im=os.path.join(app.config['UPLOAD_FOLDER'],'mobile.png')
    output=request.form.to_dict()
    thisotp=output['otp']
    if thisotp==og.generated:
        return render_template("success.html",)
    else:
        return render_template("index.html", image=im,failed='s')


if __name__ == '__main__':
    app.run(debug=True,port=5000)