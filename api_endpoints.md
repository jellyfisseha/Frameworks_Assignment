\# 📑 API Endpoints (Streamlit Features)



This project uses \*\*Streamlit\*\* for interactivity instead of a REST API.  

The following interactive features are available inside the Streamlit app.



---



\## 🔹 Home (`/`)

\- Displays project title and description.  

\- Explains the purpose of the app (exploring CORD-19 dataset).  



---



\## 🔹 Dataset Preview (`/dataset`)

\- Shows a sample of the dataset with the following columns:  

&nbsp; - Title  

&nbsp; - Authors  

&nbsp; - Journal  

&nbsp; - Year  



---



\## 🔹 Filters (`/filters`)

\- \*\*Year Range Slider\*\*:  

&nbsp; - Select a range of publication years (e.g., 2020–2021).  

&nbsp; - Dataset is filtered to show only papers published within the selected years.  



---



\## 🔹 Visualizations (`/visualizations`)

Interactive charts generated from the dataset:



1\. \*\*Publications by Year\*\*  

&nbsp;  - Bar chart of the number of papers published per year.  



2\. \*\*Top 10 Journals\*\*  

&nbsp;  - Horizontal bar chart of the top 10 journals publishing COVID-19 research.  



3\. \*\*Word Cloud of Paper Titles\*\*  

&nbsp;  - Word cloud showing the most frequent words in paper titles.  



---



\## ✅ Usage Notes

\- The dataset (`metadata.csv`) must be placed in the `data/` folder.  

\- Run the app with:  

&nbsp; ```bash

&nbsp; python -m streamlit run app/app.py



