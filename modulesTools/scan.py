
import nmap

# 传入 x.x.x.0/24
def scanNetwork(network):
    returnlist = []
    nm = nmap.PortScanner()
    a = nm.scan(hosts=network, arguments='-T4 -n -Pn')

    for k, v in a['scan'].items():
        if v['status']['state'] == 'up':
            try:
                returnlist.append([v['addresses']['ipv4'], v['addresses']['mac']])
            except:
                pass
        
    return returnlist