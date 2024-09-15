import streamlit as st
import pandas as pd

def create_item():
    st.subheader("Create New Item")
    name = st.text_input("Name")
    email = st.text_input("Email")
    if st.button("Create"):
        new_id = st.session_state.data['id'].max() + 1 if not st.session_state.data.empty else 1
        new_item = pd.DataFrame({"id": [new_id], "name": [name], "email": [email]})
        st.session_state.data = pd.concat([st.session_state.data, new_item], ignore_index=True)
        st.success("Item created successfully!")


def read_items():
    st.subheader("Read Items")
    st.dataframe(st.session_state.data)


def update_item():
    st.subheader("Update Item")
    id_to_update = st.number_input("Enter ID to update", min_value=1, step=1)
    if id_to_update in st.session_state.data['id'].values:
        item = st.session_state.data[st.session_state.data['id'] == id_to_update].iloc[0]
        name = st.text_input("Name", value=item['name'])
        email = st.text_input("Email", value=item['email'])
        if st.button("Update"):
            st.session_state.data.loc[st.session_state.data['id'] == id_to_update, 'name'] = name
            st.session_state.data.loc[st.session_state.data['id'] == id_to_update, 'email'] = email
            st.success("Item updated successfully!")
    else:
        st.error("ID not found")


def delete_item():
    st.subheader("Delete Item")
    id_to_delete = st.number_input("Enter ID to delete", min_value=1, step=1)
    if id_to_delete in st.session_state.data['id'].values:
        if st.button("Delete"):
            st.session_state.data = st.session_state.data[st.session_state.data['id'] != id_to_delete].reset_index(
                drop=True)
            st.success("Item deleted successfully!")
    else:
        st.error("ID not found")