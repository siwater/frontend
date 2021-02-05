from flask import Flask, render_template, jsonify

import os
import requests
import sys

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    msg = "Hello from the front end"
    url = "http://{server}:{port}/message".format(server=backend_server, port=backend_port)
    response = requests.get(url)
    data = response.json()
    return render_template("index.html", title="Front End", message=data['message'])

if __name__ == "__main__":
    listen_port = os.environ.get('LISTEN_PORT')
    if listen_port == None:
        sys.exit('LISTEN_PORT undefined')

    backend_server = os.environ.get('BACKEND_SERVER')
    backend_port = os.environ.get('BACKEND_PORT')

    if backend_server == None or backend_port == None:
        sys.exit("BACKEND_SERVER or BACKEND_PORT undefined")
    app.run(host='0.0.0.0', port=listen_port)
