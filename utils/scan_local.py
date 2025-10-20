import os, time
from dotenv import load_dotenv
import googlemaps
from find_email_url import find_email_url


def scan_local(location: str)-> list[dict[str, str]]:

    load_dotenv()

    gmaps = googlemaps.Client(key=os.getenv("GOOGLE_MAPS_API_KEY")) #type: ignore

    resturans = gmaps.places_nearby(location=location, radius=5000, type='restaurant')

    results = resturans.get('results',[])

    out = []
    for r in results:
        pid = r['place_id']
        details = gmaps.place(place_id=pid, fields=['name', 'formmated_address', 'website'])
        d = details.get('results', {})
        website = d.get('website')

        emails = find_email_url(website) if website else []

        out.append({
            'name': d.get('name'),
            'adress': d.get('formmated_address'),
            'website' : website,
            'emails' : emails,
        })
        time.sleep(0.1)
    return out
