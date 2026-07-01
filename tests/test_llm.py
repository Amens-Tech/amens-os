import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from core.services.llm import LLM


def test_load_prompt():

    llm = LLM()

    prompt = llm.load_prompt("sofiane")

    assert "CTO of Amens Tech" in prompt
