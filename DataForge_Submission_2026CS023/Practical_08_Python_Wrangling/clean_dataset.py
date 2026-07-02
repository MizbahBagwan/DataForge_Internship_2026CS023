import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("01_data/raw/dataset_raw.csv")

print("Original Shape:", df.shape)

# -----------------------------
# Remove duplicate rows
# -----------------------------
duplicates = df.duplicated().sum()
print("Duplicate Rows:", duplicates)

df = df.drop_duplicates()

# -----------------------------
# Convert date columns
# -----------------------------
date_columns = ["Order Date", "Ship Date"]

for col in date_columns:
    if col in df.columns:
        df[col] = pd.to_datetime(df[col], errors="coerce")

# -----------------------------
# Extract Year and Month
# -----------------------------
if "Order Date" in df.columns:
    df["Order Year"] = df["Order Date"].dt.year
    df["Order Month"] = df["Order Date"].dt.month_name()

# -----------------------------
# Fill missing categorical values
# -----------------------------
categorical_cols = df.select_dtypes(include="object").columns

for col in categorical_cols:
    df[col] = df[col].fillna("Unknown")

# -----------------------------
# Fill missing numeric values
# -----------------------------
numeric_cols = df.select_dtypes(include=np.number).columns

for col in numeric_cols:
    df[col] = df[col].fillna(df[col].median())

# -----------------------------
# Feature Engineering
# -----------------------------

# Profit Margin
if "Sales" in df.columns and "Profit" in df.columns:
    df["Profit Margin"] = (df["Profit"] / df["Sales"]) * 100

# High Value Order
if "Sales" in df.columns:
    df["High Value Order"] = np.where(
        df["Sales"] >= 1000,
        "Yes",
        "No"
    )

# -----------------------------
# Export cleaned dataset
# -----------------------------
output_path = "01_data/processed/dataforge_cleaned.csv"

df.to_csv(output_path, index=False)

print("Cleaned dataset saved successfully!")
print("Final Shape:", df.shape)