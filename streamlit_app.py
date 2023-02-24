from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""

import requests
import time

url = "https://users.chpc.ac.za"

while True:
    try:
        response = requests.get(url, verify=True)
        if response.status_code == 200:
            st.write(f"{url} is up!")
        else:
            st.write(f"{url} is down (status code {response.status_code})")
    except requests.exceptions.RequestException as e:
        st.write(f"{url} is down ({e})")
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    st.write(f"Timestamp: {timestamp}")
    time.sleep(30)

