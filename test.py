import socketio


sio = socketio.Server()
app = socketio.WSGIApp(sio)

import eventlet
eventlet.wsgi.server(eventlet.listen(('', 12000)), app)



sio.emit('my event', {'data': 'foobar'})

