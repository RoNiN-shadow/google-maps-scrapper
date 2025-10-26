from google.cloud import firestore


class Storage:
    def save_companies(self, companies: list[dict]):
        db = firestore.Client()
        company_ref = db.collection("companies")

        for company in companies:
            doc_ref = company_ref.document(company['name'])
            if not doc_ref.get().exists:
                company_ref.document(company['name']).set(
                    company, merge=True)
