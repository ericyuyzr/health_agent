import re
from typing import Any


def extract_concise_from_text(text: str) -> str:
    """Extract a short, useful recommendation summary from model text using regex.

    Tries several patterns (Recommendation block, Summary block) and falls
    back to returning the first 3 short lines found.
    """
    if not text:
        return ""

    # Pattern 1: **Recommendation**: block
    m = re.search(r"\*\*Recommendation\*\*:\s*(.+?)(?:\n\n|\Z)", text, re.S | re.I)
    if m:
        return _clean_lines(m.group(1))

    # Pattern 2: **Summary:** block
    m = re.search(r"\*\*Summary\*\*:\s*(.+?)(?:\n\n|\Z)", text, re.S | re.I)
    if m:
        return _clean_lines(m.group(1))

    # Pattern 3: look for lines starting with '-' or bullets and take top 4
    bullets = re.findall(r"^\s*[-•*]\s*(.+)$", text, re.M)
    if bullets:
        return "; ".join(bullets[:4])

    # Fallback: take first 3 non-empty lines
    lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
    return " ".join(lines[:3])


def extract_concise(response: Any) -> str:
    """Accept a response object (string or nested) and return concise text.

    We stringify unknown objects and pass to regex extractor.
    """
    if isinstance(response, str):
        text = response
    else:
        try:
            text = str(response)
        except Exception:
            text = ""
    return extract_concise_from_text(text)


def _clean_lines(block: str) -> str:
    """Clean and join lines into a short recommendation string."""
    lines = [ln.strip() for ln in block.splitlines() if ln.strip()]
    # Remove leading bullets or numbering
    cleaned = [re.sub(r"^[\-\d\.\)\s]*", "", ln) for ln in lines]
    # Join with semicolons for compactness
    return "; ".join(cleaned)
