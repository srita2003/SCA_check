import requests
import flask

app = flask.Flask(__name__)

@app.route("/")
def home():
    return "Python SCA Scan Project Running"

if __name__ == "__main__":
    app.run(debug=True)