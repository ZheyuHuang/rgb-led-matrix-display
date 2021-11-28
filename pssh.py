import sys, os, string, threading
import paramiko
from paramiko import SSHClient
from scp import SCPClient

cmd = "./led_show.sh"
outlock = threading.Lock()

def workon(host):

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username='pi', password='luxlibertas')
    scp = SCPClient(ssh.get_transport())
    scp.put('/Users/zheyu/Downloads/COMP 89/images/im1.jpg', '/home/pi/Pictures')
    scp.put('/Users/zheyu/Downloads/COMP 89/images/im2.jpg', '/home/pi/Pictures')
    scp.put('/Users/zheyu/Downloads/COMP 89/images/im3.jpg', '/home/pi/Pictures')

    scp.close()

    stdin, stdout, stderr = ssh.exec_command(cmd)
    stdin.write('luxlibertas\n')
    stdin.flush()

    with outlock:
        print (stdout.readlines())

def main():
    hosts = ['152.23.60.88','152.23.17.138', '152.23.149.117'] # etc 2'152.23.17.138', 3'152.23.149.117', 1'152.23.60.88' 
    threads = []
    for h in hosts:
        t = threading.Thread(target=workon, args=(h,))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()

