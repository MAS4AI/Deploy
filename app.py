# import streamlit as st
# from joblib import load
# import sklearn
# import pandas as pd
# import numpy as np
# ridge_model_loaded = load('majed_model.joblib')



# primaryColor="#F63366"
# backgroundColor="#FFFFFF"
# secondaryBackgroundColor="#F0F2F6"
# textColor="#262730"
# font="sans serif"
# # Streamlit form for user input
# def user_input_form():
#     st.title('Car Feature Input Form')
    
#     # Dictionary to store user inputs
#     user_data = {}

#     # we can make one radio which will make the user choose the company name then the select box will appear with the company name models################
#     with st.chat_message("user"):
#         st.write("Hello 👋 welcome to Eng.Majed AutoMobile Shop!")
        
#     user_data['make_model'] = st.selectbox('Make and Model', options=
#         ['Volvo V40', 'Ford Mondeo', 'Renault Megane', 'Opel Astra',
#        'Opel Adam', 'SEAT Leon', 'Nissan Pulsar', 'Hyundai i30',
#        'Skoda Scala', 'Ford Focus', 'Dacia Sandero', 'Fiat Panda',
#        'Ford Mustang', 'Fiat 500X', 'Renault Captur', 'Nissan Qashqai',
#        'Renault Talisman', 'Peugeot 308', 'Volvo XC40', 'Ford Fiesta',
#        'Renault Kadjar', 'Fiat 500C', 'Toyota Yaris', 'Skoda Fabia',
#        'Renault Clio', 'Opel Insignia', 'Peugeot 2008', 'SEAT Ibiza',
#        'Opel Cascada', 'Dacia Duster', 'Skoda Karoq', 'Hyundai i20',
#        'Peugeot 206', 'Volvo XC60', 'Toyota RAV 4', 'Opel Corsa',
#        'Toyota Corolla', 'Peugeot 3008', 'Hyundai TUCSON', 'Peugeot 208',
#        'Fiat 500', 'SEAT Arona', 'Volvo S60', 'Opel Grandland X',
#        'Dacia Logan', 'Peugeot RCZ', 'Nissan Micra', 'Skoda Kodiaq',
#        'Toyota C-HR', 'Skoda Superb', 'SEAT Ateca', 'Hyundai IONIQ',
#        'Skoda Octavia', 'Toyota Auris', 'Volvo V90', 'Fiat Tipo',
#        'Peugeot 207', 'Volvo XC90', 'Volvo S90', 'Volvo C30',
#        'Nissan 370Z', 'Volvo C70', 'Nissan Juke', 'Nissan X-Trail',
#        'Mercedes-Benz A 180', 'Toyota Aygo', 'Volvo V60', 'Peugeot 508',
#        'Nissan 350Z', 'Ford Kuga'],
#        )
#     user_data['body_type'] = st.selectbox('Body Type',options=
#         ['Compact', 'Station wagon', 'Coupe', 'Sedan', 'Off-Road/Pick-up','Convertible'])
#     user_data['type'] = st.selectbox('Type', options=['Used', "Employee's car", 'Demonstration', 'Pre-registered'])
#     user_data['warranty'] = st.sidebar.radio('Warranty', options=['Yes', 'No'])
#     user_data['mileage'] = st.number_input('Mileage', value=0.0)
#     user_data['gearbox'] = st.selectbox('Gearbox', options=['Manual', 'Automatic','Semi-automatic'])
#     user_data['fuel_type'] = st.selectbox('Fuel Type', options=['Diesel', 'Benzine', 'Liquid/Natural Gas', 'Electric'])
#     user_data['seller'] = st.selectbox('Seller', options=['Dealer', 'Private seller'])
#     user_data['engine_size'] = st.number_input('Engine Size (cc)', value=1500.0)
#     user_data['gears'] = st.number_input('Gears', value=6.0)
#     user_data['co_emissions'] = st.slider('CO2 Emissions (g/km)',0,500)
#     user_data['drivetrain'] = st.selectbox('Drivetrain', options=['Front', '4WD', 'Rear'])
#     user_data['extras'] = st.number_input('Extras', value=8)
#     user_data['empty_weight'] = st.number_input('Empty Weight (kg)', value=1280.0)
#     user_data['full_service_history'] = st.sidebar.radio('Full Service History', options=['Yes', 'No'])
#     user_data['upholstery'] = st.selectbox('Upholstery', options=['Part/Full Leather', 'Cloth'])
#     user_data['previous_owner'] = st.number_input('Previous Owners', value=1.0)
#     user_data['energy_efficiency_class'] = st.selectbox('Energy Efficiency Class', options=['efficient', 'inefficient'])
#     user_data['age'] = st.number_input('Age (years)', value=2.0)
#     user_data['power_kW'] = st.number_input('Power (kW)', value=88.0)
#     user_data['cons_avg'] = st.number_input('Average Consumption (l/100 km)', value=3.6)
#     user_data['comfort_&_convenience_Package'] = st.selectbox('Comfort & Convenience Package', options=['Standard', 'Premium', 'Premium Plus'])
#     user_data['entertainment_&_media_Package'] = st.selectbox('Entertainment & Media Package', options=['Standard', 'Plus'])
#     user_data['safety_&_security_Package'] = st.selectbox('Safety & Security Package', options=['Safety Standard Package', 'Safety Premium Package', 'Safety Premium Plus Package'])

