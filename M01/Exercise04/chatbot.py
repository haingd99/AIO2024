import streamlit as st
from hugchat import hugchat 
from hugchat.login import Login

st.title("Simple Chatbot")

# Login Huggingface
with st.sidebar:
    st.title("Login")
    hf_email = st.text_input("Email:")
    hf_pass = st.text_input("Password: ", type="password")
    if not (hf_email and hf_pass):
        st.warning("Please enter your email and password of HuggingFace!")
    else:
        st.success("Logged in successfull!")

if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant",\
                                   "content": "How may I help you?"}]
    
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

def gen_response(prompt, email, password):
    signin = Login(email, password)
    cookies = signin.login()
    chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
    return chatbot.chat(prompt)

if prompt := st.chat_input(disabled= not (hf_email and hf_pass)):
    st.session_state.messages.append({"role": "user",\
                                   "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = gen_response(prompt,hf_email, hf_pass)
            st.write(response)
    message = {"role": "assistant","content": response}
    st.session_state.messages.append(message)