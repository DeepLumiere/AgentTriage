from google.adk.agents.llm_agent import Agent
from google.adk.tools import AgentTool
from google.adk.tools import google_search
from .arxiv_search import arxiv_search, arxiv_search_agent
from .google_search import google_search_agent
from .semantic_search import semantic_scholar_search
from .pdf_parser import pdf_parser_agent
from .conference_rules import conference_rules_agent
from .citation_graph import citation_graph_agent
import os
root_agent = Agent(
    model=os.environ.get("MODEL"),
    name='root_agent',
    description="Orchestrate the search and writeups for the research paper.",
    instruction="""You are a research orchestration agent. 
If the user wants to research a paper or topic, you must:
1. Use arxiv_search_agent to find relevant papers.
2. If the user provides a PDF URL or file path, or if you found a PDF URL on ArXiv, use pdf_parser_agent to extract and summarize the PDF.
3. Use citation_graph_agent (with the necessary paper IDs) to fetch backward and forward citation references. 
Ensure you compile all of this information into a cohesive research summary.
""",
    tools=[
        AgentTool(google_search_agent),
        # AgentTool(arxiv_search_agent),
        AgentTool(pdf_parser_agent),
        AgentTool(conference_rules_agent),
        AgentTool(citation_graph_agent),
        arxiv_search,
        semantic_scholar_search
    ],
)
