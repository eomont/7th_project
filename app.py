import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Proyecto #7: Despliegue de aplicación en Render') #Encabezado 
st.write('Conjunto de datos de anuncios de coches') #Mensaje descriptivo


car_data = pd.read_csv('vehicles_us.csv') # leer los datos
hist_button = st.button('Construir histograma') # crear un botón
scatter_checkbox = st.checkbox("Construir scatter") #Creación del botón para diagrama de dispersión


if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
    


if scatter_checkbox:
    st.write('Creación de un diagrama de dispersión para el conjunto de datos de anuncios de venta de coches') # Mostrar mensaje
    
    fig = px.scatter(car_data, x="odometer", y="price") # crear un gráfico de dispersión
    
    st.plotly_chart(fig, use_container_width=True) #Gráfico de dispersión interactivo
