
import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Load metrics from CSV
metrics_df = pd.read_csv("manager_metrics_updated.csv")

# Identify benchmark row
benchmark_mask = metrics_df["Manager"] == "Benchmark Index"

# Function to create chart
def create_chart(metric_name):
    colors = ["red" if is_benchmark else "blue" for is_benchmark in benchmark_mask]
    fig = go.Figure(data=[
        go.Bar(x=metrics_df["Manager"], y=metrics_df[metric_name], marker_color=colors)
    ])
    fig.update_layout(title=f"{metric_name} Comparison", xaxis_title="Manager", yaxis_title=metric_name)
    return fig

# Streamlit layout
st.set_page_config(page_title="Equity Portfolio Performance Dashboard", layout="wide")
st.title("Equity Portfolio Management Performance Metrics")

# Tabs
tab1, tab2, tab3, tab4 = st.tabs(["Alpha", "Active Share", "Sharpe Ratio", "Annualized Return"])

with tab1:
    st.subheader("Alpha (%)")
    st.markdown("""
    **Formula:** \( lpha = R_p - R_b \)  
    **Explanation:** Measures the excess return of a portfolio over the benchmark. Positive alpha indicates outperformance.
    """)
    st.plotly_chart(create_chart("Alpha"), use_container_width=True)

with tab2:
    st.subheader("Active Share (%)")
    st.markdown("""
    **Formula:** \( 	ext{Active Share} = rac{1}{2} \\sum |w_{p,i} - w_{b,i}| \)  
    **Explanation:** Indicates how much the portfolio holdings differ from the benchmark. Higher values suggest more active management.
    """)
    st.plotly_chart(create_chart("Active Share"), use_container_width=True)

with tab3:
    st.subheader("Sharpe Ratio (%)")
    st.markdown("""
    **Formula:** \( 	ext{Sharpe Ratio} = rac{R_p - R_f}{\\sigma_p} \)  
    **Explanation:** Measures risk-adjusted return. Higher values indicate better performance per unit of risk.
    """)
    st.plotly_chart(create_chart("Sharpe Ratio"), use_container_width=True)

with tab4:
    st.subheader("Annualized Return (%)")
    st.markdown("""
    **Formula:** \( 	ext{Annualized Return} = (1 + R_m)^{12} - 1 \)  
    **Explanation:** Converts monthly return to yearly compounded return.
    """)
    st.plotly_chart(create_chart("Annualized Return"), use_container_width=True)
