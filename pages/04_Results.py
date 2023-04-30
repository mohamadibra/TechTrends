import pandas as pd
import plotly.express as px
import plotly.subplots as sp
import plotly.graph_objs as go
import matplotlib as mpl
import streamlit as st
from TechTrends import tech_demog


st.title("Results")
st.subheader("Current Technology Used / Future Technology Trend:")
st.write("Programming Language Trends, Database Trends, Platform Trends, and Web Frameworks Trends are shown below, with each category displaying current year and desire to learn next year, as well as all findings and implications.")

st.header("Programming Languages")

top_ten_lg_ww = tech_demog.groupby('LanguageWorkedWith')['Respondent'].count().reset_index().sort_values('Respondent',ascending=True).tail(5)
top_ten_lg_d = tech_demog.groupby('LanguageDesireNextYear')['Respondent'].count().reset_index().sort_values('Respondent',ascending=True).tail(5)

fig = sp.make_subplots(rows=1,cols=2,horizontal_spacing=0.4,column_widths=[0.5, 0.5])

fig.add_trace(go.Bar(y=top_ten_lg_ww['LanguageWorkedWith'],x=top_ten_lg_ww['Respondent'],name='Worked With',orientation='h',marker=dict(
        color='lightgreen',
        reversescale=True  # reverses the order of the bars
    )),row=1,col=1)
fig.update_xaxes(title_text='LanguageWorkedWith',row=1,col=1)
fig.update_yaxes(title_text='N Respondents',row=1,col=1)

fig.add_trace(go.Bar(y=top_ten_lg_d['LanguageDesireNextYear'],x=top_ten_lg_d['Respondent'],name='Desired Next Year',orientation='h',marker=dict(
        color='darkgreen',
        reversescale=True  # reverses the order of the bars
    )),row=1,col=2)
fig.update_xaxes(title_text='LanguageDesireNextYear',row=1,col=2)
fig.update_yaxes(title_text='N Respondents',row=1,col=2)

fig.update_layout(height=400, width=1200, dragmode=False, selectdirection=None, title='Top 5 Programming Languages worked with and Desired Next Year By Respondents',showlegend=True,
    legend=dict(
        x=0.5,
        y=1.05,
        orientation="h",
        yanchor="bottom",
        xanchor="center",
    )
)

st.plotly_chart(fig, use_container_width=True)

# create two columns
left_col, right_col = st.columns(2)

# add content to left column
with left_col:
    st.header("Findings")
    # <li class='no_bullet'>&nbsp;</li>
    text = "<ul><li>JavaScript remains on top this and next year.</li><li>JavaScript, HTML/CSS/SQL is in the top 3 worked with.</li><li>Bash/Shell/PowerShell is in the Top 5 and higher than Python.</li><li>Python is trending up with 5239 respondents willing to learn next year.</li><li>Top 5 ranges</li><ul><li>current year: 8687 - 4542</li><li>Next year: 6630 – 4088</li></ul></ul>"
    st.markdown(text,unsafe_allow_html=True)

# add separator
# st.sidebar.markdown("---")

# add content to right column
with right_col:
    st.header("Implications")
    text = "<ul><li>Gives more popularity for JavaScript web frameworks.</li><li>Web development is highly dominant among developers.</li><li>Automating tasks is essential for developers.</li><li>There might be a shift in the dominance of machine learning and AI in the coming years.</li><li>Reflects the enormous ongoing need for JavaScript, Python, HTML/CSS, and SQL.</li></ul>"
    st.markdown(text,unsafe_allow_html=True)

st.divider()  # 👈 Draws a horizontal rule

st.header("DataBases")

top_ten_db_ww = tech_demog.groupby('DatabaseWorkedWith')['Respondent'].count().reset_index().sort_values('Respondent',ascending=True).tail(5)
top_ten_db_d = tech_demog.groupby('DatabaseDesireNextYear')['Respondent'].count().reset_index().sort_values('Respondent',ascending=True).tail(5)

fig = sp.make_subplots(rows=1,cols=2,horizontal_spacing=0.4,column_widths=[0.5, 0.5])

