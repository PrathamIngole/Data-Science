<div align="center">

# 🐼 The Pandas Master Reference Guide
### "Excel for Python on Steroids"

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-2.0%2B-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Status](https://img.shields.io/badge/Status-Educational-green?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

<p align="center">
  <b>A complete, end-to-end reference book for Data Manipulation.</b><br>
  From "Hello World" to Production-Grade Vectorization.
</p>

</div>

---

## 📖 Table of Contents
1. [The Core Structures](#1-the-core-structures)
2. [Input & Output (I/O)](#2-input--output-io)
3. [The First Look (Inspection)](#3-the-first-look-inspection)
4. [Selection & Filtering](#4-selection--filtering)
5. [Data Cleaning](#5-data-cleaning)
6. [Transformation](#6-transformation)
7. [Aggregation & Grouping](#7-aggregation--grouping)
8. [Merging & Joining](#8-merging--joining)
9. [Time Series](#9-time-series)
10. [Performance (Expert Zone)](#10-performance-expert-zone)

---

## ⚡ Quick Start

```python
import pandas as pd
import numpy as np

# Verify installation
print(f"Pandas Version: {pd.__version__}")

1. The Core Structures
The atoms of the library.

🔹 1.1 The Series (1D)
A single column of data with an index.
Note --> Series can be made of any data except set, frozenSet.
Note --> Series data is of 1-Dimensional. So passing 2-D elements will raise an error.  

s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print(s['a'])  # Output: 10

🔹 1.2 The DataFrame (2D)
A table of data (rows and columns).

data = {
    'Name': ['Alice', 'Bob'], 
    'Age': [25, 30]
}
df = pd.DataFrame(data)

2. Input & Output (I/O)
Getting data in and out.

Format             Read Command                            Write Command

CSV               pd.read_csv('file.csv')               df.to_csv('file.csv', index=False)
Excel             pd.read_excel('file.xlsx')            df.to_excel('file.xlsx')
JSON              pd.read_json('file.json')             df.to_json('file.json')
SQL               pd.read_sql(query, connection)        df.to_sql('table', connection)


Pro Tip: Always use index=False when saving to CSV unless the index contains valuable information.

3. The First Look (Inspection)
Never fly blind. Inspect immediately.

df.head()          # First 5 rows
df.tail()          # Last 5 rows
df.sample(5)       # Random 5 rows
df.shape           # (Rows, Columns) tuple
df.columns         # List of column names


🔍 Crucial Inspections

df.info()          # Data types & Non-null counts
df.describe()      # Statistical summary (Mean, Max, Min)

4. Selection & Filtering
The "loc" vs "iloc" battle.

🎯 4.1 Column Selection

age = df['Age']              # Returns Series
subset = df[['Name', 'Age']] # Returns DataFrame

🎯 4.2 Row Selection (.loc vs .iloc)

Method	Type	Syntax	Example
.loc	Label based	[row_name, col_name]	df.loc[5, 'City']
.iloc	Integer based	[row_pos, col_pos]	df.iloc[0, 2]

🎯 4.3 Boolean Filtering

# Simple Condition
adults = df[df['Age'] > 18]

# Multiple Conditions (Note the parentheses!)
target = df[(df['Age'] > 18) & (df['City'] == 'London')]

# The .isin() method (Cleaner than multiple ORs)
cities = df[df['City'].isin(['London', 'Paris', 'Tokyo'])]

5. Data Cleaning
The 80/20 rule: 80% of your time is spent here.

🧹 5.1 Missing Data (NaN)

df.isnull().sum()          # Count missing values per column
df.dropna()                # Drop rows with ANY nulls
df.fillna(value=0)         # Fill with specific value
df.fillna(df.mean())       # Fill with average (Imputation)

🧹 5.2 Duplicates

df.duplicated().sum()      # Check for duplicates
df.drop_duplicates()       # Remove duplicates

6. Transformation

🛠 6.1 The .apply() Method
Apply a function to every element.

def to_fahrenheit(x):
    return (x * 1.8) + 32

df['Temp_F'] = df['Temp_C'].apply(to_fahrenheit)

🛠 6.2 String Manipulation (.str)

df['Name'] = df['Name'].str.upper()               # Uppercase
df['Tech_Job'] = df['Job'].str.contains('Data')   # Boolean search

7. Aggregation & Grouping
The "Pivot Tables" of Python.

Syntax: df.groupby('Categorical')['Numerical'].func()

# Average salary by Department
df.groupby('Department')['Salary'].mean()

# Multiple Stats
df.groupby('Department')['Salary'].agg(['mean', 'sum', 'max'])

# Value Counts (Frequency)
df['City'].value_counts()

8. Merging & Joining
SQL-style joins.

# Concatenation (Stacking)
combined = pd.concat([df1, df2], axis=0)

# Merging (Joining)
# 'how' options: 'inner', 'outer', 'left', 'right'
merged = pd.merge(df_users, df_orders, on='user_id', how='left')

9. Time Series
Handling dates like a pro.

# 1. Convert to DateTime (CRITICAL STEP)
df['Date'] = pd.to_datetime(df['Date'])

# 2. Extract features using .dt accessor
df['Month'] = df['Date'].dt.month
df['Day_Name'] = df['Date'].dt.day_name()

10. Performance (Expert Zone)
Writing code that scales.

❌ The Bad Way (Looping)
# NEVER DO THIS
for i in range(len(df)):
    df.loc[i, 'Sum'] = df.loc[i, 'A'] + df.loc[i, 'B']

✅ The Good Way (Vectorization)
# 100x Faster
df['Sum'] = df['A'] + df['B']

<div align="center">

[Pratham Ingole] Built with ❤️ and Python

</div>