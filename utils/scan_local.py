import os, time
from dotenv import load_dotenv
import googlemaps
from find_email_url import find_email_url

from typing import Any

def scan_local(location: str)-> list[dict[str, Any]]:

    load_dotenv()
    gmaps = googlemaps.Client(key=os.getenv("GOOGLE_MAPS_API_KEY")) #type: ignore

    geocode_result = gmaps.geocode(location)
    latlng = geocode_result[0]["geometry"]["location"]
    coords = (latlng["lat"], latlng["lng"])

    restaurants= gmaps.places_nearby(location=coords, radius=5000, type='restaurant')

    results = restaurants.get('results',[])

    new_companies = []
    for r in results:
        pid = r['place_id']
        details = gmaps.place(place_id=pid, fields=['name', 'formatted_address', 'website'])
        d = details.get('result', {})
        website = d.get('website')

        emails = find_email_url(website) if website else []

        new_companies.append({
            'name': d.get('name'),
            'address': d.get('formatted_address'),
            'website' : website,
            'emails' : list(emails),
        })
        time.sleep(0.1)

    return new_companies
