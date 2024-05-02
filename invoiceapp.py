import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection

url = "https://docs.google.com/spreadsheets/d/12Xz2kB_0mos07T-SGy6REs7yDvjxn3Y_5vn8F25T05A/edit#gid=0"

conn = st.experimental_connection("gsheets", type = GSheetsConnection)
data = conn.read(spreadsheet=url)
st.dataframe(data)

df = pd.DataFrame(data)


selected_indices = st.multiselect('Select rows:', df.index, default=df.index)
selected_rows = df.loc[selected_indices]
st.write('Selected Rows', selected_rows)

if not selected_rows.empty:
    # Convert DataFrame to CSV
    csv = selected_rows.to_csv(index=False)
    # Create a link to download the CSV file
    
    st.download_button(
        label="Download selected rows as CSV",
        data=csv,
        file_name='selected_rows.csv',
        mime='text/csv',
    )