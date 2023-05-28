import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_csv('top5_leagues_player.csv')
df.drop(df.columns[0], axis=1, inplace=True)

st.write("Here's our first attempt at using data to create a table:")
st.write(df)

liga_filter_options = ['Alle'] + list(df['league'].unique())
liga_filter = st.selectbox('Liga auswählen', liga_filter_options)

club_filter_options = ['Alle'] + list(df['club'].unique())
club_filter = st.selectbox('Verein auswählen', club_filter_options)

nationality_filter_options = ['Alle'] + list(df['nationality'].unique())
nationality_filter = st.selectbox('Nationalität auswählen', nationality_filter_options)

position_filter_options = ['Alle'] + list(df['position'].unique())
position_filter = st.selectbox('Position auswählen', position_filter_options)

age_range = st.slider('Alter auswählen', int(df['age'].min()), int(df['age'].max()), (int(df['age'].min()), int(df['age'].max())))


if st.button('Filter anwenden'):
    # Filter anwenden
    filtered_data = df[
        ((liga_filter == 'Alle') | (df['league'] == liga_filter)) &
        ((club_filter == 'Alle') | (df['club'] == club_filter)) &
        ((nationality_filter == 'Alle') | (df['nationality'] == nationality_filter)) &
        ((position_filter == 'Alle') | (df['position'] == position_filter)) &
        df['age'].between(age_range[0], age_range[1])
    ]
    # Gefilterte Daten anzeigen
    st.write('Gefilterte Daten:')
    st.write(filtered_data)



#chart_data = pd.DataFrame(
#np.random.randn(20, 3),
#columns=['a', 'b', 'c'])
#st.line_chart(chart_data)

@st.cache
def fetch_and_clean_data(url):
    # Fetch data from URL here, and then clean it up.
    return data