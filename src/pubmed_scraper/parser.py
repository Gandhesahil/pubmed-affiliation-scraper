import re
from typing import List, Dict, Tuple

COMPANY_KEYWORDS = ["pharma", "biotech", "inc", "corp", "ltd", "gmbh", "co.", "pvt"]

def is_company_affiliation(affiliation: str) -> bool:
    return any(word.lower() in affiliation.lower() for word in COMPANY_KEYWORDS)

def extract_info(record: Dict) -> Dict:
    try:
        article = record['PubmedArticleSet']['PubmedArticle']['MedlineCitation']
        article_info = article['Article']
        pubmed_id = article['PMID']['#text']
        title = article_info['ArticleTitle']
        pub_date = article_info['Journal']['JournalIssue']['PubDate']
        authors = article_info.get("AuthorList", {}).get("Author", [])
        if not isinstance(authors, list):
            authors = [authors]

        non_acad_authors, companies = [], []
        email = ""

        for author in authors:
            affil = author.get("AffiliationInfo", [{}])[0].get("Affiliation", "")
            name = f"{author.get('ForeName', '')} {author.get('LastName', '')}".strip()
            if is_company_affiliation(affil):
                non_acad_authors.append(name)
                companies.append(affil)

                found_emails = re.findall(r"[A-Za-z0-9\._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}", affil)
                if found_emails:
                    email = found_emails[0]

        return {
            "PubmedID": pubmed_id,
            "Title": title,
            "Publication Date": str(pub_date),
            "Non-academic Author(s)": "; ".join(non_acad_authors),
            "Company Affiliation(s)": "; ".join(companies),
            "Corresponding Author Email": email
        }
    except Exception:
        return {}
