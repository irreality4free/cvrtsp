import subprocess
import re
def startProcess(name,python):
    out = subprocess.check_output(['{}'.format(python), '{}'.format(name)])
    print(out)

def KillProcess(name):
    try:
        out = subprocess.check_output('ps -e | grep {}'.format(name),shell=True)
        out = out.decode('utf-8')
        print(out)
        pid = re.findall(r'\d+', out)
        print (pid[0])
        print('killing {} process'.format (pid[0]))
        out = subprocess.check_output('kill {} -9'.format(pid[0]), shell=True)
        print(out)

    except subprocess.CalledProcessError as m:
        print(str(m))


# KillProcess()
# startProg()
