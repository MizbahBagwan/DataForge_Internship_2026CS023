 
# Project Report – Phase 5 (Power BI Model & DAX)

## Overview

A Power BI data model was created with DAX measures to calculate key business metrics. A date table was added to support time-based analysis, and a calculated column was created to categorize order sizes.

## DAX Measures

- Total Sales
- Total Profit
- Order Count
- Average Discount (if available)
- Profit Margin

## Calculated Column

Order Size was created to classify sales into High, Medium, and Low categories, making it easier to filter and compare orders.

## Date Table

A Date Table was created using the CALENDAR function and includes Year, Month, and Month Number fields.

## Report Questions

### 1. What is the difference between a column and a measure?

A calculated column computes a value for every row in the dataset and stores the result in the model. A measure is calculated only when needed in a report or visual and changes dynamically based on filters and user selections.

### 2. Which KPI would you put on top of the dashboard and why?

Total Sales is the most important KPI because it provides an immediate view of overall business performance. Depending on the audience, Total Profit and Profit Margin are also valuable because they indicate how efficiently the business is generating profit from sales.