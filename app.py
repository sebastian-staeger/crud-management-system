import streamlit as st
import pandas as pd

from st_pages import add_page_title, get_nav_from_toml

from src.views.components import create_item, read_items, update_item, delete_item
from src.views.auth_view import login, logout

users_db = pd.DataFrame({
    "username": ["admin", "user"],
    "password": ["8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918",
                 "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"]
})

if 'data' not in st.session_state:
    st.session_state.data = pd.DataFrame({
        "id": [1, 2, 3],
        "name": ["John Doe", "Jane Smith", "Bob Johnson"],
        "email": ["john@example.com", "jane@example.com", "bob@example.com"]
    })

# Initialize session state
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = None


def home():
    st.title("CRUD App with Streamlit")

    if 'data' not in st.session_state:
        st.session_state.data = pd.DataFrame({
            "id": [1, 2, 3],
            "name": ["John Doe", "Jane Smith", "Bob Johnson"],
            "email": ["john@example.com", "jane@example.com", "bob@example.com"]
        })

    menu = ["Create", "Read", "Update", "Delete"]
    choice = st.selectbox("Select Operation", menu)

    if choice == "Create":
        create_item()
    elif choice == "Read":
        read_items()
    elif choice == "Update":
        update_item()
    elif choice == "Delete":
        delete_item()

def main_page():
    st.title('Main Page')
    st.text("some text")


def app():

    # Login Logout Button
    if st.session_state.logged_in:
        st.sidebar.button("Logout", on_click=logout)
        nav = get_nav_from_toml(".streamlit/pages.toml")
        pg = st.navigation(nav)
        add_page_title(pg)

        home()
    if not st.session_state.logged_in:
        st.sidebar.button("Login", on_click=login)
        main_page()
    else:
        st.sidebar.button("Login", on_click=login)
        login()





if __name__ == "__main__":
    app()
