import numpy as np
import pandas as pd                   #manipular la información
import matplotlib.pyplot as plt        #graficar   
import streamlit as st

df = pd.read_csv('datos.csv')   #cargar los datos



st.title("Tasa de Desempleo")



df.set_index('Fecha')['Tasa de Desempleo'].dropna().plot()


st.pyplot()

st.title("Inflación Anual")


df.set_index('Fecha')['Inflación Anual'].dropna().plot()


st.pyplot()

st.title("PIB Trimestral")


df.set_index('Fecha')['PIB Trimestral'].dropna().plot()


st.pyplot()

st.title("Tasa de Interes")

df.set_index('Fecha')['Tasa de Interes'].dropna().plot()

st.pyplot()