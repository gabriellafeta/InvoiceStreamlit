import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection

url = "https://docs.google.com/spreadsheets/d/12Xz2kB_0mos07T-SGy6REs7yDvjxn3Y_5vn8F25T05A/edit#gid=0"

conn = st.experimental_connection("gsheets", type = GSheetsConnection)
data = conn.read(spreadsheet=url)

df = pd.DataFrame(data)
st.dataframe(df)