#     # Submit button
#     submit_button = st.button('Submit')
    
#     if submit_button:
#         ii = pd.DataFrame([user_data])
        
#         i = ridge_model_loaded.predict(ii)
#         print(i)
#         st.table(ii)
#         st.text(i)
# user_input_form()




import streamlit as st
from joblib import load
import pandas as pd

# Load the pre-trained Ridge model
ridge_model_loaded = load('majed_model.joblib')
st.markdown("""
    <style>
        .main_container {
            background-color: #FFFFFF;
        }
        h1 {
            text-align: center;
            color: #0E1117;
        }
        .sidebar .sidebar-content {
            background-color: #F2F2F2;
        }
        .stButton>button {
            color: #ffffff;
            background-color: #FF4B4B;
            border: none;
            border-radius: 4px;
            padding: 0.75rem 1.5rem;
            margin: 0.75rem 0;
        }
        .stButton>button:hover {
            background-color: #FF0000;
        }
    </style>
""", unsafe_allow_html=True)
# st.set_page_config(page_title='Car Price Prediction', layout='wide')

# Set page title and background color
with st.chat_message("user"):
     st.write("Hello 👋 welcome to Eng.Majed AutoMobile Shop!")
# Define the main title and description
st.title('Car Price Prediction')


# Create a sidebar for additional information (optional)
st.sidebar.title('About')
st.sidebar.write("This app predicts car prices based on the provided features.")

# Create a multi-column layout for better organization
col1, col2 = st.columns(2)

