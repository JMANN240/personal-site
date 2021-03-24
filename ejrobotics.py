from flask import Flask, render_template, redirect
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = '\xfd{H\xe5<\x95\xf9\xe3\x96.5\xd1\x01O<!\xd5\xa2\xa0\x9fR"\xa1\xa8'

data_file = "/var/www/ejrobotics/data.json"

def loadData():
    with open(data_file, "r") as file:
        return json.load(file)

def saveData(obj):
    with open(data_file, "w") as file:
        json.dump(obj, file, sort_keys=False, indent=4)

@app.route("/")
def index():
    data = loadData()
    return render_template('index.html', sites=data["sites"], jobs=data["jobs"])

@app.route("/sites/<string:site>")
def sites(site):
    data = loadData()
    return redirect(data["sites"][site]["url"])

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8100, debug=True)