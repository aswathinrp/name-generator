import streamlit as st
import langchain_helper

st.title("Name Generator")

letter = st.sidebar.selectbox("Pick a Letter", ("I", "A", "M", "S", "D"))


if letter:
    response = langchain_helper.generate_name(letter)
    name = response['name'].strip().split(",")
    for item in name:
        st.write("-",item)
        print(item)  # Print to the console with a newline
    # menu_items = response['menu_items'].strip().split(",")
    # st.write("**Menu Items**")
    # for item in menu_items:
    #     st.write("-", item)

