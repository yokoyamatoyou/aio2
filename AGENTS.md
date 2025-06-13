# AI Agent Instructions

This repository contains a Streamlit based application for SEO and AIO analysis. The project uses a modular structure under `core/` and includes unit tests in `tests/`.

## Running Tests

Run unit tests with:

```bash
python -m unittest discover tests
```

## Key Files

- `seo_aio_streamlit.py` – main Streamlit app with PDF generation and analysis logic.
- `core/` – helper modules (`constants.py`, `industry_detector.py`, `text_utils.py`, `visualization.py`, `ui_components.py`).
- Documentation is provided in Japanese:
  - `コーディングAIシステム リファクタリング計画概要.md`
  - `コーディングAIシステム詳細指示フェーズ別.txt`

These documents outline a multi-phase refactoring plan. The phases are:

1. **Foundation & Modularization** – Split current code into logical modules, create utilities, and enforce single-responsibility.
2. **UI/UX Refresh** – Apply an Intel-inspired design with `#00C7FD` as primary and `#0068B5` as secondary colors. Use geometric pictogram icons. Provide components for buttons, forms, etc.
3. **Report Personalization** – Enhance the report with URL-based analysis and remove unnecessary meter-like UI elements.
4. **PDF Improvements** – Include SEO/AIO results, apply page breaks, and handle mojibake in titles/descriptions.
5. **Individual Page Adjustments & Unified Report** – Localize graphs to Japanese, adopt an Accenture-like report style, and expand textual explanations.
6. **Final Testing & Release Prep** – Comprehensive tests, usability review, document updates, and deployment procedures.

## Coding Style

- Python code should be UTF‑8 encoded and include minimal comments in English or Japanese.
- Ensure added modules or functions have straightforward names and docstrings.

## Environment

The application requires Streamlit, Plotly and ReportLab. Dependencies may be installed via:

```bash
pip install -r requirements.txt
```

Set the `OPENAI_API_KEY` environment variable or provide a `.env` file before running the Streamlit app.

