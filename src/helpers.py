"""
Helper functions.
"""

def is_float(string: str) -> float:
    try:
        return float(string)
    except ValueError:
        return None
