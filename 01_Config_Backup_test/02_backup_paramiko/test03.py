import paramiko
import time
import getpass
import datetime
import re


class SSH(object):

    def __init__(self):
        self.username = "belle"
        self.password = "2020senda"
        self.hostname = ""

    def login_to_device(self, ip):
        self.ip = ip
        self.ssh_client = paramiko.SSHClient()
        self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh_client.connect(hostname=self.ip, username=self.username, password=self.password, look_for_keys=False)
        self.command = self.ssh_client.invoke_shell()
        self.command.send("n\n")
        time.sleep(1)
        self.command.send("system-view\n")
        time.sleep(1)
        self.command.send("user-interface vty 0 4\n")
        time.sleep(1)
        self.command.send("screen-length 0\n")
        time.sleep(1)
        self.command.send("quit\n")
        print("成功连接", self.ip)
        time.sleep(2)
        # output = self.command.recv(65535).decode("ascii")
        # print(output)

    def get_hostname(self):
        self.command.send("dis cu | i sysname\n")
        time.sleep(5)
        output = self.command.recv(65535).decode('utf-8').replace('\r', '')
        print(output)
        hostname = re.search(r'sysname (\S+)', output)
        self.hostname = hostname.group(1)
        time.sleep(2)

    def backup_config(self):
        self.command.send("display current-configuration\n")
        time.sleep(20)
        output = self.command.recv(65535).decode("ascii")
        today = datetime.date.today()
        date = "%s-%s-%s" % (today.year, today.month, today.day)
        with open(self.hostname + "-" + self.ip + "-" + date + "tracet.template", "w+") as f:
            f.write(output)

        self.ssh_client.close()