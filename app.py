import streamlit as st
import pandas as pd
import plotly.express as px

st.header("Análisis de vehículos en EE.UU.")  # encabezado visible

# Leer los datos
car_data = pd.read_csv('vehicles_us.csv')

# Botón para histograma
if st.button('Mostrar histograma'):
    st.write('Histograma del odómetro')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig)

# Botón para gráfico de dispersión
if st.button('Mostrar gráfico de dispersión'):
    st.write('Dispersión entre odómetro y precio')
    fig2 = px.scatter(car_data, x='odometer', y='price')
    st.plotly_chart(fig2)




