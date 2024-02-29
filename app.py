
import numpy as np
import streamlit as st
import pickle
import json
    
def get_locations():
    with open("columns.json", "r") as f:
        global data
        data = json.load(f)["data_columns"]
        global locations 
        locations = data[3:]


def load_model():

    with open("final_model.pickle", "rb") as f:
        global model 
        model = pickle.load(f)

def get_price(location, sqft,bhk,bath):
    
    loc_index = data.index(location.lower())
    x  = np.zeros(len(data))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >=0:
        x[loc_index] = 1
    x = x.reshape(1,-1)
    return model.predict([x][0])

get_locations()
load_model()


st.title("Bangalore House Price Prediction")

form = st.form(key="Form Datas")
location_to_predict = form.selectbox("Select Location",options= locations)
sqft_to_predict = form.number_input("Insert a number", value=None, placeholder="Give the squarefeet")
bhk_to_predict = form.number_input("Enter the number of Bedrooms", min_value=1,max_value= 7)
bath_to_predict = form.number_input("Enter the number of Bathrooms", min_value=1, max_value= 7)

buttonvalue = form.form_submit_button()

if buttonvalue:
    price_value = round(float(get_price(location_to_predict, sqft_to_predict,bhk_to_predict,bath_to_predict )),2)
    st.write(f"The Estimated Price is {price_value} Lakhs", )
