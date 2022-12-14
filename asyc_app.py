import socket
import socketio


sio = socketio.AsyncServer(async_mode =  "asgi")

app = socketio.ASGIApp(sio, static_files={
    "/": "./public/"
}
            )

@sio.event
async def connect(sid, environ):
    print(sid ,"connected")
    pass

@sio.event
async def disconnect(sid):
    print(sid, "disconnected")
    pass
