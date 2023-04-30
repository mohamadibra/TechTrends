import streamlit as st

st.set_page_config(layout="wide")

st.title("Conclusion")
st.subheader("IT Specialist Needs to Master at least Two of each:")
text = "<ul><li>Language: JavaScript, HTML/CSS, Python, SQL.</li><li>Databases: MySQL, PostgreSQL, MongoDB, Redis.</li><li>Platforms: Linux, Docker, AWS, Windows.</li><li>Web Frameworks(if web developer): React.js, Angular.js, Vue.js, ASP.NET.</li></ul>"
st.markdown(text,unsafe_allow_html=True)
st.subheader('Extracted Knowledge:')
text2 = "<ul><li>Python, Docker, PostgreSQL, MongoDB, and React is growing fast.</li><li>Everything Powered by javascript is currently booming and still growing.</li><li>Emerging technologies spot the lights on cloud computing, machine learning, and AI.</li><li>Data Science is expected to boom in future.</li><li>Cloud computing technologies are widely employed.</li></ul>"
st.markdown(text2,unsafe_allow_html=True)