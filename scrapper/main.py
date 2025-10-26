from fatcher import Fetcher
from maps import Maps
from parser import Parser
from storage import Storage


class Scraper:
    def __init__(self):
        self.maps = Maps()
        self.fetcher = Fetcher()
        self.parser = Parser()
        self.storage = Storage()

    def run(self):
        self.maps.scan_area()
