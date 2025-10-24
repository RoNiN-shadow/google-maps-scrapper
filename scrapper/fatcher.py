import re
import requests
from bs4 import BeautifulSoup


EMAIL_RE = re.compile(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2, }')


class Fetcher:
    def get(self, url: str) -> str:

        response = requests.get(url, timeout=8, header={
                                "User-Agent": "Mozilla/5.0"})
        response.raise_for_status()
        return response.text


def find_email_url(url: str) -> list[str]:
    try:
        r = requests.get(url, timeout=8, headers={"User-Agent": "Mozilla/5.0"})
        r.raise_for_status()
    except Exception as e:
        print("Request faild", e)
        return []

    soup = BeautifulSoup(r.text, 'html.parser')
    mails = set()

    for a in soup.select('a[href^="mailto:"]'):
        href = a.get('href', '')
        mail = href.split(':', 1)[1].split('?')[0]
        mails.add(mail)
    for m in EMAIL_RE.findall(r.text):
        mails.add(m)
    return list(mails)
