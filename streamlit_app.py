import pandas as pd
import streamlit as st
import requests
import time

# Create empty DataFrame to store status and timestamp information
df = pd.DataFrame(columns=["status", "timestamp"])

url = "https://users.chpc.ac.za"

while True:
    try:
        response = requests.get(url, verify=True)
        if response.status_code == 200:
            status = "up"
            st.write(f"{url} is up!")
        else:
            status = "down"
            st.write(f"{url} is down (status code {response.status_code})")
    except requests.exceptions.RequestException as e:
        status = "down"
        st.write(f"{url} is down ({e})")
        
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    st.write(f"Timestamp: {timestamp}")
    
    # Update DataFrame with status and timestamp information
    df.loc[len(df)] = [status, timestamp]
    
    # Display DataFrame in Streamlit app
    st.write(df)
    
    time.sleep(30)
