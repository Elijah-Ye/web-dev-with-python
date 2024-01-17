from flask import Flask

app = Flask(__name__)


# @ is called declarative python
# route is what comes after the main url i.e. /people /job /...
@app.route("/")
def hello_world():
  return "<p>Hello, Jovian!</p>"


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
