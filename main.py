from flask import Flask, render_template
import pandas as pd 

# DATA!!

# Characters

# Giftable Characters


# abandoned House 
#abandoned_house_hats = 



app = Flask(__name__)

@app.route("/")
@app.route("/home/")
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port = 1234, debug=True)

