# CTF Site Monitor

Script to monitor CTF Challenge page for updates on when a change is made (challenge added). Sends email alerts. 

Uncomment line 44 and update with your email and password. If you're using gmail and have 2-step verification, you'll need to create an [App password](https://support.google.com/accounts/answer/185833?hl=en). 

## Instructions
Clone repo and cd into it \
Create virtualenv: `virtualenv venv` \
Activate venv: `source venv/bin/activate` \
Install dependencies: `pip install -r requirements.txt` \
Run: `python site-monitor.py`


