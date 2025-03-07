import streamlit as st # type: ignore

st.set_page_config(page_title="Unit Converter App", page_icon="⚖️",layout="wide")

st.markdown(
    """
    <style>
    body {
        background-color: #B9B28A;
        
    }
    .stApp {
       
        padding: 20px;
        
        font-family: 'Roboto', sans-serif;
    }


    h1 {
        color: white;
        text-align: center;
        font-size: 36px;
        font-family: 'Roboto', sans-serif;
        

    }
    .stButton>button {
        background-color:darkgray;
        color: black;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
        cursor: pointer;
    }
    .stButton>button:hover {
        background-color: gray;
        transform: scale(1.05);
        transition: transform 0.3s ease;
        color:white;
    }
    .resultbox{
        background-color: gray;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 0 10px 0 rgba(0, 0, 0, 0.1);
        font-size: 24px;
        font-weight: bold;
        text-align: center;
        font-color: black
       
    }

    
    </style>
    """,
    unsafe_allow_html=True
)


#title
st.markdown("<h1> ⚖️ Unit Converter using Python & Streamlit</h1>", unsafe_allow_html=True)



#unit selection
unit_type = st.selectbox("Select the unit type", ["Length", "Weight", "Temperature"])

value = st.number_input("Enter the value", min_value=0, value=0, step=1)

#colums
col1, col2 = st.columns(2)

#length
if unit_type == "Length":
    st.write("Length converter")
    col1, col2 = st.columns(2)
    with col1:
        
        from_unit = st.selectbox("From", ["Meter", "Kilometer", "Mile", "Yard", "Foot", "Inch", "Centimeter", "Millimeter"])
    with col2:
        
        to_unit = st.selectbox("To", ["Meter", "Kilometer", "Mile", "Yard", "Foot", "Inch", "Centimeter", "Millimeter"])

#weight
if unit_type == "Weight":
    st.write("Weight converter")
    col1, col2 = st.columns(2)
    with col1: 
        
        from_unit = st.selectbox("From", ["Kilogram", "Gram", "Milligram", "Pound", "Ounce", "Tonne", "Stone", "Pennyweight"])
    with col2:
       
        to_unit = st.selectbox("To", ["Kilogram", "Gram", "Milligram", "Pound", "Ounce"])
        
#temperature
if unit_type == "Temperature":
    st.write("Temperature converter")
    col1, col2 = st.columns(2)
    with col1:
       
        from_unit = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
    with col2:
        
        to_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])
        
#conversoin function for length
def convert_length(from_unit, to_unit, value):
    length_conversion_factors = {
        "Meter": 1,
        "Kilometer": 0.001,
        "Mile": 0.000621371,
        "Yard": 1.09361,
        "Foot": 3.28084,
        "Inch": 39.3701,
        "Centimeter": 100,
        "Millimeter": 1000
    }
    if from_unit == to_unit:
        return value
    else:
        return ((value / length_conversion_factors[from_unit]) * length_conversion_factors[to_unit])
    
#conversion function for weight
def convert_weight(from_unit, to_unit, value):
    weight_conversion_factors = {
        "Kilogram": 1,
        "Gram": 1000,
        "Milligram": 1000000,
        "Pound": 2.20462,
        "Ounce": 35.274,
        
    }
    if from_unit == to_unit:
        return value
    else:
        return ((value / weight_conversion_factors[from_unit]) * weight_conversion_factors[to_unit])

#conversion function for temperature
def convert_temperature(from_unit, to_unit, value):
   
    if from_unit == "Celsius":
        return((value *  9/5) + 32) if to_unit== "Fahrenheit" else value +  273.15 if to_unit == "Kelvin" else value
    
    elif from_unit == "Fahrenheit":
        return((value - 32) * 5/9) if to_unit == "Celsius" else (value - 32)  * 5/9 + 273.15 if to_unit == "Kelvin" else value 
    
    elif from_unit == "Kelvin":
        return((value -273.15)) if to_unit == "Celsius" else (value-273.15) * 9/5 + 32 if to_unit == "Fahrenheit" else value
    return value

#conversion button
if st.button("⚖️ Convert"):
    if unit_type == "Length":
        result = convert_length(from_unit, to_unit, value)
    elif unit_type == "Weight":
        result = convert_weight(from_unit, to_unit, value)
    elif unit_type == "Temperature":
        result = convert_temperature(from_unit, to_unit, value)
    st.markdown(f"<div class ='resultbox'> {value} {from_unit} = {result} {to_unit}</div>",unsafe_allow_html=True)
