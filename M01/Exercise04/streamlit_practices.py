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
# Initialize session state for the text inputs if they don't exist
if 'text_input_1' not in st.session_state:
    st.session_state.text_input_1 = ""
if 'text_input_2' not in st.session_state:
    st.session_state.text_input_2 = ""
if 'submitted_text_1' not in st.session_state:
    st.session_state.submitted_text_1 = ""
if 'submitted_text_2' not in st.session_state:
    st.session_state.submitted_text_2 = ""

# Function to handle the submit button for text input 1
def submit_text_1():
    st.session_state.submitted_text_1 = st.session_state.text_input_1

# Function to handle the submit button for text input 2
def submit_text_2():
    st.session_state.submitted_text_2 = st.session_state.text_input_2

# Function to handle the clear button for text input 1
def clear_text_1():
    st.session_state.text_input_1 = ""
    st.session_state.submitted_text_1 = ""
    st.experimental_rerun()  # Rerun the app to update the UI

# Function to handle the clear button for text input 2
def clear_text_2():
    st.session_state.text_input_2 = ""
    st.session_state.submitted_text_2 = ""
    st.experimental_rerun()  # Rerun the app to update the UI

# Creating two text input fields with keys
text_input_1 = st.text_input("Enter some text for input 1:", key='text_input_1')
text_input_2 = st.text_input("Enter some text for input 2:", key='text_input_2')

# Creating a row with four buttons (submit and clear for each input)
col1, col2, col3, col4 = st.columns([1, 1, 1, 1])  # Adjust the values to control spacing

with col1:
    if st.button("Submit Input 1"):
        submit_text_1()
        st.write("Submitted text 1:", st.session_state.submitted_text_1)

with col2:
    if st.button("Clear Input 1"):
        clear_text_1()
        st.empty()

with col3:
    if st.button("Submit Input 2"):
        submit_text_2()
        st.write("Submitted text 2:", st.session_state.submitted_text_2)

with col4:
    if st.button("Clear Input 2"):
        clear_text_2()

# Optionally display the current value of the text inputs
st.write("Current text input 1 value:", st.session_state.text_input_1)
st.write("Current text input 2 value:", st.session_state.text_input_2)