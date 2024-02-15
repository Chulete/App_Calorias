import streamlit as st
import streamlit.components.v1 as stc
import pandas as pd 
import base64

st.subheader('Calorías consumidas en función del ejercicio')

menu = ['Caminar', 'Correr', 'Nadar', 'Bicicleta']
choice = st.selectbox('Selecciona el deporte', menu)

if (choice == 'Caminar'):
	walk_met_1 = 3
	walk_met_2 = 4

	col1, col2 = st.columns([1, 1])
	with col1:
		peso = st.number_input(f'Peso en kg')
	with col2:
		tiempo = st.number_input(f'Tiempo en minutos', step=1)


	cal_min_walk = (walk_met_1*peso*(tiempo/60))
	cal_max_walk = (walk_met_2*peso*(tiempo/60))


	st.write('Dependiendo de la intensidad:')
	st.info(f'Has consumido entre {cal_min_walk} y {cal_max_walk} calorías')

elif (choice == 'Correr'):
	run_met_1 = 7
	run_met_2 = 12

	col1, col2 = st.columns([1, 1])
	with col1:
		peso = st.number_input(f'Peso en kg')
	with col2:
		tiempo = st.number_input(f'Tiempo en minutos', step=1)


	cal_min_run = (run_met_1*peso*(tiempo/60))
	cal_max_run = (run_met_2*peso*(tiempo/60))

	st.write('Dependiendo de la intensidad:')
	st.info(f'Has consumido entre {cal_min_run} y {cal_max_run} calorías')

elif (choice == 'Nadar'):
	swim_met_1 = 5
	swim_met_2 = 10

	col1, col2 = st.columns([1, 1])
	with col1:
		peso = st.number_input(f'Peso en kg')
	with col2:
		tiempo = st.number_input(f'Tiempo en minutos', step=1)


	cal_min_swin = (swim_met_1*peso*(tiempo/60))
	cal_max_swim = (swim_met_2*peso*(tiempo/60))

	st.write('Dependiendo de la intensidad:')
	st.info(f'Has consumido entre {cal_min_swin} y {cal_max_swim} calorías')

elif (choice == 'Bicicleta'):
	bicicle_met_1 = 5
	bicicle_met_2 = 10

	col1, col2 = st.columns([1, 1])
	with col1:
		peso = st.number_input(f'Peso en kg')
	with col2:
		tiempo = st.number_input(f'Tiempo en minutos', step=1)


	cal_min_bicicle = (bicicle_met_1*peso*(tiempo/60))
	cal_max_bicicle = (bicicle_met_2*peso*(tiempo/60))

	st.write('Dependiendo de la intensidad:')
	st.info(f'Has consumido entre {cal_min_bicicle} y {cal_max_bicicle} calorías')