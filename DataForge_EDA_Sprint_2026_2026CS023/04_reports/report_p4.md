 
# Project Report – Phase 4 (Power Query Pipeline)

## Overview

The dataset was imported into Power BI Desktop and transformed using Power Query. Data types were verified, errors were checked, and new calculated columns were created to prepare the dataset for analysis.

## Transformations Performed

- Imported the raw CSV file.
- Promoted the first row as headers.
- Verified and corrected data types.
- Removed obvious errors where necessary.
- Created a conditional column (Order Size / Profit Status).
- Extracted Year and Month from the Order Date column.
- Loaded the transformed data into Power BI.

## Report Questions

### 1. How is Power Query different from manual Excel cleaning?

Power Query records every transformation as a sequence of reusable steps. Unlike manual Excel cleaning, these steps can be automatically applied whenever new data is imported, improving consistency and reducing manual effort.

### 2. Which transformation would save time when new CSV data arrives?

Automatically promoting headers, applying the correct data types, creating calculated columns (such as Order Size), and extracting Year and Month are the most time-saving transformations because they are repeated automatically whenever the dataset is refreshed.ec