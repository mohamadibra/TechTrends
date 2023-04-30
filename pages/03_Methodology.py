import streamlit as st

st.title("Methodology")
st.write("It is required for the study to ask IT experts about their everyday technologies utilized and wanted in the future, as well as to have demographic information. For this purpose, the 2019 Stackovreflow survey was the best option.")
my_list3 = ["Data was used from a stackoverflow developer survey done in 2019",
            "It was a 20 minutes survey",
            "filled out by 90000 developers",
            "The Analysis was done on 80% of the total 90000 results"]
html_list3=""
for i in my_list3:
    html_list3 += "- " + i + "\n"
st.markdown(html_list3)
st.write("The analysis was divided into three major sections:")
my_list4 = ["Current Technology Usage",
            "Future Technology Trend",
            "Demographics"]
html_list4=""
for i in my_list4:
    html_list4 += "- " + i + "\n"
st.markdown(html_list4)

st.write("Each technology section was grouped by `Current Year` and `Next Year`:")
my_list5 = ["Language used this year - Language desire to learn next year",
            "Database used this year - Database desire to learn next year",
            "Plarform used this year - Platform desire to learn next year"
            "Web Framework used this year - Web Framework desire to learn next year"]
html_list5=""
for i in my_list5:
    html_list5 += "- " + i + "\n"
st.markdown(html_list5)
st.write("Demographics analysis focused on `age`, `gender`, `Education Level`, and `County`")