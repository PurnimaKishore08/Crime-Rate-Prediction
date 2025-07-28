### ✅ 2. `visualizations.py`

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def plot_trend(df):
    yearly_cols = [col for col in df.columns if col.isdigit()]
    df_trend = df[yearly_cols].sum().reset_index()
    df_trend.columns = ['Year', 'Total Crimes']
    plt.figure(figsize=(10, 5))
    sns.lineplot(data=df_trend, x='Year', y='Total Crimes', marker='o')
    plt.xticks(rotation=45)
    plt.title("Total Crimes Over the Years")
    st.pyplot(plt)


def plot_heatmap(df):
    yearly_cols = [col for col in df.columns if col.isdigit()]
    df_heat = df.set_index('State/UT')[yearly_cols]
    plt.figure(figsize=(12, 8))
    sns.heatmap(df_heat, cmap="Reds", annot=True, fmt=".0f")
    plt.title("Heatmap of Crimes by State and Year")
    st.pyplot(plt)


def plot_bar_chart(df):
    df['Total'] = df[[col for col in df.columns if col.isdigit()]].sum(axis=1)
    df_sorted = df.sort_values('Total', ascending=False)
    plt.figure(figsize=(12, 6))
    sns.barplot(data=df_sorted, x='Total', y='State/UT', palette="viridis")
    plt.title("Total Crimes by State")
    st.pyplot(plt)


def plot_pie_chart(df):
    df['Total'] = df[[col for col in df.columns if col.isdigit()]].sum(axis=1)
    top_states = df.nlargest(5, 'Total')
    plt.figure(figsize=(8, 8))
    plt.pie(top_states['Total'], labels=top_states['State/UT'], autopct='%1.1f%%', startangle=140)
    plt.title("Top 5 States with Highest Crimes")
    st.pyplot(plt)