fig.add_trace(go.Bar(y=top_ten_db_ww['DatabaseWorkedWith'],x=top_ten_db_ww['Respondent'],name='Worked With',orientation='h',marker=dict(
        color='lightblue',
        reversescale=True  # reverses the order of the bars
    )),row=1,col=1)
fig.update_xaxes(title_text='DatabaseWorkedWith',row=1,col=1)
fig.update_yaxes(title_text='N Respondents',row=1,col=1)

fig.add_trace(go.Bar(y=top_ten_db_d['DatabaseDesireNextYear'],x=top_ten_db_d['Respondent'],name='Desired Next Year',orientation='h',marker=dict(
        color='darkblue',
        reversescale=True  # reverses the order of the bars
    )),row=1,col=2)
fig.update_xaxes(title_text='DatabaseDesireNextYear',row=1,col=2)
fig.update_yaxes(title_text='N Respondents',row=1,col=2)

fig.update_layout(height=400,width=1200,dragmode=False, selectdirection=None, title='Top 5 databases worked with and Desired Next Year By Respondents',showlegend=True,
    legend=dict(
        x=0.5,
        y=1.05,
        orientation="h",
        yanchor="bottom",
        xanchor="center",
    )
)
st.plotly_chart(fig, use_container_width=True)

# create two columns
left_col, right_col = st.columns(2)

# add content to left column
with left_col:
    st.header("Findings")
    text = "<ul><li>MySQL is the most popular database. 25% higher than the second and third place databases.</li><li>PostgreSQL popularity booming with 4328 respondents willing to learn next year.</li><li>Redis and elastic search databases are growing in popularity, with 3331 and 2856 users willing to learn next year, respectively.</li><li>Respondents willing to learn MongoDB is 3649 falling in the second place.</li></ul>"
    st.markdown(text,unsafe_allow_html=True)

# add separator
# st.sidebar.markdown("---")

# add content to right column
with right_col:
    st.header("Implications")
    text = "<ul><li>Relational database management system (RDBMS) is now the most used for operating databases.</li><li>A possible shift in database systems dominance from (RDBMS) to Object-relational databases (ORDBMS).</li><li>Suggests a rise is the popularity of NoSQL databases and new storage technologies to follow up with.</li><li>shows the relevance of adopting NoSQL for particular internet applications in the next years.</li></ul>"
    st.markdown(text,unsafe_allow_html=True)

st.divider()  # 👈 Draws a horizontal rule

st.header("Platforms")

top_ten_pm_ww = tech_demog.groupby('PlatformWorkedWith')['Respondent'].count().reset_index().sort_values('Respondent',ascending=True).tail(5)
top_ten_pm_d = tech_demog.groupby('PlatformDesireNextYear')['Respondent'].count().reset_index().sort_values('Respondent',ascending=True).tail(5)

fig = sp.make_subplots(rows=1,cols=2,horizontal_spacing=0.4,column_widths=[0.5, 0.5])

fig.add_trace(go.Bar(y=top_ten_pm_ww['PlatformWorkedWith'],x=top_ten_pm_ww['Respondent'],name='Worked With',orientation='h',marker=dict(
        color='lightcyan',
        reversescale=True  # reverses the order of the bars
    )),row=1,col=1)
fig.update_xaxes(title_text='PlatformWorkedWith',row=1,col=1)
fig.update_yaxes(title_text='N Respondents',row=1,col=1)

fig.add_trace(go.Bar(y=top_ten_pm_d['PlatformDesireNextYear'],x=top_ten_pm_d['Respondent'],name='Desired Next Year',orientation='h',marker=dict(
        color='darkcyan',
        reversescale=True  # reverses the order of the bars
    )),row=1,col=2)
fig.update_xaxes(title_text='PlatformDesireNextYear',row=1,col=2)
fig.update_yaxes(title_text='N Respondents',row=1,col=2)

fig.update_layout(dragmode=False, selectdirection=None,height=400,width=1200, title='Top 5 Platforms worked with and Desired Next Year By Respondents',showlegend=True,
    legend=dict(
        x=0.5,
        y=1.05,
        orientation="h",
        yanchor="bottom",
        xanchor="center",
    )
)

