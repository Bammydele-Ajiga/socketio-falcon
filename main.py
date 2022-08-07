import socket
from datetime import datetime
import socketio
user  = ["bams","peace","love"]
sio = socketio.Server()
app = socketio.WSGIApp(sio, static_files={
    "/": "./public/"

}
 )
def cb(data):
    print(data)

# def task(sid):
#     sio.sleep(5)
#     sio.emit("mult", {"numbers":[3,4]}, callback=cb)

@sio.event
def connect(sid, environ):
    print(sid ,"connected")
    # sio.start_background_task(task,sid)

@sio.event
def disconnect(sid):
    print(sid, "disconnected")

@sio.event
def progress(sid,data):
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    result = {"id": "", "progress": "", "time": ""}
    if data["id"] in user:
        if data["id"] == "bams":
            result["id"] = "bams"
            result["progress"] = "90%"
            result["time"] = current_time
        elif data["id"] == "peace":
            result["id"] = "peace"
            result["progress"] = "85%"
            result["time"] = current_time
        elif data["id"] == "love":
            result["id"] = "love"
            result["progress"] = "100%"
            result["time"] = current_time
    else:
        result["id"] = "User not found"
            # sio.emit("sum_result",{"result":result}, to= sid )
    print(result)

    return result

