import re
import requests
from bs4 import BeautifulSoup
import json



EMAIL_RE = re.compile(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2, }')

def find_email_url(url: str)-> list[str]:
    try:
        r = requests.get(url, timeout=8, headers={"User-Agent": "Mozilla/5.0"})
        r.raise_for_status()
    except Exception as e:
        print("Request faild", e)
        return []
    
    soup = BeautifulSoup(r.text, 'html.parser')
    mails = set()

    #loading the data.json to save all the data about resturans in json
    with open("data.json", 'r', encoding='utf-8') as f:
        data = json.load(f)

    for a in soup.select('a[href^="mailto:"]'):
        href  = a.get('href', '')
        mail = href.split(':', 1)[1].split('?')[0]
        if data[""]
        mails.add(mail) 
    for m in EMAIL_RE.findall(r.text):
        mails.add(m)
    return list(mails)

