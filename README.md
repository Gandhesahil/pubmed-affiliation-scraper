# PubMed Affiliation Scraper

This Python-based CLI tool searches for research papers using the [PubMed API](https://www.ncbi.nlm.nih.gov/home/develop/api/), identifies papers that include at least one company-affiliated author (based on affiliation strings), and exports the results to a CSV file.

---

## 🔧 How the Code is Organized

pubmed_scraper/
├──.git/
├── src/
│   └── pubmed_scraper/
│       ├── __pycache__/
│       ├── __init__.py
│       ├── api.py             
│       ├── parser.py         
│       ├── writer.py      
│       └── main.py     
├── tests/
├── poetry.lock 
├── README.md
├── pyproject.toml
├── results.csv



---

## ⚙️ Installation & Execution

### 1. ✅ Prerequisites
- Python 3.8+
- Poetry (Install using [this guide](https://python-poetry.org/docs/#installation))

### 2. 🧱 Clone the Repository
```bash
git clone https://github.com/your-username/pubmed-affiliation-scraper.git
cd pubmed-affiliation-scraper


3.📦 Install Dependencies Using Poetry
     -> poetry install

4.🚀 Run the Tool
     -> poetry run get-papers-list "covid vaccine" -f results.csv debug



---


🛠 Tools & Libraries Used
✅ Programming Tools:
Poetry — for dependency and package management.

Python Typer — to build the command-line interface.

Requests — for making HTTP requests to the PubMed API.

xmltodict — for parsing XML responses from PubMed.

Python Standard Library — for CSV writing and OS operations.

🤖 Language Models:
This project was built with step-by-step guidance from OpenAI ChatGPT to:

Understand the PubMed API

Set up Poetry environment

Structure modular Python code

Create an interactive CLI

Filter company-affiliated papers

Generate this documentation