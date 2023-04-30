import streamlit as st

st.title("Introduction")    
st.write("Analytical study was created to track recent technological progress and identify any potential shifts that may occur in the future. The rate of progress in this sector is rapid, so a significant shift may occur in only 1 year. That is why it is critical to inquire about respondents current technology worked on and preferred to study in the coming year. Each firm's goal is to detect the latest trend in order to stay up-to-date. This analysis is year by year requirement for every IT company.")
st.write("Graduates and newcomers focus on learning and mastering languages, databases, and web frameworks, while ignoring platforms. That is why it is crucial to ask respondents about the platforms they use so that they can assist beginners.")
st.write("It is necessary to establish each respondent's demographic background and how they are spread across nations, ages, gender, and education levels. It is also crucial to understand the man:woman ratio in this enormous industry, which is mirrored in the overall gender dominance in IT businesses.")
st.write("This report analyzes the current state and future trends in the technology landscape, focusing on:")
my_list2 = ["Languages",
            "Databases",
            "Platforms",
            "Web frameworks",
            "Demographic distribution (age-gender-location-education level)"
            ]
html_list2 = "<ul>" + "\n".join([f"<li>{item}</li>" for item in my_list2]) + "</ul>"
st.markdown(html_list2, unsafe_allow_html=True)
