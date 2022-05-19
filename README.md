# Prometheus GUI 2022

Installation and Setup:
[Google Doc (with pictures!)](https://docs.google.com/document/d/13TNMpSc-YqPO50H5LMzu2A0UPb89W38w97et8WEm5aw/edit#)

<br>
<br>

## Windows Instructions
No pictures but same content as the google doc


Dependencies
- Git
- Python3
- Telegraf
- Grafana
- VS Code

### Instructions for Installing the Dependencies
Download git here: https://git-scm.com/download/win 

To download Python, go to this link: https://www.python.org/downloads/ and download the latest version of Python
Make sure to check the box that says “Add to PATH”

To download Telegraf, open a Powershell terminal as Administrator:

Copy paste these commands one by one in and wait until they finish
```
cd ~/Downloads

wget https://dl.influxdata.com/telegraf/releases/telegraf-1.22.4_windows_amd64.zip -UseBasicParsing -OutFile telegraf-1.22.4_windows_amd64.zip

Expand-Archive .\telegraf-1.22.4_windows_amd64.zip -DestinationPath 'C:\Program Files\InfluxData\telegraf'
```

To download Grafana: https://grafana.com/grafana/download?platform=windows 

Click on the words that say “Download the Installer”

Download VS Code here: https://code.visualstudio.com/download 
Check these two boxes (“Add Open with Code”)

Open VS Code and click on the “Extensions” tab on the left hand side

Download the Python extension 

All done! Yay! 

<br>


### Installing and Setting up the Actual GUI :(
Go to this link: https://github.com/atpngo/prometheus-gui-2022.git 

Click on the green Code button and then “Download ZIP” OR use this command in a terminal window: 
```
git clone https://github.com/atpngo/prometheus-gui-2022.git  
```

Unzip the file and put it anywhere you want
Open the folder by right clicking the directory and clicking “Open with Visual Studio Code”

Open up a browser window and go to localhost:3000
Make a fake login or whatever it doesn’t rly matter
Go to Configuration -> Api Keys


Add a new API key, calling it whatever you want.

<b>LEAVE THE TIME TO LIVE BOX EMPTY SO THAT THE KEY DOES NOT EXPIRE.</b>

Copy that API key and paste it in the api-key.txt file
Then run the ```replace-bearer.py``` file
This bad boy is gonna fix all the conf files so that they work with your api key :)
Next, go to Grafana and hit that plus sign and click on import

Find the ```dashboard.json file``` in the ground-systems folder and upload it
Yay i think thats it for Windows




