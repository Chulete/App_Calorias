# EN ESTA LIBRETA HAY QUE PONER LOS CÁLCULOS DE CALORÍAS NECESARIAS PARA EL OBJETIVO
# VALORAR QUE ES DISTINTO PARA HOMBRES QUE PARA MUJERES

import streamlit as st 
import streamlit.components.v1 as stc
import pandas as pd 
import base64


menu = ['Hombre', 'Mujer']
choice = st.sidebar.selectbox('Indica tu sexo', menu)

if (choice == 'Hombre'):

	st.subheader(f"Indica peso, altura y edad actual")

	# Variables:
	col1, col2, col3 = st.columns([1,1,1])
	with col1:
		peso = st.number_input(f"Peso en kg", step=0.5)
	with col2:
		altura = st.number_input(f"Estatura en cm", step=1)
	with col3:
		edad = st.number_input(f"Edad", step=1)

	peso_deseado = st.number_input(f"Indica cuál es el peso que te gustaría alcanzar", step=0.5)

		
	tmb = ((peso*10) + (6.25*altura) - (5*edad) + 5)
	
	weeks = abs((peso - peso_deseado) *2)

	st.subheader('Con estos datos calculamos que... ')
	st.markdown(f'''<div style="background-color: rgb(0, 139, 139); padding: 6px;">
		<h5 style="color:white"</h5>
		- Vas a necesitar {int(weeks)} semanas para alcanzar el peso objetivo. <br>
		- Tienes una Tasa Metabólica Basal (TMB) de {int(tmb)} calorías.
		<div>''',
    	unsafe_allow_html=True)


	st.subheader('Por el ejercicio que haces, la app piensa que...')


	menu_2 = ['Nada', '1 a 3 días', '3 a 5 días', '6 a 7 días']
	choice_2 = st.sidebar.selectbox('Cuánto ejercicio realizas a la semana', menu_2)

	if (choice_2 == 'Nada'):
		
		cal_1 = (tmb * 1.2)
		n_perder1 = (cal_1 -700)
		n_perder2 = (cal_1 - 500)
		n_ganar = (cal_1 + 500)

		st.markdown('''Te pareces a Krilin y cree que deberías esforzarte más en buscar tiempo para hacer deporte. <br>
			Deberás ser muy estricto con la dieta al no quemar calorías mediante el ejercicio. <br>
			El maestro Mutenroshi no está muy contento contigo.''',
			unsafe_allow_html=True)
		st.markdown(f'''<div style="background-color: rgb(0, 139, 139); padding: 7px;">
			<h7 style="color:white"</h5>
			En lo relativo al consumo calórico: <br>
			- Para mantener el peso actual debería consumir {int(cal_1)} calorías al día. <br>
			- Para perder peso debes consumir entre {int(n_perder1)} y {int(n_perder2)} calorías al día. <br>
			- Para aumentar de peso debes consumir más de {int(n_ganar)} al día.
			<div>''',
    		unsafe_allow_html=True)

		stc.iframe('https://i.pinimg.com/originals/79/04/f2/7904f27e38cb9cd5da4a5623bc33d6fd.jpg',
		height=700, width=500, scrolling=True)

	elif (choice_2 == '1 a 3 días'):
		cal_2 = (tmb * 1.375)
		a_perder1 = (cal_2 -700)
		a_perder2 = (cal_2 - 500)
		a_ganar = (cal_2 + 500)

		st.markdown('''Tienes tanto potencial como Goku de chiquitín pero tienes que esforzarte un poco más para explotar todo tu potencial. <br>
			''',
			unsafe_allow_html=True)
		st.markdown(f'''<div style="background-color: rgb(0, 139, 139); padding: 7px;">
			<h7 style="color:white"</h5>
			Con respecto al consumo de calorías diarias: <br>
			- Para mantener el peso actual debería consumir {int(cal_2)} calorías al día. <br>
			- Para perder peso debes consumir entre {int(a_perder1)} y {int(a_perder2)} calorías al día. <br>
			- Para aumentar de peso debes consumir más de {int(a_ganar)} al día.
			<div>''',
    		unsafe_allow_html=True)

		stc.iframe('https://i.pinimg.com/originals/b5/12/d4/b512d409fdc6119493f94e345671693b.gif',
		height=700, width=500, scrolling=True)

	elif (choice_2 == '3 a 5 días'):
		cal_3 = (tmb * 1.55)
		b_perder1 = (cal_3 -700)
		b_perder2 = (cal_3 - 500)
		b_ganar = (cal_3 + 500)

		st.markdown('''Tienes muy buena disciplina. <br>
			Goku estaría orgulloso de luchar a tu lado. <br>
			No te calientes la cabeza si no llevas el consumo de calorías a rajatabla... te has ganado saltarte la dieta cuando quieras. <br>
			''',
			unsafe_allow_html=True)

		st.markdown(f'''<div style="background-color: rgb(0, 139, 139); padding: 7px;">
			<h7 style="color:white"</h5>
			Con respecto a las calorías recomendadas:  <br>
			- Para mantener el peso actual debería consumir {int(cal_3)} calorías al día. <br>
			- Para perder peso debes consumir entre {int(b_perder1)} y {int(b_perder2)} calorías diarias. <br>
			- Para aumentar de peso debes consumir más de {int(b_ganar)} calorías.
			<div>''',
    		unsafe_allow_html=True)

		stc.iframe('https://gifdb.com/images/high/goku-thumbs-up-5r8q4qe80h4649ot.gif',
		height=700, width=1000, scrolling=True)

	elif (choice_2 == '6 a 7 días'):
		cal_3 = (tmb * 1.55)
		b_perder1 = (cal_3 -700)
		b_perder2 = (cal_3 - 500)
		b_ganar = (cal_3 + 500)

		st.markdown('''Hasta el Señor descanso el domingo... <br>
			Recuerda que el descanso es fundamental para que el cuerpo funcione al 100% de su potencial. <br>
			
			''',
			unsafe_allow_html=True)

		st.markdown(f'''<div style="background-color: rgb(0, 139, 139); padding: 7px;">
			<h7 style="color:white"</h5>
			Sobre el tema de las calorías: <br>
			- Para mantener el peso actual debería consumir {int(cal_3)} calorías al día. <br>
			- Para perder peso debes consumir entre {int(b_perder1)} y {int(b_perder2)} calorías diarias. <br>
			- Para aumentar de peso debes consumir más de {int(b_ganar)} calorías.
			<div>''',
    		unsafe_allow_html=True)

		stc.iframe('https://i.pinimg.com/originals/86/68/d9/8668d99b7fd5e3855ef8881b7000b98f.gif',
		height=700, width=1000, scrolling=True)

