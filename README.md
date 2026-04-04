# ADK Research Agent

A comprehensive research orchestration agent built with Google ADK. It uses a `root_agent` to coordinate multiple subagents, allowing you to search arXiv, parse PDFs, fetch citation graphs, search Semantic Scholar or Google, and look up conference submission rules all in one place.

## How to Run

### Run in Terminal
To run the agent interactively in your terminal, use the following command:
```bash
adk run subagents
```

### Run on the Web
To launch the agent's web interface, use:
```bash
adk web subagents
```

---

*Note: A custom FastAPI streaming frontend is also included in this repository as an alternative to `adk web`. You can start it by running `python app.py` and navigating to `http://127.0.0.1:8000/`.*

## Available Sub-Agents
* `arxiv_search_agent`: Finds relevant papers on ArXiv.
* `pdf_parser_agent`: Extracts and summarizes content from PDF URLs or local files.
* `citation_graph_agent`: Maps backward and forward citations for papers.
* `semantic_scholar_search`: Explores academic literature.
* `google_search_agent`: Fetches recent news and discussions.
* `conference_rules_agent`: Retrieves formatting constraints for major ML conferences.

