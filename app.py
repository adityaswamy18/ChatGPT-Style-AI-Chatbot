import streamlit as st
import requests


if "conversasion" not in st.session_state:
    st.session_state["conversasion"]=[]


prompt=st.chat_input("Type your message")

if prompt:
    st.session_state["conversasion"].append({"role":"user","data":prompt})
    # st.session_state["conversasion"].append(prompt)
    response=requests.post("https://patilpatil.app.n8n.cloud/webhook/24b2321d-5ded-43d3-ad2d-cb3079453f97",json={"prompt":prompt})

    if response.status_code==200:
        st.session_state["conversasion"].append({"role":"AI","data":response.json()["output"]})
         # st.session_state["conversasion"].append(response.json()["output"])

for con in st.session_state["conversasion"]:
    # st.write(con)
    with st.chat_message(con["role"]):
        st.write(con["data"])