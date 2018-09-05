from flask import Flask
from flask_sockets import Sockets


app = Flask(__name__)
sockets = Sockets(app)

# socket 路由，访问url是： ws://localhost:5000/echo
@sockets.route('/echo')
def echo_socket(ws):
    while not ws.closed:
        message = ws.receive()
        ws.send("come from web server: " + str(message))

# http 路由，访问url是： http://localhost:5000/
@app.route('/')
def hello():
    return 'Hello World!'


if __name__ == "__main__":
    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler
    server = pywsgi.WSGIServer(('', 5000), app, handler_class=WebSocketHandler)
    print("web server start ... ")
    server.serve_forever()