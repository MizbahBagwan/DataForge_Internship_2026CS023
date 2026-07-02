# Automated EDA Dashboard

## How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

## Features

* Upload any CSV
* Dataset shape
* Column names
* Data types
* Missing-value table
* Numeric summary
* Histogram
* Top 10 Sales
* Bottom 10 Sales
* Automatic insight generation

## Limitations

* Assumes the uploaded dataset is well-structured.
* Advanced statistical analysis is not included.
* Some features (such as Top/Bottom Sales) require a `Sales` column.
 
