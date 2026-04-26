📄 Interim Report
🔹 Task 1: Git & Environment Setup
Created GitHub repository: climate-challenge-week0
Set up Python virtual environment using venv
Installed dependencies using requirements.txt
Structured project into modular folders (src, notebooks, scripts, tests)
Created Git branches (setup-task, eda-ethiopia)
Implemented CI pipeline using GitHub Actions to automate dependency installation and testing
Followed conventional commit messages for version control
Merged setup-task branch into main after completing setup
🔹 Task 2: Data Profiling and Cleaning Approach
Created separate branch: eda-ethiopia
Loaded Ethiopia climate dataset using pandas
Replaced missing sentinel values (-999) with NaN
Converted YEAR and DOY into proper datetime format
Extracted MONTH feature for seasonal analysis
Performed data quality checks:
Missing value analysis
Duplicate removal
Applied outlier detection using Z-score method
Handled missing values using forward fill and row filtering strategy
Conducted exploratory data analysis:
Time series trends (temperature & rainfall)
Correlation analysis
Distribution analysis
Generated insights on Ethiopia’s climate patterns