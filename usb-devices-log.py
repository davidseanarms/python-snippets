import os
import time

# scan the USB ports on the device
ports = os.system("lsusb | awk '{print $2}'")

# output a .txt file with number of ports
f = open("./usbports.txt","w+")
f.write("Number of ports: " + str(ports) + "\n")

# ports in use
f.write("Ports in use: \n")
for i in range(ports):
    output = os.system("lsusb -v | grep bNumInterfaces | awk '{print $NF}'")
    f.write(str(output) + "\n")

# PID of physical devices connected to the ports
f.write("PID of physical devices connected to the ports: \n")
for i in range(ports):
    output = os.system("lsusb -v | grep idProduct | awk '{print $NF}'")
    f.write(str(output) + "\n")

# timestamp of when devices were connected
f.write("Timestamp of when devices were connected: \n")
timestamp = time.strftime("%d/%m/%Y %H:%M:%S")
f.write(timestamp + "\n")

f.close()
