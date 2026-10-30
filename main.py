import streamlit as st
import langchain_helper as lch

st.title("Restaurant Name Generator")

cuisine = st.sidebar.selectbox(
    "Pick a cuisine", ("Indian", "Italian", "Mexican", "Arabic", "American")
)

@st.cache_data
def get_result(c):
    return lch.generate_restaurant_name_and_items(c)

if cuisine:
    response = get_result(cuisine)
    st.header(response["restaurant_name"])
    st.write("**Menu Items**")
    for item in response["menu_items"].strip().split(","):
        st.write("-", item.strip())
