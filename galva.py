# Musu Flask serveris
from flask import Flask
from flask import request
from flask import url_for
from flask import render_template
import funci
from funci import tr_per

app = Flask(__name__)

@app.route('/',methods=['GET'])
def root():
    aa = str(request.args.get('a',default='0.',type=str))
    bb = str(request.args.get('b',default='0.',type=str))
    cc = str(request.args.get('c',default='0.',type=str))
    
    rez = "Perimetrs=" + funci.tr_per(aa,bb,cc)
    return render_template("sveikaPasaule.html",vards="Trīsstūra parametri",rezultats=rez)



@app.route('/pogasall', methods=["GET"])
def pogasall():
    aa = request.args.get('a', default='0. ', type=str)
    bb = request.args.get('b', default='0. ', type=str)
    aa= "ievdita vertiba: " + aa

    aa1 = int(aa)
    bb1 = int(bb)
    b1=[]
    for k in range(aa1):
      for j in range(bb1):
        per = 2*(k+1+j+1)
        lauk = (k*1)*(j*1)
        rinda = "mala a= "
        rinda = rinda + aa + " mala b= " + bb +"; "
        rind = rinda + "perimetrs P="+str(per)
        rind = rinda + "Laukums S="+str(lauk)

        b1.append(rinda)
        



    return render_template("sveikaPasaule.html" ,vards="kontrol parbaude",rezultats=aa)

@app.route('/pogas')
def pogas():
  return render_template("pogas.html" ,vards="podzinas")



@app.route('/tests')
def health():
  return "Serveris darbojas Uh!"

if __name__ == '__main__':
  app.run()