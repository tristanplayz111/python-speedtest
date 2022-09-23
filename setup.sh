#!/bin/bash 

/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install python3
brew install speedtest
python3 -m ensurepip --upgrade
pip3 install -r requirements.txt
echo use python3 speedtest.py to run speedtester