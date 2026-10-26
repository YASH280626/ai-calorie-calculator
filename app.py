import streamlit as st

from src.nutrition import get_food_nutrition
from src.nutrition import calculate_nutrition
from src.nutrition import get_food_names


OPTIONS = get_food_names()

st.title("Calorie Calculator")


choice = st.sidebar.selectbox("Select a Food",
                              OPTIONS)
quantity = st.number_input("Quantity (grams)", min_value=1, value = 100, step=50)
result = {}
if st.button("Search"):
    result = calculate_nutrition(get_food_nutrition(choice), quantity)

st.write(result)



