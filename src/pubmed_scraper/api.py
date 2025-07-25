import requests
import xmltodict

BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"

def fetch_pubmed_ids(query: str, max_results: int = 20):
    params = {
        "db": "pubmed",
        "term": query,
        "retmax": max_results,
        "retmode": "json"
    }
    response = requests.get(BASE_URL + "esearch.fcgi", params=params)
    response.raise_for_status()
    return response.json()["esearchresult"]["idlist"]

def fetch_paper_details(pubmed_id: str):
    params = {
        "db": "pubmed",
        "id": pubmed_id,
        "retmode": "xml"
    }
    response = requests.get(BASE_URL + "efetch.fcgi", params=params)
    response.raise_for_status()
    return xmltodict.parse(response.content)
