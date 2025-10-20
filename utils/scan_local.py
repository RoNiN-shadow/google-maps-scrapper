import os, time
from dotenv import load_dotenv
import googlemaps
from find_email_url import find_email_url
import json

from typing import Any

def scan_local(location: str)-> list[dict[str, Any]]:

    load_dotenv()

    gmaps = googlemaps.Client(key=os.getenv("GOOGLE_MAPS_API_KEY")) #type: ignore

    resturans = gmaps.places_nearby(location=location, radius=5000, type='restaurant')

    results = resturans.get('results',[])

    new_companies = []
    for r in results:
        pid = r['place_id']
        details = gmaps.place(place_id=pid, fields=['name', 'formmated_address', 'website'])
        d = details.get('results', {})
        website = d.get('website')

        emails = find_email_url(website) if website else []

        new_companies.append({
            'name': d.get('name'),
            'adress': d.get('formmated_address'),
            'website' : website,
            'emails' : list(emails),
        })
        time.sleep(0.1)

    return new_companies
