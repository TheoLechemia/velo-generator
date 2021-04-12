import re
import subprocess
device_re = re.compile("Bus\s+(?P<bus>\d+)\s+Device\s+(?P<device>\d+).+ID\s(?P<id>\w+:\w+)\s(?P<tag>.+)$", re.I)
df = subprocess.check_output("lsusb")

def find_usb_path(usb_id):
    for i in df.decode('utf-8').split('\n'):
        if i:
            info = device_re.match(i)
            if info:
                dinfo = info.groupdict()
                dinfo['device'] = '/dev/bus/usb/%s/%s' % (dinfo.pop('bus'), dinfo.pop('device'))
                if dinfo["id"] == usb_id:
                    return dinfo
    return None

# t = find_usb_path("1004:631c")
# print(t)

import usb.core 

dev = usb.core.find(idVendor=0x046d, idProduct=0xc06d)
ep = dev[0].interfaces()[0].endpoints()[0]
i = dev[0].interfaces()[0].bInterfaceNumber
print(dev)
print("ep")
print(ep)
print('la')
print(i)

if dev.is_kernel_driver_active(i):
    dev.detach_kernel_driver(i)

dev.set_configuration()

eaddr = ep.bEndpointAddress
import time

while True:
    r = dev.read(eaddr, 1024)
    print(r)
    time.sleep(1)
# r = dev.read(eaddr, 1024)
# print(r)


# Bind to a static port
# https://unix.stackexchange.com/questions/66901/how-to-bind-usb-device-under-a-static-name