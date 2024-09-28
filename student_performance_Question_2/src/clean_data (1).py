import pandas as pd

# Load the dataset (raw data)
raw_data_path = '/content/sample_data/student/data_raw/students_performance.csv.csv'
df = pd.read_csv(raw_data_path)

# 1. Check for missing values and handle them
print("Missing values before cleaning:")
print(df.isnull().sum())

# Drop rows with missing values (if any)
df_cleaned = df.dropna()

# 2. Data type conversions (if necessary)
# Ensuring scores are numeric
df_cleaned['math score'] = pd.to_numeric(df_cleaned['math score'], errors='coerce')
df_cleaned['reading score'] = pd.to_numeric(df_cleaned['reading score'], errors='coerce')
df_cleaned['writing score'] = pd.to_numeric(df_cleaned['writing score'], errors='coerce')

# Re-check for any new missing values after conversion
df_cleaned = df_cleaned.dropna()

# 3. Handle outliers (for scores outside valid range)
# Assuming scores must be between 0 and 100
df_cleaned = df_cleaned[(df_cleaned['math score'] >= 0) & (df_cleaned['math score'] <= 100)]
df_cleaned = df_cleaned[(df_cleaned['reading score'] >= 0) & (df_cleaned['reading score'] <= 100)]
df_cleaned = df_cleaned[(df_cleaned['writing score'] >= 0) & (df_cleaned['writing score'] <= 100)]

# 4. Standardize categorical data (e.g., lunch type or parental level of education)
# Ensure consistent values in 'lunch' column (standardizing text)
df_cleaned['lunch'] = df_cleaned['lunch'].str.lower().str.strip()

# Mapping to standardize categorical values (if necessary)
df_cleaned['test preparation course'] = df_cleaned['test preparation course'].replace({'none': 'No', 'completed': 'Yes'})

# 5. Renaming columns for better readability (if necessary)
df_cleaned = df_cleaned.rename(columns={
    'race/ethnicity': 'ethnicity',
    'parental level of education': 'parental_education',
    'math score': 'math_score',
    'reading score': 'reading_score',
    'writing score': 'writing_score'
})

# 6. Save the cleaned data to a new CSV file
cleaned_data_path = '/content/sample_data/student/data_clean/cleaned_student_performance.csv'
df_cleaned.to_csv(cleaned_data_path, index=False)

print(f"Data cleaned and saved to {cleaned_data_path}.")
