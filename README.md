# 🔬 PubMed Company Paper Scraper

This is a Python command-line tool I built that searches for research papers on PubMed using any user query. It filters out papers that have at least one author from a pharmaceutical or biotech company, and saves the result in a CSV file.

---

## 🚀 What It Can Do

- You can search PubMed using any keyword or query.
- It checks each paper’s author affiliations and picks the ones from companies (like Pfizer, Moderna, etc.).
- It tries to extract the corresponding author’s email address.
- It gives you the output as a CSV file (or prints to the screen if no file is given).
- You can also use the `--debug` option to see what's happening in the background.

---

## ⚙️ How to Use It

### Step 1: Install Dependencies

First, make sure you have [Poetry](https://python-poetry.org/docs/) installed. Then run:

```bash
poetry install
