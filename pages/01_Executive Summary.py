import streamlit as st

st.write("<style>ul { margin-left: 20px; } li.no_bullet { list-style-type: none;}</style>", unsafe_allow_html=True)

st.title("Executive Summary")
st.write("To spot trends and forecast the near future in the IT sector, both businesses and individuals must answer the most crucial questions:")
# Define a list of items
my_list = ["Top 5 Languages used and desired to learn.",
            "Top 5 Databases used and desired to learn.",
            "Top 5 Web Frameworks used and desired to learn.",
            "Platforms used and desired to learn.",
            "The age, gender location, and education level."
            ]

# Write the list in HTML format
html_list = "<ul>" + "\n".join([f"<li>{item}</li>" for item in my_list]) + "</ul>"
st.markdown(html_list, unsafe_allow_html=True)

st.write("A stackoverflow survey served well the analysis goals where hundreds of respondents answered these question.")
st.write("A summary of what we have obtained from the analysis:")
my_list1 = ["Languages for web developments purposes showed huge dominance where JavaScript, HTML/CSS, SQL where in the Top 5 languages worked with and desired to learn in future.",
            "Databases analysis indicated a possible shift in the future. MySQL, PostgreSQL, and Microsoft SQL Server were in the top 3 worked with. PostgreSQL, MongoDB, and Redis were in the top 3 to learn next year.",
            "Platforms used and desired to learn bring Linux on top, where businesses constantly prioritize security and dependability. Docker, Windows, and AWS are the top three desired skills.",
            "Web Framework analysis revealed that JavaScript Web Frameworks dominated, with JQuery, Angular, and React being the top three worked with. React emerged as the most desired Web Framework next year ranking 33% higher than the second most desired one, Vue.js.",
            "Demographic analysis revealed that men outnumbered women by 93.5% to 6.5%, with the majority of respondents having a BA degree level 50%, 25% MA, and 25% for the remaining education levels.",
            "Most of the respondents where distributed in USA, India, UK, Germany and Canada."
            ]
# Write the list in HTML format
html_list1 = "<ul>" + "\n".join([f"<li>{item}</li>" for item in my_list1]) + "</ul>"
st.markdown(html_list1, unsafe_allow_html=True)
