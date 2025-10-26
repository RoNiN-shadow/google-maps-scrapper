import requests


class Fetcher:
    def get(self, url: str) -> str:

        response = requests.get(url, timeout=8, header={
                                "User-Agent": "Mozilla/5.0"})
        response.raise_for_status()
        return response.text
