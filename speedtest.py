import subprocess
import threading
import colorama
from colorama import Fore
import time
import os
import sys

colorama.init(autoreset=True)


# set logfile name
logfile = 'tmp.txt'
# subprocess comand
command = ['speedtest', '-p', 'no']

# listen and write subprocess output to logfile (tmp.txt)
def writer(p, logfile):
   with open(logfile, 'w') as f:
    # spinning wheel
    print(Fore.BLUE + "made and developed by ST3W")
    print(Fore.CYAN + "Testing",)
    syms = ['\\', '|', '/', '-']
    bs = '\b'

    for _ in range(10):
        for sym in syms:
            sys.stdout.write("\b%s" % sym)
            sys.stdout.flush()
            time.sleep(.5)
    for line in p.stdout:
        f.write(line)
    for line in p.stderr:
        f.write(line)

# Run Subprocess

p = subprocess.Popen(command, stdout = subprocess.PIPE, stderr = subprocess.PIPE, universal_newlines = True)

t = threading.Thread(target = writer, args = (p, logfile))
t.start()

t.join()


# load logfile into variable (mylines)

mylines = []                             
with open (logfile, 'rt') as myfile: 
    for myline in myfile:               
        mylines.append(myline)           
#Display Info

if "(NoNetworkConnection)" in mylines[1]:
    print(Fore.RED + "No Network Connection!")
    print(Fore.YELLOW + "connect to internet to test speed")
elif mylines[1] == '   Speedtest by Ookla\n':
    print(Fore.CYAN + "   Server Used")
    print(mylines[3])
    print(Fore.CYAN + "   Your ISP Provider")
    print(mylines[4])
    print("")
    print(Fore.CYAN + "   Network Info")
    print("    ", mylines[5])
    print(mylines[6])
    print(mylines[7])
    print(mylines[8])
    print(mylines[9])
    print(mylines[10])
    if mylines[12] == ' Packet Loss: Not available.\n':
        print(Fore.YELLOW + mylines[12] + " retry test")
    elif mylines[12] == ' Packet Loss:     0.0%\n':
        print(Fore.GREEN + mylines[12])
    else:
        print(Fore.LIGHTYELLOW_EX + mylines[12])

    print(Fore.CYAN + "   View SpeedTest")
    print("   ", mylines[13])
    print(Fore.BLUE + "made and developed by ST3W ()")
    if os.path.exists("tmp.txt"):
        os.remove("tmp.txt")
        exit()
    else:
        exit()
else:
    print(Fore.RED + "Fatal Error Has Occured!")
    print(Fore.YELLOW + "check tmp.txt for more details")

print(Fore.BLUE + "made and developed by ST3W")