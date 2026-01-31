<div align="center">

🐼 The Pandas Master Reference Guide

The "Excel for Python on Steroids" Handbook

<p align="center">
<b>A comprehensive digital textbook for Data Manipulation.</b>




<i>Written by a student for students, refined for production.</i>
</p>

</div>

📚 Table of Contents

Chapter

Description

0. The Pandas Mindset

Understanding Vectorization & Alignment.

1. Series Deep Dive

Attributes, Methods, and Vectorization.

2. DataFrame Deep Dive

Structure, Attributes, and Manipulation.

3. I/O Operations

Reading CSV, Excel, SQL, and JSON.

4. Selection Strategy

Mastering loc vs iloc & Boolean Masks.

5. Data Hygiene

Handling NaN, Duplicates, and Dirty Data.

6. Transformation

.apply(), .map(), and Vectorized Strings.

7. Grouping Logic

The "Split-Apply-Combine" strategy.

8. Merging & Joins

SQL-style Joins, Concatenation, and Keys.

9. Time Series

Resampling, Date Ranges, and Frequency.

10. Expert Zone

Performance tuning and Best Practices.

🚀 Getting Started

import pandas as pd
import numpy as np

# Always check your version when debugging weird errors!
print(f"Pandas Version: {pd.__version__}")


🧠 0. The Pandas Mindset

Before writing code, understand Vectorization.

In standard Python, if you want to add 5 to a list of numbers, you write a loop. In Pandas, you apply the operation to the entire column at once. Pandas pushes the loop into C-level code, making it instant.

The Golden Rule: If you are writing a for loop to manipulate data, you are likely doing it wrong.

🧬 1. The Series (1D) Deep Dive

A Series is a one-dimensional labeled array. It is the building block of the DataFrame.

🎓 Student Note: A Series cannot contain set or frozenSet objects because they are unordered. It must be indexable.

1.1 Creation & Anatomy

# From a List (Default Index 0, 1, 2...)
s = pd.Series([10, 20, 30, 40])

# From a Dictionary (Keys become Index)
s_labeled = pd.Series({'a': 10, 'b': 20, 'c': 30})


1.2 Essential Attributes (Properties)

These are not functions, so they don't use ().

Attribute

Description

Example

.values

Returns the data as a raw NumPy array.

s.values → [10, 20, 30]

.index

Returns the index labels.

s.index → RangeIndex(start=0, stop=4)

.dtype

The data type of the elements.

s.dtype → int64

.shape

Dimensions of the data (Rows,).

s.shape → (4,)

.size

Total number of elements.

s.size → 4

.is_unique

Boolean check if all values are unique.

s.is_unique → True

1.3 Essential Methods (Functions)

These perform actions and require ().

s = pd.Series([10, 20, 20, 30, 50])

# --- Inspection ---
s.head(3)        # First 3 rows
s.tail(3)        # Last 3 rows
s.unique()       # Returns array of unique values: [10, 20, 30, 50]
s.nunique()      # Count of unique values: 4
s.value_counts() # Frequency table: 20 appears twice, others once.

# --- Math Statistics ---
s.sum()          # 130
s.mean()         # 26.0
s.std()          # Standard Deviation
s.max()          # 50
s.idxmax()       # Index of the max value (Where is 50? Index 4)


1.4 Vectorized Operations

Operations apply to every item at once.

s = pd.Series([10, 20, 30])

# Scalar Math (Broadcasting)
print(s + 5)     
# Output: [15, 25, 35]

# Vector Math (Series + Series)
# Aligns based on INDEX, not position!
s2 = pd.Series([1, 2, 3])
print(s + s2)    
# Output: [11, 22, 33]


🏗️ 2. The DataFrame (2D) Deep Dive

A DataFrame is a tabular structure (Rows & Columns). It is essentially a dictionary of Series objects.

2.1 Anatomy & Attributes

data = {
    'Name': ['Alice', 'Bob', 'Charlie'], 
    'Age': [25, 30, 35],
    'City': ['NY', 'LA', 'SF']
}
df = pd.DataFrame(data)


Attribute

Description

Example

.shape

Returns (rows, cols).

df.shape → (3, 3)

.columns

The list of column names.

df.columns → Index(['Name', 'Age', 'City'])

.index

The row labels.

df.index → RangeIndex(0, 3)

.dtypes

Types of each column.

df.dtypes

.T

Transpose (Swap rows/cols).

df.T

2.2 Structural Methods

1. Renaming Columns

# Use a dictionary to map Old -> New
df.rename(columns={'Name': 'Full Name', 'Age': 'Years'}, inplace=True)


2. Dropping Data

# Drop a Column (axis=1)
df.drop(columns=['City'], inplace=True)

# Drop a Row (axis=0) by Index
df.drop(index=0, inplace=True)


3. Sorting

# Sort by value (Low to High)
df.sort_values(by='Years', ascending=True)

# Sort by Index
df.sort_index()


4. Index Management

# Set a column as the Index (Row Label)
df.set_index('Full Name', inplace=True)

