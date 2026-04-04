import arxiv
import time
from typing import List, Dict, Any
import os

def arxiv_search(query: str, max_results: int = 5, retries: int = 3) -> Dict[str, Any]:
    """
    Search for research papers using the ArXiv API.

    Args:
        query (str): The search query.
        max_results (int): Maximum number of results to return.
        retries (int): Number of retry attempts on failure.

    Returns:
        dict: A dictionary containing the 'status' and the resulting 'data' or 'message'.
    """
    print(f"📡 [Tool: arxiv_search] Fetching papers for: '{query}'...")

    for attempt in range(retries):
        try:
            # Proper client with delay (VERY IMPORTANT)
            client = arxiv.Client(
                page_size=max_results,
                delay_seconds=3.0  # arXiv recommends ~3 seconds
            )

            search = arxiv.Search(
                query=query,
                max_results=max_results,
                sort_by=arxiv.SortCriterion.Relevance
            )

            results: List[Dict[str, Any]] = []

            for paper in client.results(search):
                results.append({
                    "title": paper.title,
                    "authors": [author.name for author in paper.authors],
                    "published": str(paper.published.date()),
                    "pdf_url": paper.pdf_url,
                    "abstract": paper.summary.replace('\n', ' ')
                })

            if not results:
                return {
                    "status": "success",
                    "message": "No papers found for this query on ArXiv.",
                    "data": []
                }

            return {
                "status": "success",
                "data": results
            }

        except Exception as e:
            wait_time = 2 ** attempt
            print(f"⚠️ Attempt {attempt + 1} failed: {e}")

            if attempt < retries - 1:
                print(f"⏳ Retrying in {wait_time} seconds...")
                time.sleep(wait_time)
            else:
                return {
                    "status": "error",
                    "message": f"Error executing ArXiv search after {retries} attempts: {str(e)}"
                }


import json

# result = arxiv_search('ti: "Attention Is All You Need"', max_results=1)
# print(json.dumps(result, indent=2))

from google.adk.agents.llm_agent import Agent

arxiv_search_agent = Agent(
    model=os.environ.get("MODEL"),
    name="arxiv_search_agent",
    instruction="Search ArXiv for related papers using the given query and summarize the results as structured JSON, extracting titles, authors, and summary links.",
    output_key="arxiv_results",
    tools=[arxiv_search],
)
