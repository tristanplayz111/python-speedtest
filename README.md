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
-speedtest
-pip3
-pip3 install -r requirements.txt
