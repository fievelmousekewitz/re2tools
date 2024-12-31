import streamlit as st

pg = st.navigation([st.Page("shield.py", title="CV Shield Calc"), st.Page("binary.py", title="Binary Search")])

pg.run()
