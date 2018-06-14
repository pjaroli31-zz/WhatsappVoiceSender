import subprocess
import os

subprocess.call('sudo apt-get update', shell=True)
subprocess.call('sudo apt-get install git', shell=True)
subprocess.call('sudo apt-get install python-pip', shell=True)
subprocess.call('sudo pip install -r requirements.txt', shell=True)
subprocess.call('sudo apt-get install python-pyaudio python3 pyaudio', shell=True)
print('\nThe project has been set up and the dependencies have been installed\n')
