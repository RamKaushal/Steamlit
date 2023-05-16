import pandas as pd
import streamlit as st

st.header("Forecast selector")

slide = st.sidebar.selectbox('Forecast page selector',['Forecast analysis','About forecast','Teammembers'])
if slide =='Forecast analysis':
    st.subheader("Please select the Region")
    region = st.selectbox("Region",['EMEA','NA'])
    if region=='EMEA':
        st.table(pd.DataFrame(data = {
            'region': ['EMEA']*10, 
            'forecast selector': list(range(1, 11)),
            'startdate': ['2022-01-01']*10,
            'enddate': ['2022-12-31']*10,
            'username': ['Ram']*10
        }))
    else:
        st.table(pd.DataFrame(data = {
        'region': ['NA']*10, 
        'forecast selector': list(range(1, 11)),
        'startdate': ['2022-01-01']*10,
        'enddate': ['2022-12-31']*10,
        'username': ['Kaushal']*10
        }))

if slide == 'About forecast':
    st.write("Forecast for EMEA and NA")
elif slide == 'Teammembers':
    st.write('Ram','Kaushal')
    