elif (choice == 'Mujer'):
	st.subheader('Indica peso, altura y edad actual')

	col1, col2, col3 = st.columns([1, 1, 1])
	with col1:
		peso_m = st.number_input(f'Peso en kg', step=0.5)
	with col2:
		altura_m = st.number_input(f'Estatura en cm', step=1)
	with col3:
		edad_m = st.number_input(f'Edad', step=1)

	peso_deseado_m = st.number_input(f'Indica cuál es el peso que te gustaría alcanzar', step=0.5)


	tmb_m = ((peso_m*10) + (6.25*altura_m) - (5*edad_m) - 161)

	weeks_m = abs((peso_m-peso_deseado_m) * 2)

	st.subheader('Con estos datos calculamos que... ')
	st.markdown(f'''<div style="background-color: rgb(0, 139, 139); padding: 6px;">
		<h5 style="color:white"</h5>
		- Vas a necesitar {int(weeks_m)} semanas para alcanzar el peso objetivo. <br>
		- Tienes una Tasa Metabólica Basal (TMB) de {int(tmb_m)} calorías.
		<div>''',
    	unsafe_allow_html=True)


	st.subheader('Por el ejercicio que haces, la app piensa que...')


	menu_2_m = ['Nada', '1 a 3 días', '3 a 5 días', '6 a 7 días']
	choice_2_m = st.sidebar.selectbox('Cuánto ejercicio realizas a la semana', menu_2_m)

	if (choice_2_m == 'Nada'):
		
		cal_1_m = (tmb_m * 1.2)
		n_perder1_m = (cal_1_m -700)
		n_perder2_m = (cal_1_m - 500)
		n_ganar_m = (cal_1_m + 500)

		st.markdown('''Te pareces al Power Ranger Rosa y cree que deberías esforzarte más en buscar tiempo para hacer deporte. <br>
			Deberás ser muy estricto con la dieta al no quemar calorías mediante el ejercicio. <br>
			El lider Zordon no está muy contento contigo.''',
			unsafe_allow_html=True)
		st.markdown(f'''<div style="background-color: rgb(0, 139, 139); padding: 7px;">
			<h7 style="color:white"</h5>
			En lo relativo al consumo calórico: <br>
			- Para mantener el peso actual debería consumir {int(cal_1_m)} calorías al día. <br>
			- Para perder peso debes consumir entre {int(n_perder1_m)} y {int(n_perder2_m)} calorías al día. <br>
			- Para aumentar de peso debes consumir más de {int(n_ganar_m)} al día.
			<div>''',
    		unsafe_allow_html=True)

		stc.iframe('https://i.makeagif.com/media/3-13-2018/fX010V.gif',
		height=700, width=500, scrolling=True)

	elif (choice_2_m == '1 a 3 días'):
		cal_2_m = (tmb_m * 1.375)
		a_perder1_m = (cal_2_m -700)
		a_perder2_m = (cal_2_m - 500)
		a_ganar_m = (cal_2_m + 500)

		st.markdown('''Tienes tanto potencial como las Súper Nenas pero tienes que esforzarte un poco más para explotar todo tu potencial. <br>
			''',
			unsafe_allow_html=True)
		st.markdown(f'''<div style="background-color: rgb(0, 139, 139); padding: 7px;">
			<h7 style="color:white"</h5>
			Con respecto al consumo de calorías diarias: <br>
			- Para mantener el peso actual debería consumir {int(cal_2_m)} calorías al día. <br>
			- Para perder peso debes consumir entre {int(a_perder1_m)} y {int(a_perder2_m)} calorías al día. <br>
			- Para aumentar de peso debes consumir más de {int(a_ganar_m)} al día.
			<div>''',
    		unsafe_allow_html=True)

		stc.iframe('https://i.gifer.com/1bev.gif',
		height=700, width=500, scrolling=True)

	elif (choice_2_m == '3 a 5 días'):
		cal_3_m = (tmb_m * 1.55)
		b_perder1_m = (cal_3_m -700)
		b_perder2_m = (cal_3_m - 500)
		b_ganar_m = (cal_3_m + 500)

		st.markdown('''Tienes muy buena disciplina. <br>
			Nick Fury o el mismísimo Tony Stark estarían orgullosos de tenerte en su equipo. <br>
			No te calientes la cabeza si no llevas el consumo de calorías a rajatabla... te has ganado saltarte la dieta cuando quieras. <br>
			''',
			unsafe_allow_html=True)

		st.markdown(f'''<div style="background-color: rgb(0, 139, 139); padding: 7px;">
			<h7 style="color:white"</h5>
			Con respecto a las calorías recomendadas:  <br>
			- Para mantener el peso actual debería consumir {int(cal_3_m)} calorías al día. <br>
			- Para perder peso debes consumir entre {int(b_perder1_m)} y {int(b_perder2_m)} calorías diarias. <br>
			- Para aumentar de peso debes consumir más de {int(b_ganar_m)} calorías.
			<div>''',
    		unsafe_allow_html=True)

		stc.iframe('https://media.tenor.com/vVwJ17m5qxEAAAAM/wonder-woman.gif',
		height=700, width=1000, scrolling=True)

	elif (choice_2_m == '6 a 7 días'):
		cal_3_m = (tmb_m * 1.55)
		b_perder1_m = (cal_3_m -700)
		b_perder2_m = (cal_3_m - 500)
		b_ganar_m = (cal_3_m + 500)

		st.markdown('''Hasta el Señor descanso el domingo... <br>
			Recuerda que el descanso es fundamental para que el cuerpo funcione al 100% de su potencial. <br>
			
			''',
			unsafe_allow_html=True)

		st.markdown(f'''<div style="background-color: rgb(0, 139, 139); padding: 7px;">
			<h7 style="color:white"</h5>
			Sobre el tema de las calorías: <br>
			- Para mantener el peso actual debería consumir {int(cal_3_m)} calorías al día. <br>
			- Para perder peso debes consumir entre {int(b_perder1_m)} y {int(b_perder2_m)} calorías diarias. <br>
			- Para aumentar de peso debes consumir más de {int(b_ganar_m)} calorías.
			<div>''',
    		unsafe_allow_html=True)

		stc.iframe('https://i.pinimg.com/originals/2f/d7/fa/2fd7fa8115100cbe13447bb9647bac69.gif',
		height=700, width=1000, scrolling=True)

















