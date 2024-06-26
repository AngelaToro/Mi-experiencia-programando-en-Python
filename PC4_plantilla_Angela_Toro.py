# Este código sirve para instalar Streamlit en tu computadora y hacer un primer programa en Streamlit.
# Pero se ejecuta en la terminal de tu computadora, no en Jupyter Notebook.
# pip install Streamlit

# Este código sirve para acceder una página web en tu navegador que te brinda información sobre Streamlit.
# Pero se ejecuta en la terminal Python de tu computadora, no en Jupyter Notebook.
# streamlit hello

# Antes de ejecutar un script de Python en Streamlit debes definir la carpeta donde se encuentra tus archivos
# cd ruta_de_tu_carpeta

# Este comando sirve para ejecutar un script de Python en Streamlit.
# Pero se ejecuta en la terminal de tu computadora, no en Jupyter Notebook.
# OJO: Debes antes tener instalado Streamlit en tu computadora, debes antes definir la ruta de tus archivos y 
##     tener un script de Python (your_script.py) que quieras ejecutar en Streamlit.
#  streamlit run your_script.py

# Este código sirve para hacer un primer programa en Streamlit.
import streamlit as st

# Creamos una barra lateral
sidebar = st.sidebar

# Si usas el siguiente código mostrará un título en la aplicación Streamlit. 
# st.title("Nombre de tu blog"): Esta línea está creando un título en la aplicación web.
# Pero, a diferencia de st.markdown, el texto estará alineado a la izquierda y no podrás cambiar el color del texto.

# La función st.markdown permite centrar y agrandar la letra del título de la web en Streamlit.
st.markdown("<h1 style='text-align: center;'>Mi experiencia como desarrollera en programación</h1>", unsafe_allow_html=True)

# <h1 style='text-align: center;'>Nombre de tu blog</h1>: Esto es una cadena de código HTML. 
# La etiqueta <h1> se utiliza para el encabezado principal de una página web, y 
# el atributo style se utiliza para agregar estilos CSS. 
# En este caso, el texto está alineado al centro (text-align: center;). 
# El texto dentro de las etiquetas <h1> ("Aquí escribe un nombre creativo para tu blog") es el contenido del encabezado.

# unsafe_allow_html=True: Este es un argumento opcional en la función markdown. 
# Por defecto, streamlit no permite HTML en el texto de Markdown por razones de seguridad. 
# Sin embargo, establecer unsafe_allow_html en True permite el uso de HTML.

# Creamos dos columnas separadas para la imagen y el texto
col1, col2 = st.columns(2)

# col1, col2 = st.columns(2): Esta línea está creando dos columnas en la interfaz de usuario de la aplicación web. 
# La función st.columns toma un número entero como argumento que especifica el número de columnas que se deben crear. 
# Las columnas creadas se asignan a las variables col1 y col2.

# En la primera columna colocamos la imagen
col1.image("fotoange.png", caption='Esta soy yo ☘️', width=300, unsafe_allow_html=True)

# col1.image("ellie.png", caption='Ellie', width=300): Esta línea está colocando una imagen en la primera columna (col1). 
# La función image toma como primer argumento la ruta de la imagen que se va a mostrar. 
# En este caso, la imagen es "ellie.png". 
# El argumento caption se utiliza para proporcionar un pie de foto a la imagen, en este caso 'Ellie'. 
# El argumento width se utiliza para especificar el ancho de la imagen, en este caso 300 píxeles.

# En la segunda columna colocamos el texto: Debe contener una presentación de ustedes
# Deben presentarse: ¿Quién eres?, ¿De dónde eres?, ¿Qué estudias?, ¿Qué te gusta de tu carrera?, 
# ¿Qué te gustaría hacer en el futuro?, ¿Qué te gusta hacer en tu tiempo libre?

texto = """
Hola! Me llamo Ángela, tengo 21 años y estudio Comunicación para el Desarrollo en la PUCP :D. Si le preguntaran a mi yo de hace hace algunos años que estaba a punto de terminar el colegio qué se veía haciendo a los 21 años, probablemente mi respuesta hubiera sido que algo muy diferente a las comunicaciones. Pero...¿quién tiene su futuro resuelto a los 16 años? En mi paso por la universidad, me di cuenta que poco a poco eso que creía saber sobre el rumbo de mi vida iba cambiando, cambiando para bien. Y aunque en su momento, todas estas dudas vocacionales fueron todo un reto y la idea de cambiarme de carrera me parecía tan emocionante como aterradora, hoy me alegra mucho haberme atrevido a escuchar mi intuición. Este es mi segundo año de facultad, y me gusta mucho lo que voy aprendiendo. En comunica vemos de todo un poco, aprendemos a manejar las cámaras, a analizar películas, a crear campañas, a observar con atención nuestra realidad y a comprender otras miradas. A inicios de este año, me dieron la noticia de que habían actualizado los planes de estudios en nuestra facultad. Yo estaba muy emocionada por saber cuáles serían estos cambios, pero a la vez, algo angustiada por cómo estos pudieran afectar mi paso por la universidad. Cuando finalmente pude ver de qué se trataba, me di cuenta que este 2024-1 tendría que llevar un nuevo curso llamado Pensamiento Computacional. Sin la menor idea de a qué me estaba metiendo salvo la certeza de que este sería un ciclo más visitando las salas de computo del z, me inscribí al curso, y así comenzó mi experiencia :)
"""

