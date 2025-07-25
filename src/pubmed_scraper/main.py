import typer
from pubmed_scraper.api import fetch_pubmed_ids, fetch_paper_details
from pubmed_scraper.parser import extract_info
from pubmed_scraper.writer import write_csv
from typing import Optional

app = typer.Typer()

@app.command()
def get_papers_list(
    query: str,
    file: Optional[str] = typer.Option(None, "--file", "-f", help="Output CSV filename"),
    debug: bool = typer.Option(False, "--debug", "-d", help="Enable debug mode")
):
    ids = fetch_pubmed_ids(query)
    if debug:
        typer.echo(f"Found {len(ids)} papers for query '{query}'.")

    results = []
    for i, pid in enumerate(ids):
        details = fetch_paper_details(pid)
        info = extract_info(details)
        if info:
            results.append(info)
        if debug:
            typer.echo(f"[{i+1}/{len(ids)}] Processed ID: {pid}")

    if file:
        write_csv(results, file)
        typer.echo(f"Saved results to {file}")
    else:
        for item in results:
            typer.echo(item)

if __name__ == "__main__":
    app()
