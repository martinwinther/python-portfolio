import streamlit as st
from send_email import send_email

st.header("Contact Me")

st.write("If you have any questions or want to collaborate, feel free to reach out to me.")

with st.form(key="email_form"):
    user_email = st.text_input("Your Email Address")
    raw_message = st.text_area("Your Message")
    message = f"""\
    Subject: New email from {user_email}
    
    From: {user_email}
    {raw_message}
    """
    submit_button = st.form_submit_button(label="Send")
    if submit_button:
        send_email(message)
        st.info("Thank you for your message!")
        st.balloons()

