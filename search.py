import bluetooth
from pick import pick

sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.bind(("", bluetooth.PORT_ANY))
sock.listen(1)
port = sock.getsockname()[1]

if port:
    found = bluetooth.discover_devices(lookup_names=True, lookup_class=True)
    names, device_id = [],[]
    for devices in found:
        names.append(devices[1])
        device_id.append(devices[0])

    names, index = pick(names, 'Please choose your device to be connected: ', indicator='->', default_index=0)
    
    print(f'Searching for your {names[index]} on channel: {device_id[index]}...')
    
    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    sock.connect((str(device_id[index]), int(port)))




    