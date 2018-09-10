[简书:20180905:Python flask-sockets](https://www.jianshu.com/p/ad79148f4c11)

今天来学习使用Python中的 flask 和 flask_sockets 来搭建一个简单的Server-Client 服务。

## Server 端
首先是Flask-Sockets  [官网](https://pypi.org/project/Flask-Sockets/)，还有 [Github](https://github.com/heroku-python/flask-sockets) 
官方对Flask-Sockets 的介绍十分简单：
       Project description
       Elegant WebSockets for your Flask apps.
Flask-Sockets是Flask框架的一个扩展，通过它，Flask应用程序可以优雅地使用WebSocket服务。
**注意：[Flask-Sockets](https://github.com/kennethreitz/flask-sockets)和[Flask-SocketIO](https://github.com/miguelgrinberg/Flask-SocketIO)是两个不同的Flask扩展库**
Flask-Sockets 仅仅将WebSocket协议进行包装，只能使用WebSocket服务；
Flask-SocketIO 不仅包装了WebSocket协议，很可以实现其他更多的功能。

开始运行程序前，需要安装Python的两个库： ```flask``` 和 ```flask-sockets```：
安装命令：
```pip install flask```
![image.png](https://upload-images.jianshu.io/upload_images/2833964-9f465eff0871692e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

```pip install flask-sockets```
![image.png](https://upload-images.jianshu.io/upload_images/2833964-682d048ae2876a78.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

然后按照github上面的demo就可以创建一个server了：
```
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


if __name__ == "__main__":
    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler
    server = pywsgi.WSGIServer(('', 5000), app, handler_class=WebSocketHandler)
    print("web server start ... ")
    server.serve_forever()
```

执行这个python程序就可以启动server了
![image.png](https://upload-images.jianshu.io/upload_images/2833964-016327b1335f6850.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

在浏览器输入：```http://localhost:5000/``` 就可以访问 根路由 "/" 了，返回的消息是'Hello World!'
![image.png](https://upload-images.jianshu.io/upload_images/2833964-d1bcba313f96c834.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

这样就可以验证Server端正常运行了。


## Client 端
Client 端 通过 ```websocket-client``` 这个库也可以非常简单的实现
```
from websocket import create_connection
# 通过socket路由访问
ws = create_connection("ws://localhost:5000/echo")
ws.send("Hello, linyk3")
result = ws.recv()
print(result)
ws.close()
```
上面代码中`import`的是 `webcket`, 但是在pip安装Python库的时候，如果是安装 `websocket`，会提示报错：
![image.png](https://upload-images.jianshu.io/upload_images/2833964-18f027c38aaa6119.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![image.png](https://upload-images.jianshu.io/upload_images/2833964-ca0d18000217b039.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

实际上需要安装的是 `websocket-client`
![image.png](https://upload-images.jianshu.io/upload_images/2833964-f45750bacf99859b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![image.png](https://upload-images.jianshu.io/upload_images/2833964-f41f8471d5ad1418.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

当Server端正常运行是，实现Client程序，通过结果可以知道Server-Client两端的交互是通的：
![image.png](https://upload-images.jianshu.io/upload_images/2833964-cdf0cf42b254ab6b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)






今天来学习使用Python中的 flask 和 flask_sockets 来搭建一个简单的Server-Client 服务。

## Server 端
首先是Flask-Sockets  [官网](https://pypi.org/project/Flask-Sockets/)，还有 [Github](https://github.com/heroku-python/flask-sockets) 
官方对Flask-Sockets 的介绍十分简单：
       Project description
       Elegant WebSockets for your Flask apps.
Flask-Sockets是Flask框架的一个扩展，通过它，Flask应用程序可以优雅地使用WebSocket服务。
**注意：[Flask-Sockets](https://github.com/kennethreitz/flask-sockets)和[Flask-SocketIO](https://github.com/miguelgrinberg/Flask-SocketIO)是两个不同的Flask扩展库**
Flask-Sockets 仅仅将WebSocket协议进行包装，只能使用WebSocket服务；
Flask-SocketIO 不仅包装了WebSocket协议，很可以实现其他更多的功能。

开始运行程序前，需要安装Python的两个库： ```flask``` 和 ```flask-sockets```：
安装命令：
```pip install flask```
![image.png](https://upload-images.jianshu.io/upload_images/2833964-9f465eff0871692e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

```pip install flask-sockets```
![image.png](https://upload-images.jianshu.io/upload_images/2833964-682d048ae2876a78.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

然后按照github上面的demo就可以创建一个server了：
```
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


if __name__ == "__main__":
    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler
    server = pywsgi.WSGIServer(('', 5000), app, handler_class=WebSocketHandler)
    print("web server start ... ")
    server.serve_forever()
```

执行这个python程序就可以启动server了
![image.png](https://upload-images.jianshu.io/upload_images/2833964-016327b1335f6850.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

在浏览器输入：```http://localhost:5000/``` 就可以访问 根路由 "/" 了，返回的消息是'Hello World!'
![image.png](https://upload-images.jianshu.io/upload_images/2833964-d1bcba313f96c834.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

这样就可以验证Server端正常运行了。


## Client 端
Client 端 通过 ```websocket-client``` 这个库也可以非常简单的实现
```
from websocket import create_connection
# 通过socket路由访问
ws = create_connection("ws://localhost:5000/echo")
ws.send("Hello, linyk3")
result = ws.recv()
print(result)
ws.close()
```
上面代码中`import`的是 `webcket`, 但是在pip安装Python库的时候，如果是安装 `websocket`，会提示报错：
![image.png](https://upload-images.jianshu.io/upload_images/2833964-18f027c38aaa6119.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![image.png](https://upload-images.jianshu.io/upload_images/2833964-ca0d18000217b039.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

实际上需要安装的是 `websocket-client`
![image.png](https://upload-images.jianshu.io/upload_images/2833964-f45750bacf99859b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![image.png](https://upload-images.jianshu.io/upload_images/2833964-f41f8471d5ad1418.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

当Server端正常运行是，实现Client程序，通过结果可以知道Server-Client两端的交互是通的：
![image.png](https://upload-images.jianshu.io/upload_images/2833964-cdf0cf42b254ab6b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)







