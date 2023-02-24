import pandas as pd
import streamlit as st
import requests
import time

# Use st.cache to cache the function that generates the DataFrame
@st.cache(allow_output_mutation=True)
def create_df():
    return pd.DataFrame(columns=["status", "timestamp"])

# Create placeholder for the DataFrame
df_placeholder = st.empty()

url = "https://users.chpc.ac.za"

while True:
    try:
        response = requests.get(url, verify=True)
        if response.status_code == 200:
            status = "up"
#             st.write(f"{url} is up!")
        else:
            status = "down"
#             st.write(f"{url} is down (status code {response.status_code})")
    except requests.exceptions.RequestException as e:
        status = "down"
#         st.write(f"{url} is down ({e})")
        
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    st.write(f"Timestamp: {timestamp}")
    
    # Get the latest version of the DataFrame from the cache and append the new row
    df = create_df()
    df.loc[len(df)] = [status, timestamp]
    
    # Clear the placeholder and show the latest row of the DataFrame
    df_placeholder.empty()
    df_placeholder.dataframe(df.tail(1))
    
    time.sleep(30)
