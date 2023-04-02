
import numpy as np
import pickle
import pandas as pd

import streamlit as st 

from PIL import Image



pickle_in = open("./classifier.pkl","rb")
classifier=pickle.load(pickle_in)


def predict_car_price(name1,location1,year1,kilometers_driven1,fuel_type1,transmission1,owner_type1,mileage1,engine1,power1,seats1,new_price1):
    
    name=[]
    location=[]
    year=[]
    kilometers_driven=[]
    fuel_type=[]
    transmission=[]
    owner_type=[]
    mileage=[]
    engine=[]
    power=[]
    seats=[]
    new_price=[]
    name.insert(0,name1)
    location.insert(0,location1) 
    year.insert(0,year1)
    kilometers_driven.insert(0,kilometers_driven1)
    fuel_type.insert(0,fuel_type1)
    transmission.insert(0,transmission1)
    owner_type.insert(0,owner_typ1)
    mileage.insert(0,mileage1)
    engine.insert(0,engine1)
    power.insert(0,power1)
    seats.insert(0,seats1)
    new_price.insert(0,new_price1)
    # prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
    # print(prediction)
    # return prediction
    data={
    'Name':name,
    'Location':location,
    'Year':year,
    'Kilometers_Driven':kilometers_driven,
    'Fuel_Type':fuel_type,
    'Transmission':transmission,
    'Owner_Type':owner_type,
    'Mileage':mileage,
    'Engine':engine,
    'Power':power,
    'Seats':seats,
    'New_Price':new_price}
    df0=pd.DataFrame(data)
    make_test = df0["Name"].str.split(" ", expand = True)
    df0["Manufacturer"] = make_test[0]
    df0.drop("Name", axis = 1, inplace = True)
    df0=convert(df0)

    df0.drop("Location", axis = 1, inplace = True)
    df0.drop("New_Price", axis = 1, inplace = True)
    pred = rf.predict(df0)
    print(pred)
    return pred



def main():
    st.title("Car Price Prediction")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Bank Authenticator ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    name1 = st.text_input("Name","Type Here")
    location1 = st.text_input("Location","Type Here")
    year1 = st.number_input("Year","Type Here")
    kilometers_driven1 = st.number_input("Kilometers_Driven","Type Here")
    fuel_type1 = st.text_input("Fuel_Type","Type Here")
    transmission1 = st.text_input("Transmission","Type Here")
    owner_type1 = st.text_input("Owner_Type","Type Here")
    mileage1 = st.text_input("Mileage","Type Here")
    engine1 = st.text_input("Engine","Type Here")
    power1 = st.text_input("Power","Type Here")
    seats1 = st.number_input("Seats","Type Here")
    new_price1 = st.text_input("New_Price","Type Here")

    result=""
    if st.button("Predict"):
        result=predict_car_price(name1,location1,year1,kilometers_driven1,fuel_type1,transmission1,owner_type1,mileage1,engine1,power1,seats1,new_price1)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()