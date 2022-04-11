import socket
import threading
import ipaddress
from netaddr import *

def port_scanner(ip,port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((str(ip), port))
        print(f"Port {port} is open")
    except:
        pass

#def checkservices:

while True:
    print("=============================================================================")
    print("========================== SIMPLE PORT SCANNER ==============================")
    print("=============================================================================")
    print("Enter IP Range (Ex. 10.10.10.1 - 10.10.10.100)")
    print("If you want to check only 1 IP then follow this (Ex. 10.10.10.1 - 10.10.10.1)")
    ipStart, ipEnd = input("Enter IP : ").split("-")

    try:
        check_ip = ipaddress.ip_address(ipStart)
        check_ip = ipaddress.ip_address(ipEnd)
        print("=============================================================================")
        print("========================== Valid IP Address =================================")
        print("=============================================================================")
        break
    except:
        print("=============================================================================")
        print("========================= Invalid IP Address ================================")
        print("=============================================================================")

iprange = IPRange(ipStart, ipEnd)

portStart, portEnd = input ("Enter Port (Ex. 0 - 65535): ").split("-")
portStart, portEnd = [int(portStart), int(portEnd)]

for ip in iprange:
   host = ip
   print("=============================================================================")
   print(host)
   print("=============================================================================")
   for port in range(portStart,portEnd):
        thread = threading.Thread(target =port_scanner, args=(ip,port))
        thread.start()