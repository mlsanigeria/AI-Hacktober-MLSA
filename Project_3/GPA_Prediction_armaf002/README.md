# GPA Prediction Project - Data Preprocessing Readme

## Introduction

This readme provides an overview of the data preprocessing steps undertaken in the GPA prediction project. Data preprocessing is a crucial part of any data science project, as it ensures that the data is clean, structured, and ready for analysis and modeling.

## Data Loading

The data for this project is sourced from an Excel file named 'year1_gpa.xlsx'. The following Python libraries were used for data loading and initial exploration:

- `numpy`
- `pandas`
- `matplotlib` for data visualization
- `seaborn` for data visualization

## Data Preprocessing

### Column Name Standardization

To ensure consistency and ease of analysis, the column names were standardized by converting them to lowercase and replacing spaces with underscores. A dictionary was created to map the original column names to their standardized forms.

### Handling Missing Values

Missing values are a common issue in real-world datasets. Several strategies were applied to handle missing values in the dataset:

1. **Columns with All NaN Values:** Columns with no meaningful data (e.g., 'Name' and 'Last_modified_time') were dropped.

2. **Fill Missing Values Based on Gender:** Missing values in columns such as 'Use_of_extra_materials' and 'Monthly_allowance' were filled based on the gender of the students. The mean and mode values for these columns were calculated for each gender, and missing values were imputed accordingly.

3. **Handling Remaining Missing Values:** Any remaining missing values in the 'CGPA' column were handled by filling them with the mean of the column. This ensures that the 'CGPA' column contains numeric data.

4. **Grading System Mapping:** The 'Grading_system' column values were mapped to a common scale to ensure consistency and facilitate analysis. Numeric data types were enforced if necessary. Specifically, the 'A' value in the 'Grading_system' column was replaced with a numeric value to prevent it from being dropped.

### Data Type Conversion

The 'CGPA' column, which represents the Cumulative Grade Point Average, was processed to remove non-numeric entries, including 'no idea', extra spaces, and 'o'. The column was then converted to a numeric data type.

### Feature Engineering

Additional features related to 'Monthly_allowance' were created, including 'Monthly_allowance_avg', 'Monthly_allowance_min', and 'Monthly_allowance_max'. These features represent the average, minimum, and maximum values of the monthly allowance, respectively.

## Conclusion

Data preprocessing is a critical step in any data science project. It ensures that the data is clean, consistent, and ready for further analysis, feature engineering, and model building. The preprocessed dataset can now be used for exploratory data analysis (EDA) and subsequent modeling to predict GPA for first-year students.
