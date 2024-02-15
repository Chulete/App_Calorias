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
# Cálculo del primer alimento
with st.expander("Alimento 1"):
    peso_alimento_1 = st.number_input("Peso del alimento")
    calorias_1 = st.number_input("Calorías por cada 100 gramos")
    total_calorias_1 = (peso_alimento_1 * calorias_1) / 100
    st.write(f"{total_calorias_1} calorías")

# Cálculo del segundo alimento
with st.expander("Alimento 2"):
    peso_alimento_2 = st.number_input("Peso del alimento")
    calorias_2 = st.number_input("Calorías por cada 100 gramos")
    total_calorias_2 = (peso_alimento_2 * calorias_2) / 100
    st.write(f"{total_calorias_2} calorías")

# Cálculo del tercer alimento
with st.expander("Alimento 3"):
    peso_alimento_3 = st.number_input("Peso del alimento")
    calorias_3 = st.number_input("Calorías por cada 100 gramos")
    total_calorias_3 = (peso_alimento_3 * calorias_3) / 100
    st.write(f"{total_calorias_3} calorías")

suma_total_calorias = total_calorias_1 + total_calorias_2 + total_calorias_3
st.write(f'Total calorías añadidas {suma_total_calorias}')








