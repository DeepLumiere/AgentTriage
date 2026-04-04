from google.adk.agents.llm_agent import Agent
from google.adk.tools import google_search
import os
conference_rules_agent = Agent(
    model=os.environ.get("MODEL"),
    name="conference_rules_agent",
    instruction="Use Google Search to find and extract the submission guidelines for a requested academic conference or journal. Extract formatting rules such as max pages, blind submission requirements, fonts, and template links into strict JSON format.",
    output_key="conference_guidelines",
    tools=[google_search],
)

