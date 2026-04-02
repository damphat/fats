import json
import sys
from pathlib import Path

# Add src to sys.path so we can import 'fats' directly without installing it
# This makes local development extremely fast.
sys.path.insert(0, str(Path(__file__).parent / "src"))


def pretty(d):
    o = {k: str(v)[:40] for k, v in d.items()}
    print(json.dumps(o, indent=2))


import fats

fats.interact()
