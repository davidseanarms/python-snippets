# This script will detect and output a list of all drivers and external devices connected to a computer.
# IT Support scripts

#!/usr/bin/env python3

# Import the necessary modules 
import os 
import sys 

# Check for operating system 
def check_os():
    if not (sys.platform.startswith('win') or sys.platform.startswith('linux')):
        print('Error: unrecognized operating system. This script only works on Windows or Linux.')
        exit()
    else:
        pass

if sys.platform.startswith('win'): 
    check_os()
    check_permissions()
    # For Windows 
    from win32com.client import GetObject 
    wmi = GetObject('winmgmts:') 
    # Get all external devices 
    devices = wmi.InstancesOf('Win32_PnPEntity') 
    check_disabled_devices()
    print('External devices connected to the PC:') 
    for device in devices: 
        print(device.Name) 
elif sys.platform.startswith('linux'): 
    check_os()
    # For Linux 
    # Get all external devices 
    devices = os.listdir('/sys/class/') 
    print('External devices connected to the PC:') 
    for device in devices: 
        print(device)

# Check for disabled devices 
def check_disabled_devices():
    disabled_devices = []
    for device in devices:
        if device.ConfigManagerErrorCode != 0:
            disabled_devices.append(device.Name)
    if len(disabled_devices) > 0:
        print('The following devices are disabled:')
        for d in disabled_devices:
            print(d)

def check_permissions():
    if not os.access('./win32com.client', os.R_OK):
        print('User does not have permissions to access WMI services')
        exit()
    else:
        pass
