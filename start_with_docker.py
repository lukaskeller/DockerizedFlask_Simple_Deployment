import subprocess

subprocess.call(['docker-compose', 'down'])
subprocess.call(['docker-compose', 'up', '--build'])