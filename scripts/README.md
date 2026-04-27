# 🌍 Climate Change Analysis Dashboard (COP32 Project)

## 📌 Project Overview
This project analyzes climate data from five African countries: **Ethiopia, Kenya, Tanzania, Nigeria, and Sudan**.  

It explores temperature trends, precipitation patterns, and climate variability, and provides an interactive Streamlit dashboard for visualization and analysis.

---

## 🚀 How to Run the Project

### 1. Install dependencies
```bash
pip install -r requirements.txt
2. Run the dashboard
streamlit run app/main.py
📊 Features
🌡️ Temperature trend analysis over time
🌧️ Precipitation distribution comparison
📍 Country selection (multi-select filter)
📆 Year range slider
📈 Interactive climate dashboard visualization
📁 Project Structure
climate-challenge-week0/
│
├── data/                  # Raw datasets (ignored in Git)
├── app/
│   ├── main.py           # Streamlit dashboard
│   └── utils.py          # Data loading & preprocessing
├── notebooks/            # EDA and analysis notebooks
├── scripts/
├── requirements.txt
└── README.md
⚙️ Data Processing
Missing values (-999) are replaced with NaN
YEAR + DOY converted into proper datetime format
Additional features created: Year and Month
🧪 Technologies Used
Python
Pandas
Matplotlib
Streamlit