setup.sh is for setup on mac. although you can still use speedtest.py with minor modifications.

setup.sh:
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install python3
brew install speedtest
python3 -m ensurepip --upgrade
pip3 install -r requirements.txt
echo use python3 speedtest.py to run speedtester


for all of the other distros make sure you have these installed:
-python3
-speedtest (make sure you install it on the whole system and not pip)
-pip3
-pip3 install -r requirements.txt


i was inspired to make this after looking for a reliable python network speedtester. but most of them use speedtest-cli which isnt very reliable unlike speedtest. the only problem was that speedtest didnt like to work with python unlike speedtest-cli which is a python module. so i made it where python runs speedtest, collects all the data, and then showing it. why would you need it if you can just use speedtest? to be honest i dont really know unless they absolutly need python.
