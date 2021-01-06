# Musu Flask serveris
from flask import Flask
from flask import request
from flask import url_for
from flask import render_template
from funci import tr_per

app = Flask(__name__)

@app.route('/', methods=["GET"])
def root():
    aa = float(request.args.get('a',default='0.',type=str))
    bb = float(request.args.get('b',default='0.',type=str))
    cc = float(request.args.get('c',default='0.',type=str))
    rez = "perimetrs="+str(tr_per(aa,bb,cc))
    return rez



@app.route('/pogasall', methods=["GET"])
def pogasall():
    aa = request.args.get('a', default='0. ', type=str)
    aa= "ievdita vertiba: " + aa


    return render_template("sveikaPasaule.html" ,vards="kontrol parbaude",rezultats=aa)

@app.route('/pogas')
def pogas():
  return render_template("pogas.html" ,vards="podzinas")



@app.route('/tests')
def health():
  return "Serveris darbojas Uh!"

if __name__ == '__main__':
  app.run()