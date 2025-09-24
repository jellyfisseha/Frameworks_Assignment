# 📊 Frameworks_Assignment  

This project explores the **CORD-19 metadata dataset** using:  
- **Pandas** → data analysis  
- **Matplotlib / Seaborn** → visualization  
- **Streamlit** → interactive web app  

---

## 🚀 How to Run  

### 1. Clone the repository  
```bash
git clone https://github.com/jellyfisseha/Frameworks_Assignment.git
cd Frameworks_Assignment
2. Install dependencies
bash
Copy code
pip install -r requirements.txt
3. Download the dataset
Due to GitHub’s file size limit, the dataset is not included in this repo.
Download metadata.csv from Kaggle:
👉 https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge

Place the file inside the data/ folder:

bash
Copy code
Frameworks_Assignment/data/metadata.csv
4. Run the analysis script
bash
Copy code
python notebooks/analysis.py
5. Run the Streamlit app
bash
Copy code
python -m streamlit run app/app.py
Then open in your browser: http://localhost:8501

📂 Project Structure
bash
Copy code
Frameworks_Assignment/
├── app/               # Streamlit app + generated plots
├── data/              # dataset (metadata.csv)
├── notebooks/         # Jupyter / Python analysis
├── requirements.txt   # dependencies
└── README.md          # project documentation
📊 Features
Load & clean CORD-19 metadata dataset

Explore publication trends by year

Identify top journals publishing COVID-19 research

Generate a word cloud of paper titles

Interactive Streamlit app for exploration

📝 Reflection
This assignment gave me the opportunity to work through the end-to-end data science workflow:

Data Loading & Cleaning: I learned how to handle a large real-world dataset (CORD-19), manage missing values, and transform columns like dates and abstracts.

Exploration & Visualization: I practiced creating meaningful plots (publications by year, top journals) and text analysis (word cloud of titles).

Building an App: I developed a simple Streamlit application to make my analysis interactive, which helped me understand how data insights can be shared with others.

Challenges
Handling the large dataset size — GitHub file size limits meant I had to exclude the raw CSV and document how to download it instead.

Path issues when running scripts from different folders — I learned how to use relative paths correctly.

Learning Outcome
I now feel more confident in using Pandas, Matplotlib, Seaborn, and Streamlit together to create an end-to-end data analysis project.
I also practiced version control with Git and GitHub.

Overall, this assignment improved both my technical data analysis skills and my ability to package and share work professionally through GitHub.

