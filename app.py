import streamlit as st
import pandas as pd
from prediction_model import predict_crime_rate
from visualizations import plot_trend, plot_heatmap, plot_bar_chart, plot_pie_chart

# 🎨 Set wide layout and page configs
st.set_page_config(page_title="🔐 Crime Rate Prediction", layout="wide", initial_sidebar_state="expanded")

# 🌃 Apply a background color using markdown and inline CSS
st.markdown("""
    <style>
        .main {
            background-color: #0f1117;
            color: #f5f5f5;
            padding: 1.5rem;
        }
        .block-container {
            padding-top: 2rem;
        }
        .stDataFrame, .stTable {
            background-color: #1c1e25;
        }
    </style>
""", unsafe_allow_html=True)

# 🚀 Title Section
st.title("🔐 Crime Rate Prediction Dashboard")

# 📁 Sidebar for file upload
with st.sidebar:
    st.header("📂 Upload Dataset")
    uploaded_file = st.file_uploader("Upload your crime dataset (CSV)", type=["csv"])
    st.markdown("---")
    st.info("Dataset should include 'State/UT', year-wise data (2020–2022), and optionally population.")

# 🧠 Main Content
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success("✅ Dataset uploaded successfully!")
    st.dataframe(df, use_container_width=True)

    st.markdown("## 📊 Data Visualizations")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 🔹 Crime Trends Over Time")
        try:
            plot_trend(df)
        except Exception as e:
            st.error(f"Error in trend plot: {e}")

    with col2:
        st.markdown("### 🔹 Crime Heatmap")
        try:
            plot_heatmap(df)
        except Exception as e:
            st.error(f"Error in heatmap: {e}")

    col3, col4 = st.columns(2)
    with col3:
        st.markdown("### 🔹 Crime by State (Bar Chart)")
        try:
            plot_bar_chart(df)
        except Exception as e:
            st.error(f"Error in bar chart: {e}")

    with col4:
        st.markdown("### 🔹 Crime Composition (Pie Chart)")
        try:
            plot_pie_chart(df)
        except Exception as e:
            st.error(f"Error in pie chart: {e}")

    st.markdown("---")
    st.markdown("## 🔮 Predict Next Year's Crime Rate")
    state = st.selectbox("Choose a State/UT", df['State/UT'].unique())
    if st.button("Predict"):
        try:
            forecast = predict_crime_rate(df, state)
            st.success(f"📈 Predicted crime count for next year in {state}: **{forecast:.2f}**")
        except Exception as e:
            st.error(f"Prediction error: {e}")
else:
    st.warning("📌 Please upload a dataset to get started.")
