# -*- coding: utf-8 -*-
"""Helper for generating industry-specific advice."""
from typing import List
from .industry_detector import INDUSTRY_CONTENTS


def generate_actionable_advice(missing_keywords: List[str], industry: str) -> str:
    """Return advice string based on missing keywords and industry.

    If industry is known, use its display name. Otherwise provide generic guidance.
    """
    if not missing_keywords:
        return "特に不足している重要キーワードは見当たりません。"

    info = INDUSTRY_CONTENTS.get(industry)
    display = info["display_name"] if info else "サイト"
    joined = "、".join(missing_keywords)
    if info:
        return f"{display}向けに『{joined}』に関する情報を追加すると効果的です。"
    return f"関連性の高い内容（例: {joined}）をページに盛り込むことを検討してください。"
