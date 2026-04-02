
import os
import sys
from pathlib import Path

project_root = Path(__file__).resolve().parents[1]
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

import config

SEMANTIC_SCHOLAR_API_KEY="edqGK2rKbUhEdMkgsJifiUd1LJRJNT27cHjcLya0"
GEMINI_API_KEY="AIzaSyB0JnuoOtfA3q6quHDhSWuWlBQF7XOsIt4"

def set_env():
    os.environ["SEMANTIC_SCHOLAR_API_KEY"] = SEMANTIC_SCHOLAR_API_KEY
    os.environ["GEMINI_API_KEY"] = GEMINI_API_KEY
