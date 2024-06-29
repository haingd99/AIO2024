import streamlit as st

st.title("This is Streamlit Practices")
st.header("Step by step to work with Streamlit")
st.subheader("This is Subheader")

st.divider()

st.header("Button Interactive")
if st.button("Say Hello"):
    print(st.write("Hello!"))

st.divider()

st.header("Working with layout")
question = st.text_input(label="Input your question: ", key="question01")

col1, col2 = st.columns([1,6])

with col1:
    if st.button("Submit"):
        st.write("Submited", question)

with col2:
    if st.button("Cancel"):        
        st.write("Cancelled")

st.divider()
st.subheader("Multiselect Box")

options = st.multiselect("Multi select colors:", ["Red", "Green", "Yellow", "Blue"], ["Yellow", "Blue"])
st.write("You selected: ", options)

st.divider()
st.subheader("Working with form")

with st.form("my_form"):
    col1, col2 = st.columns(2)
    f_name = col1.text_input("First Name: ")
    l_name = col2.text_input("Last Name: ")
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("First Name: ", f_name, " - Last Name: ", l_name)


st.divider()
st.subheader("Upload file")

with st.form("upload_files"):
    st.markdown("1. Upload a file:")
    a_file = st.file_uploader("Select Files: ", accept_multiple_files=False)
    st.markdown("1. Upload multi files:")
    files = st.file_uploader("Select Files: ", accept_multiple_files=True)
    submitted = st.form_submit_button("Submit")
    if submitted:
        if a_file:
            st.write("You submitted a file: ", a_file)
        
        if files:
            st.write("You submitted multi files: ", files, "Total files: ",len(files))

st.divider()
st.subheader("Working with slide")
st.slider("Select values: ", 0, 100, value=50, step=5, key ="slider1")
st.slider("Select values: ", .0, 1., value=0.1, step=0.1, key="slider2")



