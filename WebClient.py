from websocket import create_connection
# 通过socket路由访问
ws = create_connection("ws://localhost:5000/echo")
ws.send("Hello, linyk3")
result = ws.recv()
print(result)
ws.close()