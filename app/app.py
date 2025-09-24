import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Tell panda not to warn about mixed types
pd.options.mode.chained_assignment = None  # default='warn'
df = pd.read_csv("data/metadata.csv", low_memory=False) 

st.title("CORD-19 Data Explorer")
st.write("Interactive exploration of COVID-19 research papers")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("data/metadata.csv")
    df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
    df['year'] = df['publish_time'].dt.year
    df['journal'] = df['journal'].fillna("Unknown")
    return df

df = load_data()

# Sidebar filters
year_range = st.slider("Select year range", int(df['year'].min()), int(df['year'].max()), (2019, 2021))
filtered = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

st.write(f"Showing {len(filtered)} papers between {year_range[0]} and {year_range[1]}")

# Publications by year
st.subheader("📊 Publications by Year")
year_counts = filtered['year'].value_counts().sort_index()
st.bar_chart(year_counts)

# Top journals
st.subheader("🏢 Top Journals")
top_journals = filtered['journal'].value_counts().head(10)
st.bar_chart(top_journals)

# Show sample data
st.subheader("📑 Sample Data")
st.dataframe(filtered[['title', 'journal', 'year']].head(20))
