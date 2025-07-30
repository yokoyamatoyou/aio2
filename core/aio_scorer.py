# -*- coding: utf-8 -*-
"""AIO scoring helpers."""
from typing import Dict, List, Tuple


def calculate_personalization_score(text: str, industry: str, industry_contents_map: Dict[str, Dict]) -> Tuple[float, List[str]]:
    """Return coverage score and missing recommended keywords."""
    if not text or industry not in industry_contents_map:
        return 0.0, []
    keywords: List[str] = industry_contents_map[industry].get('keywords', [])
    if not keywords:
        return 0.0, []
    text_lower = text.lower()
    missing: List[str] = []
    matched = 0
    for kw in keywords:
        if kw.lower() in text_lower:
            matched += 1
        else:
            missing.append(kw)
    score = (matched / len(keywords)) * 100 if keywords else 0.0
    return score, missing
