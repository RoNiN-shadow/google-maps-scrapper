from fatcher import Fetcher
from maps import Maps
from parser import Parser
from storage import Storage


class Scraper:
    def __init__(self, location: str, type: str):
        self.maps = Maps(location, type)
        self.fetcher = Fetcher()
        self.parser = Parser()
        self.storage = Storage()

    def run(self):
        companies = self.maps.scan_area()
        update_companies = []
        for company in companies:
            if company.get("emails") is None:
                html = self.fetcher.get(company.get("url"))

                emails = self.parser.parse(html)
                company.get("emails").extend(emails)
            update_companies.append(company)

        self.storage.save_companies(update_companies)
