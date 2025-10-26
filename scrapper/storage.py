from google.cloud import firestore


class Storage:
    def save_companies(self, companies: list[dict], email: str):
        db = firestore.Client()
        company_ref = db.collection("companies")

        for company in companies:
            if company.get("email") is None:
                company["email"] = email
                doc_ref = company_ref.document(company['name'])
                if not doc_ref.get().exists:
                    company_ref.document(company['name']).set(
                        company, merge=True)
