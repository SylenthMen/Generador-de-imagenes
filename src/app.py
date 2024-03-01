# import streamlit as st
# import openai

# # Configura la clave API de OpenAI
# openai.api_key = st.secrets["OPENAI_API_KEY"]

# st.title("Generador de imágenes con IA")

# st.write("Este es un generador de imágenes con IA, una red neuronal que puede generar imágenes a partir de texto")

# with st.form("image_form"):
#     text = st.text_input("Para usarlo, escribe una frase que describa la imagen que quieres generar")
#     num_images = st.number_input("Número de imágenes a generar", min_value=1, max_value=3, value=1)
#     image_size = st.selectbox("Tamaño de la imagen", ["256x256", "512x512", "1024x1024"], index=0)
#     submit_button = st.form_submit_button("Generar imagen")

# if submit_button:
#     st.write("Generando imagen...")
#     response = openai.Image.create(
#         prompt=text,
#         n=num_images,
#         size=image_size
#     )
#     # Asumiendo que la respuesta contiene las URLs de las imágenes
#     if response and 'data' in response:
#         for i, img in enumerate(response['data']):
#             st.image(img['url'], caption=f"Imagen {i+1}", use_column_width=True)

import streamlit as st
import openai
import requests
from io import BytesIO

# Configura la clave API de OpenAI
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.title("Generador de imágenes con IA")

st.write("Este es un generador de imágenes con IA, una red neuronal que puede generar imágenes a partir de texto")

with st.form("image_form"):
    text = st.text_input("Para usarlo, escribe una frase que describa la imagen que quieres generar")
    num_images = st.number_input("Número de imágenes a generar", min_value=1, max_value=3, value=1)
    image_size = st.selectbox("Tamaño de la imagen", ["256x256", "512x512", "1024x1024"], index=0)
    submit_button = st.form_submit_button("Generar imagen")

if submit_button:
    st.write("Generando imagen...")
    response = openai.Image.create(
        prompt=text,
        n=num_images,
        size=image_size
    )
    if response and 'data' in response:
        for i, img in enumerate(response['data']):
            # Descarga la imagen
            image_url = img['url']
            response = requests.get(image_url)
            if response.status_code == 200:
                # Crea un buffer de bytes para la imagen
                bytes_io = BytesIO(response.content)
                # Muestra la imagen
                st.image(image_url, caption=f"Imagen {i+1}", use_column_width=True)
                # Agrega el botón de descarga
                st.download_button(
                    label="Descargar imagen",
                    data=bytes_io,
                    file_name=f"imagen_{i+1}.png",
                    mime="image/png"
                )
