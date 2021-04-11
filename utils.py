import re
import subprocess
device_re = re.compile("Bus\s+(?P<bus>\d+)\s+Device\s+(?P<device>\d+).+ID\s(?P<id>\w+:\w+)\s(?P<tag>.+)$", re.I)
df = subprocess.check_output("lsusb")

def find_usb_path(usb_id):
    devices = []
    for i in df.decode('utf-8').split('\n'):
        if i:
            info = device_re.match(i)
            if info:
                dinfo = info.groupdict()
                dinfo['device'] = '/dev/bus/usb/%s/%s' % (dinfo.pop('bus'), dinfo.pop('device'))
                devices.append(dinfo)
    return next( (x for x in devices if x["id"] == usb_id), devices)


t = find_usb_path("1004:631c")
print(t)