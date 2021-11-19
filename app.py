import streamlit as st
import requests
import pandas as pd

CSS = """
.stApp {
    background-color: #7895c4;
    color: white;
}
"""
st.write(f'<style>{CSS}</style>', unsafe_allow_html=True)

'''# TaxiFareModel front
'''

# st.markdown('''
# Remember that there are several ways to output content into your web page...

# Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
# ''')
# '''
# ## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

# 1. Let's ask for:
# - date and time
# - pickup longitude
# - pickup latitude
# - dropoff longitude
# - dropoff latitude
# - passenger count
# '''
# '''
# ## Please input your ride parameters
# '''
"## Input your ride details"

columns = st.columns(2)
pickup_date = columns[0].date_input('Pickup date')
pickup_time = columns[1].time_input('Pickup time')
pickup_datetime = f"{pickup_date} {pickup_time}"

pickup_longitude  = columns[0].number_input('Pickup longitude',  step=1e-8, format='%.8f')
pickup_latitude = columns[1].number_input('Pickup latitude', step=1e-8, format='%.8f')
dropoff_longitude = columns[0].number_input('Dropoff longitude', step=1e-8, format='%.8f')
dropoff_latitude = columns[1].number_input('Dropoff latitude', step=1e-8, format='%.8f')

passenger_count   = columns[0].number_input('Number of passengers', value=1, format='%i')

"Your pickup and dropoff locations"
locations = pd.DataFrame.from_dict({
  'lon': [pickup_longitude, dropoff_longitude],
  'lat': [pickup_latitude, dropoff_latitude]
})
st.map(locations)

# '''
# ## Once we have these, let's call our API in order to retrieve a prediction

# See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

# 🤔 How could we call our API ? Off course... The `requests` package 💡
# '''

url = 'https://jules-image-n7oq3xptua-ew.a.run.app/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown(
        'Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...'
    )
# '''

# 2. Let's build a dictionary containing the parameters for our API...
# '''
params = {
    # "key": "2013-07-06 17:18:00.000000119",  # Not returned, but model requires
    # a key - hardcoded here
    "pickup_datetime"  : pickup_datetime,
    "pickup_longitude" : pickup_longitude,
    "pickup_latitude"  : pickup_latitude,
    "dropoff_longitude": dropoff_longitude,
    "dropoff_latitude" : dropoff_latitude,
    "passenger_count"  : passenger_count
}
# '''
# 3. Let's call our API using the `requests` package...
# '''

prediction = requests.get(url=url, params=params).json()['prediction']
# '''
# 4. Let's retrieve the prediction from the **JSON** returned by the API...

# ## Finally, we can display the prediction to the user
# '''
'''
## This is the prediction for your parameters:
'''

st.write(f">**{prediction}**")
