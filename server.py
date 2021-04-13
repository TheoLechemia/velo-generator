import webbrowser
import serial
from random import random
from threading import Thread, Event, Timer
from flask import Flask, render_template
from flask_socketio import SocketIO

async_mode = 'eventlet'
app = Flask(__name__)
socket_ = SocketIO(app, async_mode=async_mode, logger=True, engineio_logger=True)
app.config.from_object('config')

thread = Thread()
thread_stop_event = Event()

try:
    usb_power_production1 = serial.Serial(app.config["USB_PRODUCTION_MOUNT_POINT"])
    usb_power_production2 = serial.Serial(app.config["USB_DEMAND_MOUNT_POINT"])
except serial.SerialException as e:
    print("""
        One of the required USB device not found
    """)
    print(e)
    raise

def parse_power(usb_stream:list):
    power_list = []
    for s in usb_stream:
        decode_stream = s.decode('utf-8').rstrip()
        print("OHHH", decode_stream)
        temp = decode_stream.split(";")
        if temp:
            temp.pop(0)
            production_str = temp[len(temp)-1]
            production_list = production_str.split(",")
            # remove last element
            production_list.pop(len(production_list) -1)
            # cast in float
            production_list = list(map(lambda x: float(x), production_list))
            power_list = [*power_list, *production_list]
    return power_list

def get_power_from_usb():
    while not thread_stop_event.is_set():
        # get value from usb
        production1 = usb_power_production1.readline()
        production2 = usb_power_production2.readline()
        result = parse_power([production1, production2])
        socket_.emit('production', {'list': result})
        socket_.sleep(1)



@app.route('/')
def index():
    return render_template('home.html', name="John", sync_mode=socket_.async_mode)

@socket_.on('connect')
def test_connect():
    print("Client connected")
    global thread
    if not thread.is_alive():
        print("start threading")
        thread = socket_.start_background_task(get_power_from_usb)


@socket_.on('disconnect')
def test_disconnect():
    print('Client disconnected')
    
def open_browser():
    webbrowser.open_new('127.0.0.1:5006')

if __name__ == '__main__':
    #Timer(1, open_browser).start()
    socket_.run(app, debug=True, port="5006")
