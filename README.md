# aio2

This repository contains a Streamlit application for combined SEO and AIO (AI search optimization) analysis.

## Usage

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   *(Streamlit, Plotly, ReportLab and other libraries are required)*

2. Set your OpenAI API key via environment variable `OPENAI_API_KEY` or by creating a `.env` file.

3. Launch the application:
   ```bash
   streamlit run seo_aio_streamlit.py
   ```
4. Run a quick syntax check (optional but recommended):
   ```bash
   python -m py_compile $(git ls-files '*.py')
   ```
5. Execute the unit tests:
   ```bash
   python -m unittest discover tests
   ```

## Modules

The code has been modularized:

- `core/constants.py` – application constants and color settings.
- `core/industry_detector.py` – industry detection utilities.
- `core/visualization.py` – helper functions for charts.

The main `seo_aio_streamlit.py` script imports these modules.

## Features

- Japanese-labeled SEO score graphs for better clarity.
- Enhanced PDF reports with actionable insights and modern styling.
- Added conclusion and next-steps section in PDF reports.
