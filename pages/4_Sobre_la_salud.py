# EXPLICACIÓN DEL MOTIVO DE QUERER ESTAR EN UN RANGO DE PESO

import streamlit as st
import streamlit.components.v1 as stc


st.header("Por qué lcanzar el peso deseado")
st.write("Tener un peso saludable es beneficioso para la salud en muchos aspectos. Razones clave:")
with st.expander("Prevención de enfermedades"):
	st.info("""Mantener un peso saludable reduce el riesgo de desarrollar diversas enfermedades crónicas, 
		como enfermedades cardíacas, diabetes tipo 2, hipertensión arterial 
		y ciertos tipos de cáncer. Estas enfermedades están relacionadas con el exceso de peso y la obesidad.
		""")
with st.expander("Funcionamiento óptimo del cuerpo"):
	st.info("""Un peso saludable contribuye al funcionamiento óptimo de los sistemas del cuerpo. 
		El exceso de peso puede poner una carga adicional en los órganos, las articulaciones y los músculos, 
		lo que puede llevar a problemas de salud a largo plazo.""")
with st.expander("Mejora de la salud mental"):
	st.info("""Mantener un peso saludable también está relacionado con la salud mental. 
		La autoimagen positiva y la confianza en uno mismo pueden estar vinculadas a mantener un peso dentro de 
		los rangos recomendados. Además, hay evidencia de que el ejercicio regular, que a menudo se asocia con 
		la gestión del peso, puede mejorar el estado de ánimo y reducir el estrés.""")

with st.expander("Mayor energía y vitalidad"):
	st.info("""Un peso saludable suele ir de la mano con un estilo de vida activo y una alimentación equilibrada. 
		Esto puede resultar en niveles de energía más altos y una sensación general de vitalidad. 
		Las personas con un peso saludable a menudo encuentran que tienen más resistencia física y pueden 
		participar en actividades diarias con mayor facilidad.""")

with st.expander("Mejora de la calidad del sueño"):
	st.info("""El mantenimiento de un peso saludable puede contribuir a mejorar la calidad del sueño. 
		La obesidad y el sobrepeso a menudo se asocian con trastornos del sueño como la apnea del sueño, 
		que pueden afectar negativamente la calidad del descanso.""")

with st.expander("Longevidad"):
	st.info("""Existe evidencia que sugiere que mantener un peso saludable está asociado con una mayor longevidad. 
		Las personas con un índice de masa corporal (IMC) dentro del rango saludable tienden a vivir más tiempo 
		que aquellas que tienen un IMC en los rangos de sobrepeso u obesidad.""")

menu = ['Recomendaciones', 'Tipos de ejercicio']
choice = st.selectbox('Recomendaciones de la OMS', menu)

if (choice ==  'Recomendaciones'):
	st.success('''Realiza al menos 150 minutos de actividad moderada a la semana,
	 75 minutos de actividad vigorosa o una combinación equivalente de ambas.''')
	st.error('''Realiza, al menos 2 días a la semana, actividades de fortalecimiento 
		muscular y mejora de la masa ósea y actividad para mejorar la flexibilidad.''')
	st.info('''Reduce los periodos sedentarios prolongados de más de 2 horas seguidas.
		Realiza descansos cada hora para hacer estiramientos o dar un breve paseo.''')
	st.warning('''Limita el tiempo delante de una pantalla. Cada cierto tiempo hay que descansar la vista. 
		Cada 20 minutos mira a lo lejos unos 20 segundos.''')

elif (choice=='Tipos de ejercicio'):
	st.info('''LEVE. Te permite hablar mientras lo prácticas.''')
	st.warning('''MODERADO. Aumenta la sensación de calor y se inicia una ligera sudoración pero aún se puede hablar.''')
	st.success('''VIGOROSO. La sensación de calor, el sudor es más fuerte y el ritmo cardiaco es más elevado, 
		por lo que es difícil hablar mientras se practica.''')




		




