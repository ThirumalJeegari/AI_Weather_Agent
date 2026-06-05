import streamlit as st
import requests

S_URL = st.secrets["backend_url"]

st.title("AI Weather Agent")

city = st.text_input("Enter City")
question = st.text_input("Ask Your Weather Question")
submit_button = st.button("Ask Agent")

if submit_button:
    if city == "" or question == "":
        st.error("Please enter city and question")
    else:
        res = requests.post(
            f"{S_URL}/get_weather",
            params={"city": city, "question": question}
        )

        data = res.json()
        st.write(data["messages"][-1]["content"])