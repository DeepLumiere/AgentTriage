import requests
from google.adk.agents.llm_agent import Agent
import os
def fetch_citations(paper_id: str) -> dict:
    """Fetch citations using Semantic Scholar Graph API"""
    url = f"https://api.semanticscholar.org/graph/v1/paper/{paper_id}/citations?fields=title,authors,year"
    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        return r.json()
    except Exception as e:
        return {"error": str(e)}

citation_graph_agent = Agent(
    model=os.environ.get("MODEL"),
    name="citation_graph_agent",
    instruction="Fetch citation graphs for a given paper using Semantic Scholar. Output a structured JSON map of citation history backward and forward. For ArXiv papers, use 'ARXIV:<arxiv_id>' as the paper_id.",
    output_key="citation_graph",
    tools=[fetch_citations],
)
