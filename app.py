from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>welcome to urban cafe trail</p><p>transport mode <select><option>bike/car/pedestrian-friendly</option></select></p><p>heure douverture <input name=\"cafeopentime\" type=\"time\"/></p>"
