import math
import webbrowser
import serial
import json
from random import random
from threading import Thread, Event, Timer
from flask import Flask, render_template
from flask_socketio import SocketIO
from pymodbus.client.sync import ModbusSerialClient as ModbusClient


async_mode = 'eventlet'
app = Flask(__name__)
socket_ = SocketIO(app, async_mode=async_mode, logger=True, engineio_logger=True)
app.config.from_object('config')

thread = Thread()
thread_stop_event = Event()

try:
    usb_power_production1 = serial.Serial(app.config["USB_PRODUCTION_MOUNT_POINT_1"])
    usb_power_production2 = serial.Serial(app.config["USB_PRODUCTION_MOUNT_POINT_2"])
    client = ModbusClient(
        method = "rtu", 
        port=app.config["USB_DEMAND_MOUNT_POINT"], 
        stopbits = 1, 
        bytesize = 8, 
        parity = 'N', 
        baudrate = 9600
    )


except serial.SerialException as e:
    print("""
        One of the required USB device not found
    """)
    print(e)
    raise


def calc (registers, factor):
    format = '%%0.%df' % int (math.ceil (math.log10 (factor)))
    if len(registers) == 1:
        return format % ((1.0 * registers[0]) / factor)
    elif len(registers) == 2:
        return format % (((1.0 * registers[1] * 65535) + (1.0 * registers[0])) / factor)

def parse_power(usb_stream:list):
    power_list = []
    for s in usb_stream:
        decode_stream = s.decode('utf-8').rstrip()
        temp = decode_stream.split(";")
        if temp:
            temp.pop(0)
            production_str = temp[len(temp)-1]
            production_list = production_str.split(",")
            # remove last element
            production_list.pop(len(production_list) -1)
            # cast in float
            production_list = list(map(lambda x: float(x) * 12, production_list))
            power_list = [*power_list, *production_list]
    return power_list

def get_power_from_usb():
    while not thread_stop_event.is_set():
        # get value from usb
        production1 = usb_power_production1.readline()
        production2 = usb_power_production2.readline()
        production = parse_power([production1, production2])
        if client.connect():
            try:
                demand_result = client.read_input_registers(0x0000, 10, unit = 0x01)
                demand = {
                    "voltage": calc(demand_result.registers[0:1], 10),
                    "power": calc(demand_result.registers[3:5], 10),
                    "frequency": calc(demand_result.registers[7:8], 10)
                }
            finally:
                client.close()

        else:
            print("NOT CONNECTED")
        socket_.emit(
            "data", json.dumps({"production": production, "demand": demand})
        )

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
