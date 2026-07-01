import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from services.git import GitService


def test_status():
    git = GitService()
    result = git.status()

    assert result["returncode"] == 0
    assert "On branch" in result["stdout"]
