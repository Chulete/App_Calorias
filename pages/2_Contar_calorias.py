# CONTEO DE CALORÍAS

import streamlit as st
import streamlit.components.v1 as stc
import pandas as pd 
import base64

st.subheader("Cómo las cuento")
stc.iframe("https://i.pinimg.com/originals/c5/a2/4d/c5a24d98dcd5eae25128f7b04f04223a.gif",
	height=420, width=800, scrolling=True)
st.write("""Esto es tan fácil como coger una tana, váscula... y pesar la comida.
	En los siguientes deplegables se muestra las calorías por cada 100 gramos de alimento ...
	""")

col1, col2 = st.columns([2,2])
with col1:
	peso_alimento = st.number_input("Peso del alimento")
with col2:
	calorias = st.number_input("Calorías por cada 100 gramos")
if peso_alimento is not None and calorias is not None:
	total_calorias = (peso_alimento * calorias) / 100
	st.write(f"{total_calorias} calorías")

col3, col4 = st.columns([2,2])
with col3:
	peso_alimento_2 = st.number_input("Peso del alimento")
with col4:
	calorias_2 = st.number_input("Calorías por cada 100 gramos")
if peso_alimento_2 is not None and calorias_2 is not None:
	total_calorias_2 = (peso_alimento_2 * calorias_2) / 100
	st.write(f"{total_calorias_2} calorías")

col5, col6 = st.columns([2,2])
with col5:
	peso_alimento_3 = st.number_input("Peso del alimento")
with col6:
	calorias_3 = st.number_input("Calorías por cada 100 gramos")
if peso_alimento_3 is not None and calorias_3 is not None:
	total_calorias_3 = (peso_alimento_3 * calorias_3) / 100
	st.write(f"{total_calorias_3} calorías")

suma_total_calorias = total_calorias + total_calorias_2 + total_calorias_3
st.write(f'Total calorías añadidas {suma_total_calorias}')





