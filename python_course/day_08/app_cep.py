import streamlit as st
import pandas as pd
import requests

url = "https://viacep.com.br/ws/{cep}/json/"

st.title("Search CEP")

cep = st.text_input("Search your CEP")

if cep != "":

    try:
        resp = requests.get(url.format(cep=cep))
        data = pd.DataFrame([resp.json()])
        st.dataframe(data, hide_index=True)

    except Exception as err:
        st.error("Enter a valid CEP!")