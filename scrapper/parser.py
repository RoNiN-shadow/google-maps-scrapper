from bs4 import BeatifulSoup
import re


class Parser:
    def parse(self, html) -> list[str]:

        soup = BeatifulSoup(html, 'html.parser')

        # deleting all unnessary tags from html
        for tag in soup.select(['script', 'style', 'noscript']):
            tag.decompose()

        # select all tags which contain contact information
        contact_sections = soup.select('.contact, .contacts, #contact, footer')

        # pattern for an email
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

        emails = []

        if contact_sections:

            for section in contact_sections:
                found = re.findall(pattern, section.get_text())
                emails.extend(found)
        else:
            emails = re.findall(pattern, soup.get_text())

        fake_domains = ['example.com', 'test.com', 'domain.com']
        # filter fake domains
        real_emails = [e for e in emails if not any(
            d in e for d in fake_domains)]

        return real_emails
