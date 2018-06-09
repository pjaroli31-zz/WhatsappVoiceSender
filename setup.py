import subprocess
import os

subprocess.call('cd ..', shell=True)
subprocess.call('sudo apt-get update', shell=True)
subprocess.call('sudo apt-get install git', shell=True)
subprocess.call('sudo apt-get install python-pip', shell=True)
subprocess.call('sudo apt-get install virtualenv', shell=True)
subprocess.call('pip install virtualenv', shell=True)
subprocess.call('virtualenv py-env', shell=True)
subprocess.call('source py-env/bin/activate', shell=True)
os.chdir('WassapVoiceSender')
subprocess.call('sudo pip install -r requirements.txt', shell=True)
print('\nThe project has been set up and the dependencies have been installed\n')
