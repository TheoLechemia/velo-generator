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
    usb_power_production = serial.Serial(app.config["USB_PRODUCTION_MOUNT_POINT"])
    usb_power_demand = serial.Serial(app.config["USB_DEMAND_MOUNT_POINT"])
except serial.SerialException as e:
    print("""
        One of the required USB device not found
    """)
    print(e)
    raise


def get_power_from_usb():
    while not thread_stop_event.is_set():
        number = round(random()*1000, 3)
        # get value from usb
        production = usb_power_production.readline()
        demand = usb_power_demand.readline()
        decoded_production = production.decode('utf-8').rstrip()
        decoded_demand = demand.decode('utf-8').rstrip()
        # power_tab = decoded_val.split(',')
        socket_.emit('production', {'list': decoded_production})
        socket_.emit('demand', {'list': decoded_demand})
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
    Timer(1, open_browser).start()
    socket_.run(app, debug=True, port="5006")
