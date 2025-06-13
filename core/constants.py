# -*- coding: utf-8 -*-
"""Application-wide constants."""

APP_VERSION = "3.0.0"
APP_NAME = "SEO・AIO統合分析ツール"

# グレー基調カラーパレット
COLOR_PALETTE = {
    "primary": "#2C2C2C",
    "secondary": "#3C3C3C",
    "accent": "#4A9EFF",
    "background": "#E8E8E8",
    "surface": "#F5F5F5",
    "text_primary": "#1A1A1A",
    "text_secondary": "#4A4A4A",
    "success": "#4CAF50",
    "warning": "#FF9800",
    "error": "#F44336",
    "info": "#2196F3",
    "gold": "#FF8C00",
    "dark_blue": "#1565C0",
}

# AIOスコアマッピング
AIO_SCORE_MAP_JP_UPPER = {
    "experience": "経験 (Experience)",
    "expertise": "専門性 (Expertise)",
    "authoritativeness": "権威性 (Authoritativeness)",
    "trustworthiness": "信頼性 (Trustworthiness)",
    "structure": "構造化と整理",
    "qa_compatibility": "質問応答適合性",
    "citation_potential": "AIによる引用可能性",
    "multimodal": "マルチモーダル対応",
}

AIO_SCORE_MAP_JP_LOWER = {
    "search_intent": "検索意図マッチング",
    "personalization": "ーソナライズ可能性",
    "uniqueness": "情報の独自性",
    "completeness": "コンテンツの完全性",
    "readability": "読みやすさスコア",
    "mobile_friendly": "モバイル対応性",
    "page_speed": "ページ速度",
    "metadata": "メタデータ最適化",
}

AIO_SCORE_MAP_JP = {**AIO_SCORE_MAP_JP_UPPER, **AIO_SCORE_MAP_JP_LOWER}
