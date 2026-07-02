# Project Report – Phase 8 (Data Cleaning & Feature Engineering)

## Overview

The dataset was cleaned using a reusable Python script and a Jupyter Notebook. Duplicate records were checked, missing values were handled, date columns were converted to datetime format, and new features were created to improve analytical capabilities.

## Cleaning Steps

* Loaded the raw dataset.
* Checked for duplicate records and removed them if present.
* Converted Order Date and Ship Date to datetime format.
* Extracted Order Year and Order Month.
* Filled missing categorical values with **"Unknown"**.
* Filled missing numeric values using the median of each numeric column.
* Exported the cleaned dataset to the processed data folder.

## Feature Engineering

Two additional features were created:

1. **Profit Margin** – Percentage of profit relative to sales.
2. **High Value Order** – Identifies orders with sales of at least 1000 as "Yes" and others as "No".

## Report Questions

### 1. What cleaning decision could affect business conclusions?

Filling missing numeric values with the median can influence summary statistics and trends. While it avoids losing records, it may slightly alter averages and distributions, so the chosen method should be documented.

### 2. Which engineered feature is most useful and why?

The **Profit Margin** feature is the most useful because it measures profitability relative to sales. It enables comparison across products, categories, and regions regardless of sales volume, helping identify areas that generate the best returns.
  