# Las comillas triples (""") en Python se utilizan para definir cadenas multilínea.
# Mostramos el texto
col2.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto}</div>", unsafe_allow_html=True)

# <div style='text-align: justify; font-size: 15px;'>{texto}</div>: Esta es una cadena de código HTML. 
# La etiqueta <div> se utiliza para agrupar contenido en HTML. 
# En este caso, el texto está justificado (text-align: justify;). 
# El tamaño de la fuente se establece en 15 píxeles (font-size: 15px;).
# El texto dentro de las etiquetas <div> es la variable texto.

# f"": Esta es una cadena de formato en Python. 
# Permite la interpolación de variables, lo que significa que puedes insertar el valor de una variable directamente en la cadena. 
# En este caso, {texto} se reemplaza por el valor de la variable texto.


# Debajo de las columnas colocamos un subtítulo que describa tu experiencia aprendiendo a programar
# Deben presentar tu experiencia aprendiendo a programar: ¿Cómo te sentiste al principio?, 
# ¿Qué te ha enseñado la programación?, ¿Qué te gusta de programar?, 
# ¿Qué te gustaría hacer con la programación en el futuro? 

# Agregamos un subtítulo
st.markdown("<h2 style='text-align: center;'>Mi experiencia aprendiendo a programar 💻</h2>", unsafe_allow_html=True)

# <h2 style='text-align: center;'>Mi experiencia aprendiendo a programar 💻</h2>: Esta es una cadena de código HTML.
# La etiqueta <h2> se utiliza para el encabezado secundario de una página web.
# El texto está centrado (text-align: center;).
# El texto dentro de las etiquetas <h2> ("Mi experiencia aprendiendo a programar 💻") es el contenido del encabezado
# unsafe_allow_html=True: Este es un argumento opcional en la función markdown.
# Por defecto, streamlit no permite HTML en el texto de Markdown por razones de seguridad.
# Sin embargo, establecer unsafe_allow_html en True permite el uso de HTML.
# Puedes agregar emojis en el texto de Markdown utilizando códigos de emoji.

# Agregar un  texto para la respuesta
texto_2 = """
Mi experiencia aprendiendo a programar en Python ha sido una montaña rusa. Antes de iniciar el curso tenía muchas dudas sobre los contenidos, sobre la complejidad de los temas...estaba segura de la programación no era lo mío pero también estaba decidida a no dejarme intimidar por esas largas cadenas de texto antes de comenzar. Un martes, comenzamos con un print('Hola Mundo') y de repente todas esas dudas se hicieron más pequeñas. Me gustó mucho aprender sobre las funciones, los bucles y el manejo de datos, habían temas que me resultaban más sencillos y divertidos, y habían otros que me dejaban pensando por horas. Pero lo que más me gustó fue la manera en que íbamos construyendo los algoritmos, ordenando cada tarea paso a paso para que pueda cumplir su función. Creo que ejercitar este tipo de pensamiento es muy mportante para nosotros como comunicadores, porque observamos cada parte del proceso, desglozando un objetivo grande en pequeñas partes que finalmente contribuyen a lograr el producto final. 
"""

# Mostramos el texto
st.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto_2}</div>", unsafe_allow_html=True)

# <div style='text-align: justify; font-size: 15px;'>{texto_2}</div>: Esta es una cadena de código HTML.
# La etiqueta <div> se utiliza para agrupar contenido en HTML.
# En este caso, el texto está justificado (text-align: justify;).
# El tamaño de la fuente se establece en 15 píxeles (font-size: 15px;).
# El texto dentro de las etiquetas <div> es la variable texto_2.
# f"": Esta es una cadena de formato en Python.
# Permite la interpolación de variables, lo que significa que puedes insertar el valor de una variable directamente en la cadena.
# En este caso, {texto_2} se reemplaza por el valor de la variable texto_2.

# Agregamos un subtítulo en la barra lateral
sidebar.markdown("<h1 style='text-align: center;'>Gráficos que elaboramos en clase</h1>", unsafe_allow_html=True)

