# Climate Challenge Week 0

## Setup Instructions
- Python environment setup using venv
- Install dependencies using requirements.txt
- Run CI using GitHub Actions workflow

## Project Structure
- src/
- notebooks/
- tests/
- scripts/
## 📊 Ethiopia Climate EDA

This project analyzes Ethiopia’s climate dataset using NASA climate data.

### 🔹 Steps Performed:
- Data loading and cleaning (-999 handling)
- Feature engineering (DATE, MONTH)
- Missing value analysis
- Duplicate removal
- Outlier detection using Z-score
- Time series analysis (temperature & rainfall)
- Correlation analysis
- Data visualization

### 🔥 Key Insights:
- Ethiopia has a tropical highland climate
- Temperature is stable with small variation (~4°C)
- Rainfall is strongly seasonal (monsoon pattern)
- Most days are dry with occasional heavy rainfall events
- Humidity strongly follows rainfall patterns

### 📁 Output:
- Clean dataset exported as `ethiopia_clean.csv`
- Full EDA notebook available in `/notebooks`