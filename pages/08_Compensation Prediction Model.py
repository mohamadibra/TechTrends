import pandas as pd
import streamlit as st
from streamlit.components.v1 import html
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import make_column_transformer
from TechTrends import df_clean


st.title("Compensation Model")
st.write("compensation refers to monetary payment given to an individual in exchange for their services.In the workplace, compensation is what is earned by employees. It includes salary or wages in addition to commission and any incentives or perks that come with the given employee's position.")
st.write("Based on the compensation data collected from respondents, a compensation prediction model dependent on 'age' and 'Education level' was developed.")

dt = df_clean[['EdLevel','ConvertedComp','Age']]

# create dummy variables for education level
ohe = OneHotEncoder(sparse=False)
ct = make_column_transformer((ohe, ['EdLevel']), remainder='passthrough')
X = ct.fit_transform(dt.drop('ConvertedComp', axis=1))

# define the target variable and fit a linear regression model
y = dt['ConvertedComp']
model = LinearRegression().fit(X, y)

# define the education level options for the dropdown list
ed_level_options = dt['EdLevel'].unique()

# get user inputs
ed_level = st.selectbox('Education level:', ed_level_options)
age = st.slider('Age:', 16, 65, 30)

# transform the user inputs and predict the compensation
new_data = pd.DataFrame({'EdLevel': [ed_level], 'Age': [age]})
new_X = ct.transform(new_data)
predicted_compensation = model.predict(new_X)

# display the predicted compensation to the user
st.title('Your predicted compensation')
st.write('Education level:', ed_level)
st.write('Age: ', f'<span style="color:lightgreen">{age}</span>', unsafe_allow_html=True)
# st.write('Predicted compensation: $', predicted_compensation[0])
st.write('Predicted compensation: ', f'<span style="color:lightgreen">$ {int(predicted_compensation[0])}</span>', unsafe_allow_html=True)