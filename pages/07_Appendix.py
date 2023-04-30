import pandas as pd
import plotly.express as px
import plotly.subplots as sp
import plotly.graph_objs as go
import numpy as np
import streamlit as st
from TechTrends import tech_demog


st.title("Appendix")
rel_bash = tech_demog[tech_demog['LanguageWorkedWith'] == 'Bash/Shell/PowerShell']
rel_bash = rel_bash.groupby('PlatformWorkedWith').count().sort_values('Respondent',ascending=False).reset_index()
rel_bash = rel_bash[['PlatformWorkedWith','Respondent']]
st.subheader("Answering the question: Why are Bash/Shell/PowerShell among the top languages used? Here's a diagram of each platform to which this language contributes.")
fig = px.bar(rel_bash,x='Respondent',y='PlatformWorkedWith',orientation='h')
fig.update_layout(dragmode=False, selectdirection=None,xaxis_title="Number of Respondents",yaxis_title="Platform using Bash/Shell/Powershell",title='Bash/Shell/PowerShell Langauge Users for each Platform',width=400,margin=dict(l=0, r=0, t=170, b=0))
st.plotly_chart(fig)

st.divider()

st.subheader("Python is the #1 option for data scientists, followed by SQL and R. The preceding charts demonstrate the significance of Bash/Shell/PowerShell and SQL is always required. We may conclude that a Data Scientist must be fluent in at least three languages. SQL, Python/R, Bash/Shell/PowerShell.")
data_scientist = tech_demog.query("DevType == 'Data scientist or machine learning specialist'")

left_col, right_col = st.columns(2)

with left_col:
    DS1 = data_scientist.groupby('LanguageWorkedWith')['Respondent'].count().reset_index().sort_values('Respondent',ascending=False)
    fig = px.bar(DS1,x='Respondent',y='LanguageWorkedWith',orientation='h')
    fig.update_layout(dragmode=False, selectdirection=None,xaxis_title="Number of Respondents",yaxis_title="Language Worked With",title='Data Scientists languages Worked With',width=400,margin=dict(l=0, r=0, t=170, b=0))
    st.plotly_chart(fig)

with right_col:
    DS2 = data_scientist.groupby('LanguageDesireNextYear')['Respondent'].count().reset_index().sort_values('Respondent',ascending=False)
    fig = px.bar(DS2,x='Respondent',y='LanguageDesireNextYear',orientation='h')
    fig.update_layout(dragmode=False, selectdirection=None,xaxis_title="Number of Respondents",yaxis_title="Language Desire Next Year",title='Data Scientists languages Desired Next Year',width=400,margin=dict(l=0, r=0, t=170, b=0))
    st.plotly_chart(fig)

st.divider()

# Add your demographic data visualizations and analysis here
st.write('<t1 style="font-weight:bold"> Average Age, Number of Respondents For each Eduaction Level </t1>',unsafe_allow_html=True)
EdLevel_age = tech_demog.groupby(['EdLevel']).agg({'Respondent':pd.Series.count,'Age':np.mean}).reset_index()
st.write(EdLevel_age)

country_age = tech_demog.groupby(['Country']).agg({'Respondent':pd.Series.count,'Age':np.mean}).reset_index().sort_values('Respondent',ascending=False).head(20)
# st.write(country_age)

# create a subplot with two axes
fig = sp.make_subplots(specs=[[{"secondary_y": True}]])

# add a bar trace to the subplot
fig.add_trace(go.Bar(x=country_age['Country'], y=country_age['Respondent'], name='N Respondents',marker=dict(color='lightblue')))

# add a line trace to the subplot's secondary axis
fig.add_trace(go.Scatter(x=country_age['Country'], y=country_age['Age'], name='Mean Age', mode='lines', yaxis='y2',marker=dict(color='blue')))

# update the layout to show the secondary axis
fig.update_layout(dragmode=False, selectdirection=None,
                    legend=dict(orientation='h', y=1.2),
                    yaxis=dict(title='N Respondnets'),yaxis2=dict(title='Mean Age'),height=350,width=400,title='Top 20 Countries By Respondents and Thier average Age')

st.plotly_chart(fig)

