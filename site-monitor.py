# run 'pip install -r requirements.txt' to install all dependencies
import requests
from bs4 import BeautifulSoup
import difflib
import time
from datetime import datetime

# Set URL 
url = 'https://ctf.mlh-fellowship.space/challenges'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

PrevVersion = ''
FirstRun = True
while True:

    # download the page
    response = requests.get(url, headers=headers)
    # parse page
    soup = BeautifulSoup(response.text, "lxml")

    # remove all script and style elements
    for script in soup(["script", "style"]):
        script.extract()
    soup = soup.get_text()

    # compare text to the previous version
    if PrevVersion != soup:
        if FirstRun:
            FirstRun = False
            PrevVersion = soup
            print ("Start Monitoring "+url+" "+datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        else:
            print("Changes detected at: "+url+" "+datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            OldVersion = PrevVersion.splitlines()
            NewVersion = soup.splitlines()
            # compare the two versions
            diff = difflib.context_diff(OldVersion, NewVersion, n=10)
            out_text = '\n'.join([ll.rstrip() for ll in '\n'.join(diff).splitlines() if ll.strip()])
            print(out_text)
            OldVersion = NewVersion
            PrevVersion = soup
    else:
        print("No Changes detected at: "+url+" "+datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    time.sleep(10)
    continue