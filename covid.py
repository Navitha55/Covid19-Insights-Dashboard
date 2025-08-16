import pandas as pd
import kagglehub

# Download dataset with latest version
path = kagglehub.dataset_download("aditeloo/the-world-dataset-of-covid19")

df = pd.read_csv("./owid-covid-data.csv")

# Initial exploration
print(df.describe())
print(df.info())
print(df.head(10))

# Removing or dropping columns
df = df.drop(['new_cases','new_cases_smoothed','new_deaths','new_deaths_smoothed','total_cases_per_million','new_cases_per_million','new_cases_smoothed_per_million','total_deaths_per_million','new_deaths_per_million','new_deaths_smoothed_per_million','icu_patients','icu_patients_per_million','hosp_patients_per_million','weekly_icu_admissions','weekly_icu_admissions_per_million','weekly_hosp_admissions','weekly_hosp_admissions_per_million'], axis = 1)
df = df[['iso_code','continent','location','date','total_cases','total_deaths','reproduction_rate','hosp_patients','total_tests','positive_rate','total_vaccinations','people_fully_vaccinated','population','aged_65_older','extreme_poverty','life_expectancy','human_development_index']]  

# Missing Values check
print(df.isnull().sum())
num_cols = df.select_dtypes(include=['float64']).columns
df[num_cols] = df[num_cols].fillna(0)
cat_cols = df.select_dtypes(include=['object']).columns
df = df.drop(columns=[col for col in cat_cols if df[col].isnull().any()])

# Duplicates removal
df = df.drop_duplicates()

# Datatype Check
print(df.dtypes)
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# Saving the cleaned file

df.to_csv("covid_cleaned.csv", index=False)
