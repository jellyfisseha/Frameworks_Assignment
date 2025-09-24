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
3. Run the analysis script
bash
Copy code
python notebooks/analysis.py
4. Run the Streamlit app
bash
Copy code
python -m streamlit run app/app.py
Open in your browser at http://localhost:8501.

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