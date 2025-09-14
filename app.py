
import streamlit as st
import pandas as pd
import plotly.io as pio

# Load updated metrics
metrics_df = pd.read_csv("manager_metrics_updated.csv")

# Load updated charts with benchmark in red
alpha_chart = pio.read_json("alpha_chart_red.json")
active_share_chart = pio.read_json("active_share_chart_red.json")
sharpe_ratio_chart = pio.read_json("sharpe_ratio_chart_red.json")
annual_return_chart = pio.read_json("annualized_return_chart_red.json")

# Streamlit app layout
st.set_page_config(page_title="Equity Portfolio Performance Dashboard", layout="wide")
st.title("Equity Portfolio Management Performance Metrics")

# Create tabs
tab1, tab2, tab3, tab4 = st.tabs(["Alpha", "Active Share", "Sharpe Ratio", "Annualized Return"])

with tab1:
    st.subheader("Alpha (%)")
    st.markdown("""
    **Formula:** \( lpha = R_p - R_b \)  
    **Explanation:** Measures the excess return of a portfolio over the benchmark. Positive alpha indicates outperformance.
    """)
    st.plotly_chart(alpha_chart, use_container_width=True)

with tab2:
    st.subheader("Active Share (%)")
    st.markdown("""
    **Formula:** \( 	ext{Active Share} = rac{1}{2} \sum |w_{p,i} - w_{b,i}| \)  
    **Explanation:** Indicates how much the portfolio holdings differ from the benchmark. Higher values suggest more active management.
    """)
    st.plotly_chart(active_share_chart, use_container_width=True)

with tab3:
    st.subheader("Sharpe Ratio (%)")
    st.markdown("""
    **Formula:** \( 	ext{Sharpe Ratio} = rac{R_p - R_f}{\sigma_p} \)  
    **Explanation:** Measures risk-adjusted return. Higher values indicate better performance per unit of risk.
    """)
    st.plotly_chart(sharpe_ratio_chart, use_container_width=True)

with tab4:
    st.subheader("Annualized Return (%)")
    st.markdown("""
    **Formula:** \( 	ext{Annualized Return} = (1 + R_m)^{12} - 1 \)  
    **Explanation:** Converts monthly return to yearly compounded return.
    """)
    st.plotly_chart(annual_return_chart, use_container_width=True)
