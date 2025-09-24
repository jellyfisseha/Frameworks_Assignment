# notebooks/analysis.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# -------------------
# Part 1: Load & Explore
# -------------------
print("🔹 Loading dataset...")
df = pd.read_csv("../data/metadata.csv", low_memory=False, nrows=5000)

print("\nShape:", df.shape)
print("\nInfo:")
print(df.info())
print("\nMissing values (top 10):")
print(df.isnull().sum().sort_values(ascending=False).head(10))

# -------------------
# Part 2: Data Cleaning
# -------------------
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
df['year'] = df['publish_time'].dt.year
df['abstract_word_count'] = df['abstract'].fillna("").str.split().str.len()
df['journal'] = df['journal'].fillna("Unknown")

# Drop rows missing title or publish_time
df = df.dropna(subset=['title', 'publish_time'])

# -------------------
# Part 3: Analysis & Visualizations
# -------------------

# 1. Publications by year
year_counts = df['year'].value_counts().sort_index()
plt.figure(figsize=(8,5))
sns.barplot(x=year_counts.index, y=year_counts.values, color="skyblue")
plt.title("Publications by Year")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("../app/plots_publications_by_year.png")
plt.close()

# 2. Top 10 journals
top_journals = df['journal'].value_counts().head(10)
plt.figure(figsize=(8,5))
sns.barplot(y=top_journals.index, x=top_journals.values, color="green")
plt.title("Top 10 Journals Publishing COVID-19 Research")
plt.tight_layout()
plt.savefig("../app/plots_top_journals.png")
plt.close()

# 3. Word cloud of paper titles
text = " ".join(df['title'].dropna().astype(str).tolist())
wc = WordCloud(width=800, height=400, background_color="white").generate(text)
wc.to_file("../app/plots_wordcloud_titles.png")

print("\n✅ Analysis complete. Plots saved inside the app/ folder.")
