import subprocess
import time

p = subprocess.Popen(['C:\Riot Games\Riot Client\RiotClientServices.exe', '--launch-product=valorant', '--launch-patchline=live'])
start = time.time()
p.wait()
elapsed = int(time.time() - start) 
print('You\'ve played for ' + str(elapsed) + ' seconds (' + str(int(elapsed/60)) + ' minutes)' )