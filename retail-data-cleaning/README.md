# 🧹 Retail Transaction Data Cleaning with Pandas & NumPy

This was my **first real-world data cleaning project** using **Python**, **Pandas**, and **NumPy**, where I cleaned and transformed a messy dataset containing over 9,500 retail transactions.

## 🗃️ Dataset Overview

The original dataset included:

- Inconsistent or unclear **item names** (e.g., `Juice`, `Juice/Cake`)
- **Duplicate prices** assigned to different items
- **Missing or blank values** in:
  - `Transaction Date`
  - `Quantity`
  - `Total Spent`
  - `Price Per Unit`
  - `Items`
- Rows with **incomplete data** (e.g., both quantity and total spent missing)
- Values with **incorrect data types** or **whitespace instead of nulls**

---

## 🧪 Objectives

- Identify and handle missing values logically.
- Correct inconsistent formatting and invalid entries.
- Infer missing values when possible using relationships (like `Total Spent = Quantity × Price`).
- Drop rows that could not be salvaged.
- Preserve the dataset’s analytical value.

---

## 🧰 Tools Used

- [x] Python 3
- [x] Pandas
- [x] NumPy
- [x] Jupyter Notebook

---

## 🧼 Cleaning Process Summary

- Converted `Transaction Date` to valid datetime format using Pandas.
- Coerced non-numeric values to NaN using `errors='coerce'` for numeric fields.
- Used `Item` and known price patterns to infer missing values where possible.
- Removed rows where both `Quantity` and `Total Spent` were missing (non-actionable).
- Removed rows where both `Items` and `Price Per Unit` was missing (non-actionable).
- Created a `Price ➝ Item` mapping (e.g., `$3` → `Juice/Cake`) to handle overlapping prices.
- Exported a fully cleaned dataset to CSV for future analysis.

---

## ✅ Final Output

- Total records after cleaning: **~9,500**
- No critical null values in essential fields.
- Dataset ready for analysis, visualization, or machine learning.

---

## 📁 Files in This Repository

| File Name                 | Description                               |
| ------------------------- | ----------------------------------------- |
| `cleaned_data.csv`        | Final cleaned version of the dataset      |
| `data_cleaning_script.py` | Full Python script used to clean the data |
| `README.md`               | Project overview (this file)              |
| `original_data.csv`       | Raw dataset before cleaning               |

---

This project was my **first hands-on experience** with real-world dirty data. It helped me build not only technical skills but also **confidence in solving real problems** using logic and tools — step by step.

---
