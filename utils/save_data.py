import json
from find_email_url import find_email_url
from scan_local import scan_local
from typing import Any

def save_data():

    with open("../data/data.json", 'r', encoding='utf-8') as file:
        companies = json.load(file)

    new_companies: list[dict[str, Any]] = scan_local("Krakov")

    for company in new_companies:
        if company.get("email") is None:
            get_email = find_email_url(company["website"])
            company["email"] = get_email
            if company not in companies:
                companies.append(company)

    with open("../data/data.json", 'w', encoding='utf-8') as file:
        json.dump(companies, file, ensure_ascii=False, indent=4)
