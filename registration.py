import streamlit as st

# ---------------- CSS ----------------

css = """
<style>

.stApp {
    background-color: #eaf4ff;
}

h1 {
    text-align: center;
    color: #1f4e79;
    font-size: 42px;
    font-weight: bold;
}

h2 {
    color: #2e75b6;
}

h3 {
    color: #1f4e79;
}

p {
    color: #333333;
    font-size: 16px;
}

.stTextInput input {
    background-color: white;
    border: 2px solid #9ec5e8;
    border-radius: 8px;
}

.stNumberInput input {
    background-color: white;
    border: 2px solid #9ec5e8;
    border-radius: 8px;
}

.stTextArea textarea {
    background-color: white;
    border: 2px solid #9ec5e8;
    border-radius: 8px;
}

.stSelectbox div[data-baseweb="select"] > div {
    background-color: white;
    border: 2px solid #9ec5e8;
    border-radius: 8px;
}

.stButton button {
    width: 100%;
    background-color: #1f77b4;
    color: white;
    border-radius: 8px;
    border: none;
    padding: 10px;
    font-size: 18px;
    font-weight: bold;
}

.stButton button:hover {
    background-color: #155a8a;
    color: white;
}

</style>
"""

st.markdown(css, unsafe_allow_html=True)
st.title("🎓 Student Registration")
st.header("Welcome to the Student Registration Portal")
st.write("Please fill in the details below to register as a student.")
st.subheader("Personal Details")
name = st.text_input("Enter your full name:")
email = st.text_input("Enter your email:")
phone = st.text_input("Enter your phone number:")
age = st.number_input("Enter your age:",min_value=1,max_value=100)
gender = st.radio("Select your gender:",["Female", "Male", "Other"])
st.subheader("Academic Details")
college = st.text_input("Enter your college name:")
course = st.selectbox("Select your course:",["B.Tech", "B.Sc", "B.Com", "BCA", "MCA", "MBA"])
branch = st.selectbox("Select your branch:",["CSE", "AIML", "ECE", "EEE", "IT", "Civil", "Mechanical"])
year = st.selectbox("Select your year:",["1st Year", "2nd Year", "3rd Year", "4th Year"])
st.subheader("Account Details")
username = st.text_input("Create a username:")
password = st.text_input("Create a password:",type="password")
confirm_password = st.text_input("Confirm your password:",type="password")
st.subheader("Additional Information")
message = st.text_area("Tell us something about yourself:")
agree = st.checkbox("I agree to the terms and conditions.")
if st.button("Register"):
    if name == "":
        st.error("Please enter your name.")
    elif email == "":
        st.error("Please enter your email.")
    elif password != confirm_password:
        st.error("Passwords do not match.")
    elif not agree:
        st.warning("Please agree to the terms and conditions.")
    else:
        st.success("🎉 Registration successful!")
        st.write("Name:", name)
        st.write("Email:", email)
        st.write("Course:", course)
        st.write("Branch:", branch)
        st.write("Year:", year)
st.caption("© 2026 Student Registration Portal")
