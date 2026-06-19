from langchain.tools import tool
import arxiv

client = arxiv.Client(page_size=5, delay_seconds=1.0, num_retries=2)

@tool
def arxiv_search(query: str) -> str:
    """Search for academic papers on arXiv and return the results."""
    search = arxiv.Search(
        query=query,
        max_results=5,
        sort_by=arxiv.SortCriterion.Relevance
    )
    results = []
    for result in client.results(search):
        results.append(f"Title: {result.title}\nAuthors: {', '.join(author.name for author in result.authors)}\nSummary: {result.summary}\nURL: {result.entry_id}\n")
    return "\n\n".join(results)