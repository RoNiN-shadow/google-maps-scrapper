import os
import time
from dotenv import load_dotenv
import googlemaps


class Maps:
    def __init__(self, location: str, type: str):
        self.location = location
        self.type = type

    def scan_area(self):
        load_dotenv()

        gmaps = googlemaps.Client(key=os.getenv(
            "GOOGLE_MAPS_API_KEY"))
        geocode_result = gmaps.geocode(self.location)

        latlng = geocode_result[0]["geometry"]["location"]

        coords = (latlng["lat"], latlng["lng"])

        restaurants = gmaps.places_nearby(
            location=coords, radius=5000, type=self.type)
        results = restaurants.get('results', [])

        new_companies = []
        for r in results:
            pid = r['place_id']
            details = gmaps.place(place_id=pid, fields=[
                                  'name', 'formatted_address', 'website'])
            d = details.get('result', {})
            website = d.get('website')
            email = d.get('email')

            new_companies.append({
                'name': d.get('name'),
                'address': d.get('formatted_address'),
                'website': website,
                'emails': list(email),
            })
            time.sleep(0.1)
        return new_companies