# <h1 style='text-align: center;'>Los análisis de Ellie</h1>: Esta es una cadena de código HTML.
# La etiqueta <h1> se utiliza para el encabezado principal de una página web.
# El texto está centrado (text-align: center;).
# El texto dentro de las etiquetas <h1> ("Los análisis de Ellie") es el contenido del encabezado.

# Creamos una lista de gráficos
graficos = ['Mapa de Peliculas', 'Gráfico de Tarjetas Amarillas', 'Gráfico de Tarjetas Rojas', 'Histograma de Strasbourg', 'Gráfico de Familias', 'Mapa de Familias lingüísticas']

# Creamos un cuadro de selección en la barra lateral
grafico_seleccionado = sidebar.selectbox('Selecciona un gráfico', graficos)
# El cuadro de selección se crea con la función selectbox.
# El primer argumento es el texto que se muestra en el cuadro de selección.
# El segundo argumento es una lista de opciones que se pueden seleccionar.
# En este caso, las opciones son los elementos de la lista graficos.
# La opción seleccionada se asigna a la variable grafico_seleccionado.
# La variable grafico_seleccionado se utiliza para mostrar el gráfico correspondiente en la aplicación web.
# La función selectbox se utiliza para crear un cuadro de selección en la barra lateral.

# Mostramos el gráfico seleccionado
if grafico_seleccionado == 'Mapa de películas':
    sidebar.markdown("<div style='text-align: justify; font-size: 20px;'>Este primer gráfico, es un mapa en el que se observan los lugares donde se grabaron mis 5 películas favoritas</div>", unsafe_allow_html=True)
    sidebar.image("mapa_pelis.png", caption='Mapa de películas', width=500)
    pass
elif grafico_seleccionado == 'Gráfico de Tarjetas Amarillas':
    sidebar.markdown("<div style='text-align: justify'>Este gráfico muestra el promedio de tarjetas amarillas recibidas como equipo local de los equipos de la Liga Francesa durante la temporada 2022-2023.</div>", unsafe_allow_html=True)
    sidebar.image("barras_tarjeta_amarilla.png", caption='Gráfico de Tarjetas Amarillas', width=500)
    pass
elif grafico_seleccionado == 'Gráfico de Tarjetas Rojas':
    sidebar.markdown("<div style='text-align: justify'>Este gráfico muestra el promedio de tarjetas rojas recibidas como equipo visitante de los equipos de la Liga Francesa durante la temporada 2022-2023.</div>", unsafe_allow_html=True)
    sidebar.image("barras_tarjeta_rojas.png", caption='Gráfico de Tarjetas Rojas', width=500)
    pass
elif grafico_seleccionado == 'Histograma de Strasbourg':
    sidebar.markdown("<div style='text-align: justify'>Este gráfico muestra los goles anotados por el equipo Strasbourg como equipo local y como equipo visitante durante la temporada 2022-2023.</div>", unsafe_allow_html=True)
    sidebar.image("histograma_strasbourg.png", caption='Histograma de Strasbourg', width=500)
    pass
elif grafico_seleccionado == 'Gráfico de Familias':
    sidebar.markdown("<div style='text-align: justify'>Este gráfico se hizo a partir de una base de datos sobre lenguas sudamericanas y muestra la cantidad de lenguas por familias linguística dentro.</div>", unsafe_allow_html=True)
    sidebar.image("barras_horizontales_familia.png", caption='Gráfico de Familias', width=500)
    pass
elif grafico_seleccionado == 'Mapa de Familias Linguísticas':
    sidebar.markdown("<div style='text-align: justify'>Por último, este gráfico es un mapa de Sudamérica que ubica los puntos geográficos del Quechuan, una familia linguística sudamericana.</div>", unsafe_allow_html=True)
    sidebar.image("mapa_familia_linguistica.png", caption='Mapa de Familias Linguísticas', width=500)
    pass

# if grafico_seleccionado == 'Gráfico de Macroareas':: Esta línea verifica si la opción seleccionada es 'Gráfico de Macroareas'.
# Si es así, se ejecuta el código dentro del bloque if.
# En este caso, se muestra un texto y una imagen correspondientes al gráfico de Macroareas.
# El texto y la imagen se muestran en la barra lateral.
# La función markdown se utiliza para mostrar el texto en la barra lateral.
# La función image se utiliza para mostrar la imagen en la barra lateral.
# El argumento caption se utiliza para proporcionar un pie de foto a la imagen.
# El argumento width se utiliza para especificar el ancho de la imagen.
# La palabra clave pass se utiliza para indicar que no se debe hacer nada en caso de que la opción seleccionada no sea 'Gráfico de Macroareas'.