# User input form in col1
with col1:
    st.header('Car Features')
    user_data = {}
    user_data['make_model'] = st.selectbox('Make and Model', options=['Volvo V40', 'Ford Mondeo', 'Renault Megane', 'Opel Astra',
       'Opel Adam', 'SEAT Leon', 'Nissan Pulsar', 'Hyundai i30',
       'Skoda Scala', 'Ford Focus', 'Dacia Sandero', 'Fiat Panda',
       'Ford Mustang', 'Fiat 500X', 'Renault Captur', 'Nissan Qashqai',
       'Renault Talisman', 'Peugeot 308', 'Volvo XC40', 'Ford Fiesta',
       'Renault Kadjar', 'Fiat 500C', 'Toyota Yaris', 'Skoda Fabia',
       'Renault Clio', 'Opel Insignia', 'Peugeot 2008', 'SEAT Ibiza',
       'Opel Cascada', 'Dacia Duster', 'Skoda Karoq', 'Hyundai i20',
       'Peugeot 206', 'Volvo XC60', 'Toyota RAV 4', 'Opel Corsa',
       'Toyota Corolla', 'Peugeot 3008', 'Hyundai TUCSON', 'Peugeot 208',
       'Fiat 500', 'SEAT Arona', 'Volvo S60', 'Opel Grandland X',
       'Dacia Logan', 'Peugeot RCZ', 'Nissan Micra', 'Skoda Kodiaq',
       'Toyota C-HR', 'Skoda Superb', 'SEAT Ateca', 'Hyundai IONIQ',
       'Skoda Octavia', 'Toyota Auris', 'Volvo V90', 'Fiat Tipo',
       'Peugeot 207', 'Volvo XC90', 'Volvo S90', 'Volvo C30',
       'Nissan 370Z', 'Volvo C70', 'Nissan Juke', 'Nissan X-Trail',
       'Mercedes-Benz A 180', 'Toyota Aygo', 'Volvo V60', 'Peugeot 508',
       'Nissan 350Z', 'Ford Kuga'])  # Add all options
    user_data['body_type'] = st.selectbox('Body Type', options=['Compact', 'Station wagon', 'Coupe', 'Sedan', 'Off-Road/Pick-up','Convertible'])
    user_data['type'] = st.selectbox('Type', options=['Used', "Employee's car", 'Demonstration', 'Pre-registered'])
    user_data['warranty'] = st.radio('Warranty', options=['Yes', 'No'])
    user_data['mileage'] = st.number_input('Mileage', value=0.0)
    user_data['gearbox'] = st.selectbox('Gearbox', options=['Manual', 'Automatic', 'Semi-automatic'])
    user_data['fuel_type'] = st.selectbox('Fuel Type', options=['Diesel', 'Benzine', 'Liquid/Natural Gas', 'Electric'])
    user_data['seller'] = st.selectbox('Seller', options=['Dealer', 'Private seller'])
    user_data['engine_size'] = st.number_input('Engine Size (cc)', value=1500.0)
    user_data['gears'] = st.number_input('Gears', value=6.0)
    user_data['co_emissions'] = st.slider('CO2 Emissions (g/km)', 0, 500)
    user_data['drivetrain'] = st.selectbox('Drivetrain', options=['Front', '4WD', 'Rear'])
    user_data['extras'] = st.number_input('Extras', value=8)
    user_data['empty_weight'] = st.number_input('Empty Weight (kg)', value=1280.0)
    user_data['full_service_history'] = st.radio('Full Service History', options=['Yes', 'No'])
    user_data['upholstery'] = st.selectbox('Upholstery', options=['Part/Full Leather', 'Cloth'])
    user_data['previous_owner'] = st.number_input('Previous Owners', value=1.0)
    user_data['energy_efficiency_class'] = st.selectbox('Energy Efficiency Class', options=['efficient', 'inefficient'])
    user_data['age'] = st.number_input('Age (years)', value=2.0)
    user_data['power_kW'] = st.number_input('Power (kW)', value=88.0)
    user_data['cons_avg'] = st.number_input('Average Consumption (l/100 km)', value=3.6)
    user_data['comfort_&_convenience_Package'] = st.selectbox('Comfort & Convenience Package', options=['Standard', 'Premium', 'Premium Plus'])
    user_data['entertainment_&_media_Package'] = st.selectbox('Entertainment & Media Package', options=['Standard', 'Plus'])
    user_data['safety_&_security_Package'] = st.selectbox('Safety & Security Package', options=['Safety Standard Package', 'Safety Premium Package', 'Safety Premium Plus Package'])

    # Submit button
    submit_button = st.button('Predict Price')

# Prediction and display in col2
with col2:
    st.header('Car Price Prediction')
    if submit_button:
        # Create a DataFrame with user input
        user_input_df = pd.DataFrame([user_data])

        # Make a prediction using the loaded model
        predicted_price = ridge_model_loaded.predict(user_input_df)[0]

        # Display the prediction to the user
        st.subheader('Estimated Car Price:')
        st.write(f'${predicted_price:.2f}')

# Optionally, you can add more styling using CSS
st.markdown(
    """
    <style>
    .css-1v3fvcr {
        background-color: #F0F2F6;
    }
    .css-1ehg38r {
        background-color: #FF2F1F;
        color: #FFFFFF;
        text-align: center;
        padding: 10px;
        border-radius: 5px;
        margin-bottom: 20px;
    }
    .css-1l01bc7 {
        padding: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

