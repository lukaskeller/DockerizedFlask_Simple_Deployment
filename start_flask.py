import os
os.environ['FLASK_APP']= os.path.join('app', 'main.py')

import subprocess

subprocess.call(['flask', 'run'])