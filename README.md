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

## Setup Instructions

1. **Install dependencies:**
   Ensure you have Python installed, then install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up API keys:**
   Depending on the tools configured (like Google Search or Semantic Scholar), you may need to set environment variables. Set them in your shell or a `.env` file before running the ADK.

## Available Sub-Agents
* `arxiv_search_agent`: Finds relevant papers on ArXiv.
* `pdf_parser_agent`: Extracts and summarizes content from PDF URLs or local files.
* `citation_graph_agent`: Maps backward and forward citations for papers.
* `semantic_scholar_search`: Explores academic literature.
* `google_search_agent`: Fetches recent news and discussions.
* `conference_rules_agent`: Retrieves formatting constraints for major ML conferences.

## Usage & Examples

### Using the Terminal (`adk run subagents`)
Once the agent starts, you will get an interactive prompt. You can provide instructions to instruct the `root_agent` to use multiple tools. 

#### Example Prompt to Test All Agents
You can use the following comprehensive prompt to test the integration of all sub-agents:

> "Search arXiv for the latest papers on 'Large Language Models Agentic Workflows'. Pick the most relevant paper and download/parse its PDF to summarize its key contributions. Then, fetch its citation graph to find backward and forward citations. If possible, use Semantic Scholar to gather more context on its authors, and run a Google Search to see if there's any recent news or discussion about it. Finally, check formatting rules for the next NeurIPS conference to see if this paper aligns with their page limits."

### Using the Web Interface (`adk web subagents`)
You can access the generated web interface (usually at a local URL like `http://localhost:8000`).
The UI allows you to chat with the agent similarly, but with a richer interface.
