#!/usr/bin/python
import time,subprocess
time.sleep(5)
subprocess.call('./setup.sh', shell=True)
subprocess.call('python run.py', shell=True)
