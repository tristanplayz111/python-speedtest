import colorama
from colorama import Fore



colorama.init(autoreset=True)

mylines = []                             # Declare an empty list named mylines.
with open ('tmp.txt', 'rt') as myfile: # Open lorem.txt for reading text data.
    for myline in myfile:                # For each line, stored as myline,
        mylines.append(myline)           # add its contents to mylines.

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
else:
    print(Fore.RED + "Fatal Error Has Occured!")
    print(Fore.YELLOW + "check tmp.txt for more details")



