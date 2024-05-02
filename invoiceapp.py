import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection

url = "https://docs.google.com/spreadsheets/d/12Xz2kB_0mos07T-SGy6REs7yDvjxn3Y_5vn8F25T05A/edit#gid=0"

conn = st.experimental_connection("gsheets", type = GSheetsConnection)
data = conn.read(spreadsheet=url)
st.dataframe(data)

df = pd.DataFrame(data)

if 'updated_df' not in st.session_state:
    st.session_state.updated_df = df.copy()

for i, row in st.session_state.updated_df.iterrows():
    # The key ensures each checkbox is unique
    new_value = st.checkbox("Vendido?", value=row['Vendido'], key=i, help="Select if sold")
    st.session_state.updated_df.at[i, 'Vendido'] = new_value

st.write("Updated DataFrame:", st.session_state.updated_df)