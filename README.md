# Covid19-Insights-Dashboard
This repository contains an interactive Power BI dashboard built using the Covid-19 World dataset. The project demonstrates how business insights can be derived from sales data through data cleaning, visualization, and analysis. This dashboard provides insights into World Covid-19 datasets. 

## Features
- KPI Cards showing:
  * Total Deaths
  * Total Population
  * Total Cases
- Pie Chart – Distribution of deaths across countries/locations
- Trend Analysis – COVID-19 spread over time

## Objective
- To analyze the impact of COVID-19 worldwide, understand trends in cases and deaths, and compare across countries and populations using data visualization techniques.

## Tech Stack
- Power BI (dashboard creation & visualization)
- Python – Preprocessing and handling missing values
- COVID-19 Dataset (collected from Kaggle)

## Steps Followed

### 🔗 Dataset
- This dataset is downloaded from kaggle.
- You can easily download it from Python script itself given with link to download the dataset.

### 🧹 Data Preprocessing
- Raw dataset was cleaned using Python (pandas, numpy).
- Steps included handling missing values, Removing dupliactes, and removing null categorical columns.
- Script included in `covid.py` for reference.

### 📊 Data Visualization (Power BI)
- Import cleaned_covid.csv into Power BI
- Build dashboard with:
- KPI Cards → Total Cases, Total Deaths, Total Population
- Pie Chart → Location-wise Death Distribution
- Line Chart → Cases Over Time
- Bar Chart → Top 10 Countries by Cases

### 📷 Dashboard Screenshot
<img width="1268" height="702" alt="Covid Dashboard" src="https://github.com/user-attachments/assets/9e6849c3-e002-4a69-9245-60b5ba3e12c8" />

### 📈 Key Insights
- Countries with higher populations didn’t always have the highest deaths.
- Death % varied significantly across locations.
- Cases followed clear waves over time → helps track policy impacts.

## Contributions
- Feel free to fork, improve, add features or difficulty levels, and submit pull requests!

## License
- This project is open source and available under the MIT License.
