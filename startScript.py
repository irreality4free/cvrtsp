import subprocess
import re
def startProcess():
    out = subprocess.check_output(['python3', 'CameraScript.py'])
    print(out)

def KillProcess():
    try:
        out = subprocess.check_output('ps -e | grep CameraScript.py',shell=True)
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