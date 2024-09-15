import streamlit as st
from ..utils.auth_utils import hash_password
from src.data.data import users_db


def login():
    st.title("Login")
    st.warning('Please enter your username and password')

    with st.form('my_form'):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button('Submit')

        if submitted:
            hashed_password = hash_password(password)
            user = users_db[(users_db.username == username) & (users_db.password == hashed_password)]

            if not user.empty:
                st.session_state.logged_in = True
                st.session_state.name = username
                st.rerun()
            else:
                st.error("Invalid username or password")


def logout():
    st.session_state.logged_in = None
    st.session_state.logout_succesful = True
