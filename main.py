from wsgiref import simple_server
import os
from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return 'Hello world trail'

port = int(os.getenv("PORT",5001))

if __name__ == "__main__":
    app.run(port=5001)
    host = '0.0.0.0'

    httpd = simple_server.make_server(host=host, port=port, app=app)
    httpd.serve_forever()
