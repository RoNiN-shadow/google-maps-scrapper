from bs4 import BeatifulSoup


class Parser:
    def parse(self, html):

        soup = BeatifulSoup(html, 'html.parser')

        for link in soup.select()

