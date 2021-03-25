from flask_socketio import SocketIO

SOCKET = SocketIO(cors_allowed_origins="*", async_mode="eventlet")