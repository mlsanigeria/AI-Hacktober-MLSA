import streamlit as st
import pandas as pd
import numpy
import sklearn
import joblib

st.title("Year One GPA Prediction Application")
st.write("This is an open source project created by participants of the HacktoberFest Open Source Contribution in conjuction with         the Microsoft Learn Student Ambassadors (MLSA) in Nigeria. The aim of this project is to create a web application that predicts the GPA of first year students")

st.write("Input the following details to predict your GPA")
jamb_score = st.number_input("What was your score in JAMB", min_value=0, max_value=400, step=1)
age_in_year_one = st.number_input("What was your age in Year One", min_value=14, max_value=30, step=1)
st.write("Input your grades in WAEC for the five relevant subjects including English and Maths")
english_score = st.selectbox("English", ["A","B","C","D","E","F"])
math_score = st.selectbox("Mathematics", ["A","B","C","D","E","F"])
subject_3 = st.selectbox("Third Subject", ["A","B","C","D","E","F"])
subject_4 = st.selectbox("Fourth Subject", ["A","B","C","D","E","F"])
subject_5 = st.selectbox("Fifth Subject", ["A","B","C","D","E","F"])
extra_tutorials = st.selectbox("Did you attend extra tutorials?", ["Yes","No"])
extra_curriculum = st.number_input("Rate your participation in extra curricular activities on a scale of 1-10", min_value=1, max_value=10, step=1)
class_attendance = st.number_input("Rate your class attendance on a scale of 1-10", min_value=1, max_value=10, step=1)
class_participation = st.number_input("Rate your class participation on a scale of 1-10", min_value=1, max_value=10, step=1)
extra_materials = st.number_input("Rate your use of extra materials (e.g. Youtube, Textbooks etc.) in year one on a scale of 1-10", min_value=1, max_value=10, step=1)
day_per_week_reading = st.number_input("How many days do you read in a week?", min_value=0, max_value=7, step=1)
taught_peers = st.selectbox("Did you teach your peers?", ["No: Didn't Interact with my peers","No : Studied Alone", "Yes : I ran a tutorial service", "Yes : A few times"])
hours_per_day_reading = st.number_input("How many hours of personal study per day?", min_value=0, max_value=24, step=1)
teaching_style_rating = st.number_input("Rate the teaching style/method of your lecturers on a scale of 1-10", min_value=1, max_value=10, step=1)
institution_type = st.selectbox("What was your institution type?", ["Public - Federal", "Public - State", "Private"])
grading_style = st.selectbox("What grading system does your school use?", [5,4,7,10])
monthly_allowance = st.selectbox("What was your monthly allowance in Year One", ["0-5k",'6-10k','11-20k','21-30k','31-50k','51-70k','71-100k','100k+'])
preferred_study_time = st.selectbox("What time of the day do you prefer to study?", ["Morning", "Late Night", "Evening", "Afternoon"])
# Encode the subjects
ordinal_encoding_map = {'A': 5, 'B': 4, 'C': 3, 'D': 2, 'E': 1, 'F': 0}
features_to_encode = ['english', 'maths', 'subject_3', 'subject_4', 'subject_5']

for feature in features_to_encode:
    if feature == 'english':
        english_score = ordinal_encoding_map[english_score]
    elif feature == 'maths':
        math_score = ordinal_encoding_map[math_score]
    elif feature == 'subject_3':
        subject_3 = ordinal_encoding_map[subject_3]
    elif feature == 'subject_4':
        subject_4 = ordinal_encoding_map[subject_4]
    elif feature == 'subject_5':
        subject_5 = ordinal_encoding_map[subject_5]

# Encode the institution type
if institution_type == 'Public - Federal':
    institution_type = 1
elif institution_type == 'Public - State':
    institution_type = 2
else:
    institution_type = 0

#Encode monthly allowance
if monthly_allowance == '0-5k':
    monthly_allowance = 5
elif monthly_allowance == '6-10k':
    monthly_allowance = 0
elif monthly_allowance == '11-20k':
    monthly_allowance = 2
elif monthly_allowance == '21-30k':
    monthly_allowance = 1
elif monthly_allowance == '31-50k':
    monthly_allowance = 3
elif monthly_allowance == '51-70k':
    monthly_allowance = 4
else:
    monthly_allowance = 6

if preferred_study_time == 'Morning':
    preferred_study_time = 3
elif preferred_study_time == 'Late Night':
    preferred_study_time = 2
elif preferred_study_time == 'Evening':
    preferred_study_time = 1
else:
    preferred_study_time = 0

if taught_peers == "No: Didn't Interact with my peers":
    taught_peers = 0
elif taught_peers == "No : Studied Alone":
    taught_peers = 1
elif taught_peers == "Yes : I ran a tutorial service":
    taught_peers = 2
else:
    taught_peers = 3

if extra_tutorials == 'Yes':
    extra_tutorials = 1
else:
    extra_tutorials = 0

average_subject_score = (english_score + math_score + subject_3 + subject_4 + subject_5)/5


# Create a dataframe
student_data = pd.DataFrame({
    'jamb_score': [jamb_score],
    'age_in_year_one': [age_in_year_one],
    'Did you attend extra tutorials?\xa0': [extra_tutorials],
    'extracurricular_participation': [extra_curriculum],
    'class_attendance_rating': [class_attendance],
    'class_participation_rating': [class_participation],
    'Rate\xa0your use of extra materials for study in Year One (Youtube, Other books, others).': [extra_materials],
    'days_per_week_reading': [day_per_week_reading],
    'hours_per_day_personal_study': [hours_per_day_reading],
    'taught_peers': [taught_peers],
    'What was your monthly allowance in Year One?': [monthly_allowance],
    'teaching_style_rating': [teaching_style_rating],
    'institution_type': [institution_type],
    'grading_style': [grading_style],
    'preferred_study_time': [preferred_study_time],
    'avg_subject_score': [average_subject_score],
})

X = student_data.drop(['grading_style'], axis=1)

scaler = joblib.load('scaler.joblib')
model = joblib.load('regression_model.joblib')

X_scaled = scaler.transform(X)

#Load JobLIb File
prediction = model.predict(X_scaled)
predicted_gpa = prediction[0] * student_data['grading_style'][0]

if st.button('Predict'):
    st.write('Your predicted GPA is: ', round(predicted_gpa,3))