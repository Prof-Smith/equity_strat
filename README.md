
# Equity Portfolio Management Performance Dashboard

This Streamlit app allows students to explore equity portfolio management strategies by comparing the performance of five hypothetical fund managers against a benchmark index.

## Features
- Visualize monthly return series
- Compare Alpha, Active Share, Sharpe Ratio, and Annualized Return
- Benchmark index is highlighted in red for clarity
- Educational tooltips explain each metric with formulas

## How to Run
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Launch the app:
   ```bash
   streamlit run app.py
   ```

## Tabs Overview
- **Alpha**: Measures excess return over the benchmark
- **Active Share**: Indicates portfolio deviation from the benchmark
- **Sharpe Ratio**: Evaluates risk-adjusted return
- **Annualized Return**: Converts monthly return to yearly performance
