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
    import requests

    url = "https://users.chpc.ac.za"

    try:
        response = requests.get(url, verify=False)
        if response.status_code == 200:
            print(f"{url} is up!")
            status = 'up'
        else:
            print(f"{url} is down (status code {response.status_code})")
            status = 'down'
    except requests.exceptions.RequestException as e:
        print(f"{url} is down ({e})")
#         st.write(f"{url} is down ({e})")
        
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
#     st.write(f"Timestamp: {timestamp}")
    
    # Get the latest version of the DataFrame from the cache and append the new row
    df = create_df()
    df.loc[len(df)] = [status, timestamp]
    
    # Clear the placeholder and show the latest row of the DataFrame
    df_placeholder.empty()
    df_placeholder.dataframe(df.tail(1))
    
    time.sleep(10)
