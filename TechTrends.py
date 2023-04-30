import pandas as pd
import streamlit as st

st.set_page_config(layout="wide",page_title='Tech Trends')

demog = pd.read_csv('m5_survey_data_demographics.csv')
tech = pd.read_csv('m5_survey_data_technologies_normalised.csv')

tech_demog = pd.merge(tech,demog,on='Respondent',how='inner')

df = tech_demog[['Respondent','Age','EdLevel','ConvertedComp','Country']]

df['Age'].fillna(df['Age'].median(), inplace=True)

df['EdLevel'].fillna(df['EdLevel'].mode()[0], inplace=True)

df.dropna(subset='ConvertedComp',inplace=True)

Q1 = df['ConvertedComp'].quantile(0.25)
Q3 = df['ConvertedComp'].quantile(0.75)
IQR = Q3 = Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = df[(df['ConvertedComp'] < lower_bound) | (df['ConvertedComp'] > upper_bound)]

df_clean = df[~((df['ConvertedComp'] < lower_bound) | (df['ConvertedComp'] > upper_bound))]

def main():
    st.title("Tech Trends")
    st.subheader("Tech Trends: Analyzing Top Programming Languages, Databases, Platforms, and Web Frameworks Used and Desired for Learning")


if __name__ == "__main__":
    main()