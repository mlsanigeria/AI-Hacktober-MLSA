# GPA Prediction
This project analyzes factors contributing to first-year student performance and predicts the GPA of first year students based on factors such as: high school performance, Jamb Score, finances, class participation, extra curriular activities etc. 

### Python Libraries Used
The following python libaries were used for the different areas of the project. 
- Data Exploration & Preprocessing : `pandas` `numpy` `openpyxl`
- Data Visualization : `matplotlib` `seaborn`
- Machine Learning : `scikit-learn` `joblib`
- Deploymnet : `streamlit`

### Data Acquision & Preprocessing Techniques
The data was collected via a survey from Nigerian students in tertiary institutions. The link to the survey can be found [here](https://forms.office.com/pages/responsepage.aspx?id=oBzDhDusrk6tEVGdgCM-b3WhuDg-4D1CshxaPwVhg9lUQkhTSFFKVDJESFlPM0MwNUgxNUVVVkNVTC4u/). The following techniques were applied to preprocess the data:
- Removing missing values, irrelevant columns and rows
- Treating erroneous values 
- Converting data to the right data type
- Label encoding 

### Insights
By applying univariate and bi-variate analysis, the following are some of the insights were gathered from the data: 

- A greater proportion of first-year students are between 16 and 18, however a younger age does not imply better performance
- There is a moderate positive relationship between JAMB scores and the GPA of first year students
- Students who use extra materials tend to perform better than their peers. 
- Students who attend extra tutorials tend to perform better than those who don't 
- Students who have a higher monthly allowance tend to have a higher GPA than their counterparts.

### Notebook Structure
This depicts the workflow followed in the notebook.

```bash
├── Data Collection
├── Data Preprocessing
│   ├── renaming columns
│   ├── treating missing data
│   ├── converting columns to categorical/numerical data types
├── Data Exploration
├── Feature Engineering
│   ├── Label Encoding
│   ├── Scaling (Standard Scaling)
├── Modelling
│   ├── model training
│   ├── model evaluation
│   ├── saving the model
```
### Modelling
The optimal model is the `Random Forest Regressor` with a `RMSE` of 0.108 and a `MAE` of 0.08

### Deployment
The model was deployed as a web application using streamlit. To run locallay, use : `streamlit run streamlit_app.py`.
