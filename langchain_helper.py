import os
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

os.environ["GOOGLE_API_KEY"] = st.secrets["GOOGLE_API_KEY"]

MODEL = "gemini-3.5-flash-lite"
llm = ChatGoogleGenerativeAI(model=MODEL, temperature=0.7)

name_prompt = PromptTemplate(
    input_variables=["cuisine"],
    template="I want to open a restaurant for {cuisine} food. Suggest one fancy name. Only the name, nothing else."
)
menu_prompt = PromptTemplate(
    input_variables=["restaurant_name"],
    template="Suggest 6 menu items for the restaurant {restaurant_name}. Return only a comma separated list, nothing else."
)

name_chain = name_prompt | llm | StrOutputParser()
menu_chain = menu_prompt | llm | StrOutputParser()

def generate_restaurant_name_and_items(cuisine):
    name = name_chain.invoke({"cuisine": cuisine}).strip()
    items = menu_chain.invoke({"restaurant_name": name})
    return {"restaurant_name": name, "menu_items": items}
