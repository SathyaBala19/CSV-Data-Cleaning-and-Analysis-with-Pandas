# CSV-Data-Cleaning-and-Analysis-with-Pandas

# CSV Data Cleaning and Analysis with Pandas

## 📌 Project Overview

This project demonstrates how to clean and analyze CSV data using Python and Pandas. The dataset contains missing values, duplicate records, invalid data, and different data types. The goal is to transform the raw data into a clean and usable dataset.

## 🛠 Technologies Used

* Python
* Pandas

## 📂 Dataset Issues

The sample dataset contains:

* Missing values
* Duplicate records
* Invalid data (`abc` in marks column)
* Mixed data types

## 🚀 Steps Performed

### 1. Read CSV File

Loaded the CSV file using Pandas.

```python
df = pd.read_csv("students.csv")
```

### 2. Identify Missing Values

Checked null values in each column.

```python
df.isnull().sum()
```

### 3. Detect Duplicate Records

Found duplicate rows using Pandas.

```python
df.duplicated()
```

### 4. Remove Duplicates

Removed duplicate student records.

```python
df.drop_duplicates()
```

### 5. Convert Data Types

Converted the marks column to numeric values.

```python
pd.to_numeric(df["marks"], errors="coerce")
```

### 6. Handle Missing Values

Filled missing values using appropriate methods.

* Name → "Unknown"
* City → "Not Available"
* Age → Average Age
* Marks → Average Marks

### 7. Data Analysis

Performed:

* Average Marks
* Highest Marks
* Lowest Marks
* Topper Identification
* Student Count
* City-wise Analysis

### 8. Sort Data

Sorted students based on marks.

```python
df.sort_values(by="marks", ascending=False)
```

### 9. Export Cleaned Data

Saved the cleaned dataset to a new CSV file.

```python
df.to_csv("cleaned_students.csv", index=False)
```

## 📊 Learning Outcomes

Through this project, I learned:

* Reading CSV files with Pandas
* Handling missing values
* Detecting and removing duplicates
* Data type conversion
* Data cleaning techniques
* Data analysis using Pandas
* Grouping and sorting data
* Exporting cleaned datasets

## 📁 Project Structure

```text
CSV-Data-Cleaning-and-Analysis-with-Pandas/
│
├── students.csv
├── cleaned_students.csv
├── clean_csv.py
└── README.md
```

## 🎯 Conclusion

This project helped me understand the complete data cleaning workflow using Pandas. It covers common real-world data quality issues and demonstrates how to prepare data for further analysis.
