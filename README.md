# Pyhtools
  基于python-nmap, scapy, socket等库实现的可对目标主机进行dos攻击, 局域网内arp断网攻击，短信轰炸，邮箱轰炸。
  
  开发环境为vscode，在pycharm下运行代码打开json文件的相对路径可能会报错，改为pycharm下文件相对路径写法即可正常使用！
![image](https://user-images.githubusercontent.com/102849988/215247341-69c5970f-c1cb-4c33-8496-a6d47d0c078a.png)

## Install
### 1. Windows下安装nmap（如果不使用arp断网攻击，不需要安装nmap）
### 2. python相关库安装
```python
pip install -r requirements.txt
```

## Usage
### 1. ArpAttack
输入1，待扫描完成后，选择目标开始输入每分钟发包次数，按Ctrl+C停止攻击。
![image](https://user-images.githubusercontent.com/102849988/215247970-903bb90c-14e1-4fa5-bb9c-afc665a1cfd6.png)
### 2. DoS Attack
输入2， 输入网址，存在一个bug待解决，Python的Thread线程该如何停止。。。
![image](https://user-images.githubusercontent.com/102849988/215248058-56232ea8-d59c-4a4b-a85d-8e7ee849fc3d.png)
### 3. Email Bomb
输入3，要轰炸的邮箱，主题，内容。通过yagmail库实现发送邮件，使用的是QQ邮箱，多添加
QQ邮箱及其授权码，效果更加（防止单一QQ邮箱发送邮件被放入垃圾邮箱）

![image](https://user-images.githubusercontent.com/102849988/215248094-53be6daf-6675-4570-9d81-8d5154e31e4c.png)
### 4. SmS Bomb
输入4，填写要轰炸的手机号。smsBomb.py源文件中只实现一次轰炸，可以添加多线程，在api.json中增加api接口效果更加！

![image](https://user-images.githubusercontent.com/102849988/215248252-505efad1-83b8-401d-92d4-805c13bb9de5.png)

## Bug and Improvement
### 1. Bug: DoS模块中Python的Thread线程该如何停止（通过Ctrl+C停止）？
### 2. Bug: 垃圾短信轰炸只是通过简单的request请求是否响应来判断该次发送短信是否成功。大部分api失效。
### 3. Improvement: 邮箱轰炸增加QQ邮箱及其授权码。
### 4. Improvement: 垃圾短信轰炸增加多线程及其api接口。
### 5. Improvement: 更多的攻击手段添加。