st.plotly_chart(fig, use_container_width=True)

# create two columns
left_col, right_col = st.columns(2)

# add content to left column
with left_col:
    st.header("Findings")
    text = "<ul><li>Linux on top, follows windows is on top with 5811, 5563 respectively.</li><li>Linux is the top platform desired to learn next year while docker userser are rapidly increasing.</li><li>Linux, Docker, Windows, and AWS continue to be the most wanted platforms for this year and next.</li</ul>"
    st.markdown(text,unsafe_allow_html=True)

# add separator
# st.sidebar.markdown("---")

# add content to right column
with right_col:
    st.header("Implications")
    text = "<ul><li>Linux and windows are currently the most used platforms by respondents.</li><li>Linux is still trending higher for next year with, Docker is expected to boom in the coming years.</li><li>Every IT professional should be able to grasp one or two of these platforms since they are in high demand today and in the future.</li></ul>"
    st.markdown(text,unsafe_allow_html=True)

st.divider()  # 👈 Draws a horizontal rule

st.header("Web Framework")

top_ten_wf_ww = tech_demog.groupby('WebFrameWorkedWith')['Respondent'].count().reset_index().sort_values('Respondent',ascending=True).tail(5)
top_ten_wf_d = tech_demog.groupby('WebFrameDesireNextYear')['Respondent'].count().reset_index().sort_values('Respondent',ascending=True).tail(5)

fig = sp.make_subplots(rows=1,cols=2,horizontal_spacing=0.4,column_widths=[0.5, 0.5])

fig.add_trace(go.Bar(y=top_ten_wf_ww['WebFrameWorkedWith'],x=top_ten_wf_ww['Respondent'],name='Worked With',orientation='h',marker=dict(
        color='lightpink',
        reversescale=True  # reverses the order of the bars
    )),row=1,col=1)
fig.update_xaxes(title_text='WebFrameWorkedWith',row=1,col=1)
fig.update_yaxes(title_text='N Respondents',row=1,col=1)

fig.add_trace(go.Bar(y=top_ten_wf_d['WebFrameDesireNextYear'],x=top_ten_wf_d['Respondent'],name='Desired Next Year',orientation='h',marker=dict(
        color='darkmagenta',
        reversescale=True  # reverses the order of the bars
    )),row=1,col=2)
fig.update_xaxes(title_text='WebFrameDesireNextYear',row=1,col=2)
fig.update_yaxes(title_text='N Respondents',row=1,col=2)

fig.update_layout(dragmode=False, selectdirection=None,height=400,width=1200, title='Top 5 Web Frameworks worked with and Desired Next Year By Respondents',showlegend=True,
    legend=dict(
        x=0.5,
        y=1.05,
        orientation="h",
        yanchor="bottom",
        xanchor="center",
    )
)

st.plotly_chart(fig, use_container_width=True)

# create two columns
left_col, right_col = st.columns(2)

# add content to left column
with left_col:
    st.header("Findings")
    text = "<ul><li>JQuery on top, then Angular.js, then React.js on top 4629, 3327, 3302 respectively.</li><li>React is on top of web frameworks desired next year with 4714 and 33% higher than Vue.js 3143 which on 2nd place.</li><li>JQuery, Angular, React, and ASP.NET are remain among the top five web frameworks this year and next year.</li</ul>"
    st.markdown(text,unsafe_allow_html=True)

# add separator
# st.sidebar.markdown("---")

# add content to right column
with right_col:
    st.header("Implications")
    text = "<ul><li>JavaScript related web frameworks is currently dominating the web frameworks.</li><li>Powered by JavaScript, the number of React users is projected to grow in the next years.</li><li class='no_bullet'>&nbsp;</li><li>Web frameworks powered by JavaScript and .NET is hugely required for every web developer.</li></ul>"
    st.markdown(text,unsafe_allow_html=True)

st.divider()  # 👈 Draws a horizontal rule

st.header("Demographics")



