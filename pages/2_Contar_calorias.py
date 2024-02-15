# CONTEO DE CALORÍAS

import streamlit as st
import streamlit.components.v1 as stc
import pandas as pd 
import base64



df_fruta = pd.read_excel("C:/Users/34610/Desktop/Mis_apps/Healthy/calorias_alimentos/calorias_fruta.xlsx")
df_verdura = pd.read_excel("C:/Users/34610/Desktop/Mis_apps/Healthy/calorias_alimentos/calorias_verdura.xlsx")
df_carne = pd.read_excel("C:/Users/34610/Desktop/Mis_apps/Healthy/calorias_alimentos/calorias_carne.xlsx")
df_pescado = pd.read_excel("C:/Users/34610/Desktop/Mis_apps/Healthy/calorias_alimentos/calorias_pescado.xlsx")
df_pasta = pd.read_excel("C:/Users/34610/Desktop/Mis_apps/Healthy/calorias_alimentos/calorias_pasta.xlsx")
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


col1, col2 = st.columns([2,2])
with col1:
	with st.expander("Fruta"):
		st.dataframe(df_fruta)
with col2:
	with st.expander("Verdura"):
		st.dataframe(df_verdura)

col3, col4 = st.columns([2,2])
with col3:
	with st.expander("Carne"):
		st.dataframe(df_carne)
with col4:
	with st.expander("Pescado"):
		st.dataframe(df_pescado)




