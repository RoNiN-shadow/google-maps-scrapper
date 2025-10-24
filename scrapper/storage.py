from find_email_url import find_email_url
from scan_local import scan_local
from typing import Any
from google.cloud import firestore


def save_data():

    db = firestore.Client()
    company_ref = db.collection("companies")

    new_companies: list[dict[str, Any]] = scan_local("Krakov")

    for company in new_companies:
        if company.get("email") is None:
            get_email = find_email_url(company["website"])
            company["email"] = get_email
            doc_ref = company_ref.document(company['name'])
            if not doc_ref.get().exists:
                company_ref.document(company['name']).set(company, merge=True)