# st.subheader("Gender Distribution")
m_f_tech_demog = tech_demog.query("Gender == 'Man' or Gender == 'Woman'")
m_f_tech_demog['Gender'].value_counts()
# Count number of men and women
counts = m_f_tech_demog['Gender'].value_counts()

# Calculate percentage of men and women
percentages = counts / counts.sum()

# Create pie chart
fig = px.pie(
    values=percentages,
    names=percentages.index,
    title='Gender Distribution'
)

fig.update_layout(dragmode=False, selectdirection=None,legend=dict(
    x=0,
    y=1,
    traceorder='normal',
    font=dict(
        family='sans-serif',
        size=12,
        color='white'
    ),
    # bgcolor='LightSteelBlue',
    # bordercolor='Black',
    # borderwidth=2),
    ),
    height=400
    )

st.plotly_chart(fig, use_container_width=True)

# add separator
# st.sidebar.markdown("---")

# st.subheader("Country Distribution")
# Group by country and count respondents
tech_demog_loc = tech_demog.groupby('Country')['Respondent'].count().reset_index().sort_values('Respondent',ascending=False)

# Create choropleth map
data = go.Choropleth(
    locations=tech_demog_loc['Country'],
    z=tech_demog_loc['Respondent'],
    locationmode='country names',
    colorscale='Blues',
    marker_line_color='#010101',
    marker_line_width=0.5,
)

layout = go.Layout(
    title='Country Distribution',
    geo=dict(
        showframe=False,
        showcoastlines=False,
        projection_type='natural earth',
        ),
    margin=dict(l=0, r=0, t=70, b=0),
)

fig = go.Figure(data=data, layout=layout)

# Display map
st.plotly_chart(fig)       

# group by Gender and EdLevel and count the number of respondents
df_count = m_f_tech_demog.groupby(['Gender', 'EdLevel'])['Respondent'].count().reset_index()
# create stacked bar chart
fig = px.bar(df_count, y='EdLevel', x='Respondent', color='Gender', barmode='group', orientation='h',
            title='Number of Respondents by Education Level and Gender')
fig.update_layout(dragmode=False, selectdirection=None,xaxis_title='Number of Respondents', yaxis_title='Education Level')

# Display the chart
st.plotly_chart(fig)

tech_demog_age = m_f_tech_demog.groupby('Age')['Respondent'].count().reset_index().sort_values('Age',ascending=False)
fig = go.Figure(go.Scatter(
x=tech_demog_age['Age'],
y=tech_demog_age['Respondent'],
mode='lines+markers',
marker=dict(size=4),
line=dict(width=1.5, color='royalblue'),
hovertemplate='Age: %{x}<br>Respondent: %{y}',
))

# Customize the layout
fig.update_layout(dragmode=False, selectdirection=None,
    title='Number of Respondents by Age',
    xaxis_title='Age',
    yaxis_title='Number of Respondents',
    height = 350,
    width=430
)
st.plotly_chart(fig)

st.subheader("Findings – Implications")
st.write(" This shows the country's technical development, as IT Specialists shape the technology status of their country. Highest age is 99, lowest age is 16, the age with the most respondents (4942) is 28. 31 is the average age of all respondents.Most respondents have a bachelor's degree, followed by a master's degree, and then college/university studies without a degree with 37600, 17012, 8983 respondents respectively. It is worth noting that over half of the respondents hold a bachelor's degree.")
text = "<ul><li>Men IT Specialists is 93.5% where Women is 6.5%, about 14:1 ratio.</li><li>USA, India, UK, Germany and Canada are the Top 5 countries with IT specialists of range 20818 – 2775. This shows the country's technical development, as IT Specialists shape the technology status of their country.</li><li>Highest age is 99, lowest age is 16, the age with the most respondents (4942) is 28. 31 is the average age of all respondents.</li><li>Most respondents have a bachelor's degree, followed by a master's degree, and then college/university studies without a degree with 5342, 2484, 1280 respondents respectively. It is worth noting that over half of the respondents hold a bachelor's degree.</li></ul>"
st.markdown(text,unsafe_allow_html=True)