import os

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello_world():
  """Example Hello World route."""
  name = os.environ.get("NAME", "World")
  return f"Hello {name}!"

@app.route("/postdata", methods = ['POST'])
def postdata():
  if request.method == 'POST':
    print("POSTER")
    print(request.form['eventType'])
  return "OK"

if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 3000)))