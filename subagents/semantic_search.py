
import requests
import time
from typing import List, Dict, Any
import os
API_KEY = os.environ.get("SEMANTIC_SEARCH_API_KEY")
_last_request_time = 0


def _rate_limit():
    """
    Ensures at most 1 request per second globally.
    """
    global _last_request_time
    now = time.time()
    elapsed = now - _last_request_time

    if elapsed < 1.0:
        time.sleep(1.0 - elapsed)

    _last_request_time = time.time()

def semantic_scholar_search(
        query: str,
        max_results: int = 5,
        retries: int = 3
) -> Dict[str, Any]:
    """
    Search for research papers using Semantic Scholar API.

    Args:
        query (str): The search query.
        max_results (int): Maximum number of results to return.
        retries (int): Number of retry attempts on failure.

    Returns:
        dict: A dictionary containing the 'status' and the resulting 'data' or 'message'.
    """

    print(f"📡 [Semantic Scholar] Searching: '{query}'...")

    url = "https://api.semanticscholar.org/graph/v1/paper/search"

    headers = {
        "x-api-key": API_KEY
    }

    params = {
        "query": query,
        "limit": max_results,
        "fields": "title,authors,year,abstract,url,citationCount"
    }

    for attempt in range(retries):
        try:
            _rate_limit()

            response = requests.get(url, headers=headers, params=params)

            if response.status_code == 200:
                data = response.json()
                papers = data.get("data", [])

                if not papers:
                    return {
                        "status": "success",
                        "message": "No papers found.",
                        "data": []
                    }

                results: List[Dict[str, Any]] = []

                for paper in papers:
                    results.append({
                        "title": paper.get("title", "N/A"),
                        "authors": [a["name"] for a in (paper.get("authors") or [])],                        "year": paper.get("year", "N/A"),
                        "citations": paper.get("citationCount", 0),
                        "url": paper.get("url", "N/A"),
                        "abstract": (paper.get("abstract") or "").replace('\n', ' ')
                    })

                return {
                    "status": "success",
                    "data": results
                }

            elif response.status_code == 429:
                raise Exception("Rate limit exceeded (429)")

            else:
                raise Exception(f"HTTP {response.status_code}: {response.text}")

        except Exception as e:
            wait_time = max(2 ** attempt, 1)  # always >= 1 sec
            print(f"⚠️ Attempt {attempt + 1} failed: {e}")

            if attempt < retries - 1:
                print(f"⏳ Retrying in {wait_time} seconds...")
                time.sleep(wait_time)
            else:
                return {
                    "status": "error",
                    "message": f"Error after {retries} attempts: {str(e)}"
                }
