# -*- coding: utf-8 -*-
"""Helper for generating industry-specific advice."""
from typing import List
from .industry_detector import INDUSTRY_CONTENTS, get_industry_display_name


def generate_actionable_advice(missing_keywords: List[str], industry: str) -> str:
    """Return advice string based on missing keywords and industry.

    If industry is known, use its display name. Otherwise provide generic guidance.
    """
    if not missing_keywords:
        return "特に不足している重要キーワードは見当たりません。"

    info = INDUSTRY_CONTENTS.get(industry)
    joined = "、".join(missing_keywords)
    if info:
        display = get_industry_display_name(industry)
        return (
            f"{display}のサイトとして、見込み客が求める『{joined}』に関する情報が不足しているようです。"
            "これらのコンテンツを追加することで、サイトの信頼性が向上し、受注機会の増加につながります。"
        )
    return (
        "サイトのコンテンツが少ないため、業種を特定できませんでした。"
        "事業内容、サービス、会社情報などを具体的に記述し、コンテンツを充実させることを強くお勧めします。"
    )
