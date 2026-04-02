from google.adk.agents.llm_agent import Agent
from google.adk.tools import AgentTool
from google.adk.tools import google_search

from subagents.arxiv_search import arxiv_search
from subagents.google_search import google_search_agent

from subagents.semantic_search import semantic_scholar_search

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description="Orchestrate the search and writeups for the research paper.",
    instruction="",
    tools=[AgentTool(google_search_agent), arxiv_search, semantic_scholar_search],
)