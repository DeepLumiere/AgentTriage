from google.adk import Agent
from google.adk.tools import google_search
import sys


MODEL = "gemini-2.5-flash"

google_search_agent = Agent(
        model=MODEL,
        name="academic_websearch_agent",
        instruction="Websearch and give summary of paper in JSON of: title, author, year, summary, url. Use the 'google_search' tool to find recent papers citing a given paper.",
        output_key="recent_citing_papers",
        tools=[google_search],
    )