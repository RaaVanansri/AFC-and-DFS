from flask import Flask,render_template,request
import dfs
import os

tdwr = ["India","Russia","UK","US","Japan","China"]

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    channelno = [52,56,60,64,100,104,108,112,116,120,124,128,132,136,140,144,36,40,44,48,149,153,157,161,165,54,62,102,110,118,126,134,142,38,46,151,159,58,106,122,138,42,155,114,50]
    channelno.sort()
    if request.method == 'POST':
        ch = int(request.form.get('channel'))
        countrytd = request.form.get('country')
        ch = dfs.randint(ch,countrytd)
        return render_template('home.html',out=ch,channel=channelno,country=tdwr)
    return render_template('home.html',out='',channel=channelno,country=tdwr)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0',debug=True,port=port)