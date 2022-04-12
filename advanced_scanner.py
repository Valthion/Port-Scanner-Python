import ipaddress
import nmap
import requests
import socket
from netaddr import *

def test_socks4(ip,port,url):
    resp = None
    try:
        proxy_url = "socks4://" + ip + ":" + str(port)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; U; Android 4.0.3; ko-kr; LG-L160L Build/IML74K) AppleWebkit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'
        }
        resp = requests.post(url,headers=headers,proxies=dict(http=proxy_url,https=proxy_url),timeout=10)
    except:
        resp=None
    return(resp)

def test_socks5(ip,port,url):
    resp=None
    try:
        proxy_url = "socks5://" + str(ip) + ":" + str(port)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; U; Android 4.0.3; ko-kr; LG-L160L Build/IML74K) AppleWebkit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'
        }
        resp = requests.post(url,headers=headers,proxies=dict(http=proxy_url,https=proxy_url),timeout=10)
    except:
        resp=None
    return(resp)

def scanner(ip,port):
    pesan=""
    try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(5)
            s.connect((str(ip), int(port)))
            s.send(b'halo')
            pesan = s.recv(4096)
            s.close()
    except:
        pesan="Error"
    return(pesan)

while True:
    print("=================================================================================")
    print("============================= ADVANCED PORT SCANNER =============================")
    print("=================================================================================")
    print("Enter IP Range (Ex. 10.10.10.1 - 10.10.10.100)")
    print("If you want to check only 1 IP then follow this (Ex. 10.10.10.1 - 10.10.10.1)")
    ipStart, ipEnd = input("Enter IP : ").split("-")

    try:
        check_ip = ipaddress.ip_address(ipStart)
        check_ip = ipaddress.ip_address(ipEnd)
        print("=================================================================================")
        print("=========================== Valid IP Address ====================================")
        print("=================================================================================")
        break
    except:
        print("=================================================================================")
        print("========================= Invalid IP Address ====================================")
        print("=================================================================================")

iprange = IPRange(ipStart, ipEnd)

portrange = input ("Enter Port (Ex. 0 - 65535): ")
print("=================================================================================")

nm = nmap.PortScanner()

for ip in iprange:
   host = ip
   print(host)
   print("=================================================================================")

   try:
       nm.scan(str(ip), str(portrange))
       for host in nm.all_hosts():
           print('Host : %s (%s)' % (host, nm[host].hostname()))
           print('State : %s' % nm[host].state())
           print("=================================================================================")
           if (len(nm[host].all_protocols()) == 0):
               print("No open ports")
               print("=================================================================================")
           for proto in nm[host].all_protocols():
               print('Protocol : %s' % proto)
               print("=================================================================================")
               lport = nm[host][proto].keys()
               for port in lport:
                   socksyes4 = False
                   socksyes5 = False
                   if (nm[host][proto][port]['state'] == 'open'):
                       pesan = scanner(ip,port)

                       if (str(test_socks4(str(ip), port, "https://siasat.uksw.edu")) == "<Response [200]>"):
                           socksyes4 = True
                       else:
                           socksyes4 = False

                       if (str(test_socks5(str(ip), port, "https://www.twitter.com")) == "<Response [200]>"):
                           socksyes5 = True
                       else:
                           socksyes5 = False

                       print(f"IP {ip} | Service Identification : {pesan}")
                       print('Port : %s\t| State : %s' % (port, nm[host][proto][port]['state']))
                       print("Socks v4 : ", socksyes4, " | Socks v5 : ", socksyes5)
                       print("=================================================================================")

   except Exception as e:
       print(e)
