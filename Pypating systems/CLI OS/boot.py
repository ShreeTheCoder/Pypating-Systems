import subprocess
import time

print("Booting up...")
time.sleep(1)
print("Loading functions and system files including boot files...")
time.sleep(4)
print("Starting...")
time.sleep(2)
subprocess.run(["python", "main.py"])
exit()