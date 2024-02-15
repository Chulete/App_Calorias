# CÁLCULO DE CALORÍAS PARA ALCANZAR OBJETIVOS
import pandas as pd 
import streamlit as st
import streamlit.components.v1 as stc

titulo = """
		<div style="background-color:rgb(0, 167, 179);padding:10px;border-radius:10px">
		<h1 style="color:white;text-align:center;">FITÁSTICO</h1>
		<h4 style="color:white;text-align:center;">(App para el cálculo de calorías)</h4>
		</div>
		"""


# Función main()
def main():
	st.markdown("""
		<style>
		body {background-color: yellow;}
		</style>""",
		unsafe_allow_html=True)

	stc.html(titulo)
	st.subheader("Intenciones de la app")
	st.markdown('''
		Esta aplicación está diseñada para ayudar a conseguir los objetivos relacionados con el peso corporal. <br>
		Con una dieta saludable y una vida activa se puede lograr un peso óptimo que te repercurtirá positivamente 
		en el futuro.''',
		unsafe_allow_html=True)
	st.info('En la pestaña "Ejercicio" te ponemos un ejemplo del consumo de caloría')
	st.subheader("Cómo te ayuda Fitástico")
	st.markdown('''Esta aplicación te marcará el consumo calórico diario en función del ejercicio 
		semanal que realices. <br>

		''',
		unsafe_allow_html=True)
	st.error('RECUERDA!!! el objetivo es cuidar el cuerpo para que te dure mucho :smile:')

	stc.iframe('https://i.pinimg.com/originals/86/55/06/8655061908ac22b563dec8914865b15d.gif',
	height=700, width=1000, scrolling=True)




if __name__ == '__main__':
	main()