# Reset back to default 0, 1, 2...
df.reset_index(inplace=True)


💾 3. Input & Output (I/O)

Data persistence is usually step one. Pandas supports a vast array of formats.

Format

Read Command

Write Command

Note

CSV

pd.read_csv('file.csv')

df.to_csv('f.csv', index=False)

Most common format.

Excel

pd.read_excel('file.xlsx')

df.to_excel('f.xlsx')

Requires openpyxl.

JSON

pd.read_json('file.json')

df.to_json('f.json')

Good for web APIs.

SQL

pd.read_sql(query, conn)

df.to_sql('table', conn)

Requires SQLAlchemy.

✍️ Author's Tip: Always use index=False when saving to CSV. If you don't, Pandas will save the row numbers as a new column, creating a mess when you reload the data later.

🎯 4. Selection & Filtering

This is where beginners struggle most. Understanding Label vs Position is critical.

🆚 The loc vs iloc Cheat Sheet

Method

Type

Syntax

Description

Example

.loc

Label

[row_name, col_name]

"Human" selection. Inclusive of endpoints.

df.loc[5, 'City']

.iloc

Index

[row_pos, col_pos]

"Computer" selection. Exclusive of end.

df.iloc[0, 2]

⚡ Boolean Filtering (The "Mask")

This is the equivalent of SQL's WHERE clause.

# Combined One-Liner (Standard Practice)
# Note: Parentheses () are MANDATORY for multiple conditions!
target = df[(df['Age'] > 18) & (df['City'] == 'New York')]

# The .isin() method (Cleaner than multiple ORs)
cities = df[df['City'].isin(['London', 'Paris', 'Tokyo'])]


🧹 5. Data Hygiene

The 80/20 rule: 80% of Data Science is cleaning.

🚫 Handling Missing Data (NaN)

NaN stands for "Not a Number". It propagates like a virus (1 + NaN = NaN), so you must handle it.

df.isnull().sum()          # Count missing values per column

# Option A: Destruction
df.dropna()                # Drop rows with ANY nulls

# Option B: Imputation (Filling)
df.fillna(0)               # Fill with specific value
df['Age'].fillna(df['Age'].mean(), inplace=True) # Fill with average


♻️ Handling Duplicates

df.duplicated().sum()      # Check for duplicates
df.drop_duplicates(keep='first') # Remove duplicates, keep first instance


🛠 6. Transformation

The .apply() Method

Used to apply a custom Python function to every row or column.
Warning: This is slower than native vectorization, use only when necessary.

def to_fahrenheit(x):
    return (x * 1.8) + 32

# Apply to a column
df['Temp_F'] = df['Temp_C'].apply(to_fahrenheit)


String Manipulation (.str)

Pandas has a dedicated accessor for string operations that handles NaNs automatically.

df['Name'] = df['Name'].str.upper()               # Uppercase
df['Name'] = df['Name'].str.strip()               # Remove whitespace
df['Tech_Job'] = df['Job'].str.contains('Data')   # Boolean Search -> True/False


📊 7. Aggregation & Grouping

This utilizes the Split-Apply-Combine strategy.

Split data into groups based on criteria.

Apply a function to each group independently.

Combine the results into a new data structure.

Syntax: df.groupby('Categorical')['Numerical'].func()

# "For every Department, calculate the Mean Salary"
df.groupby('Department')['Salary'].mean()

# Multiple Stats at once
df.groupby('Department')['Salary'].agg(['mean', 'sum', 'max', 'count'])


🔗 8. Merging & Joining

Concatenation (Stacking)

Gluing dataframes together (usually vertically).

# Stack df1 on top of df2
combined = pd.concat([df1, df2], axis=0)


Merging (SQL Joins)

Connecting data side-by-side based on a shared "Key".

# Types of Joins (how=):
# 'inner': Only keep rows that match in BOTH tables.
# 'left': Keep all rows from LEFT table, match Right where possible (fill NaN if not).
# 'outer': Keep ALL rows from both tables.

merged = pd.merge(df_users, df_orders, on='user_id', how='left')


📅 9. Time Series

Pandas was originally built for financial time series.

# 1. Convert to DateTime (CRITICAL STEP)
# Pandas is smart enough to parse most date formats automatically
df['Date'] = pd.to_datetime(df['Date'])

# 2. Extract features using .dt accessor
df['Month'] = df['Date'].dt.month
df['Day_Name'] = df['Date'].dt.day_name()


⚡ 10. Performance (Expert Zone)


❌ The Bad Way (Looping)

Never loop through a DataFrame row-by-row.

# SLOW
for i in range(len(df)):
    df.loc[i, 'Sum'] = df.loc[i, 'A'] + df.loc[i, 'B']


✅ The Good Way (Vectorization)

Pandas operations are optimized in C. They operate on the entire array at once.

# FAST (100x speedup)
df['Sum'] = df['A'] + df['B']


<div align="center">

Happy Coding! 🐼





<sub>Created for the Modern Data Scientist</sub>

</div>