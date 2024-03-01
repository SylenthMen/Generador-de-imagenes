# import streamlit as st
# #from dotenv import load_dotenv
# import os
# from openai import OpenAI
# client = OpenAI()
# #load_dotenv()


# OpenAI.api_key = st.secrets["OPENAI_API_KEY"]


# st.title("Generador de imagenes con DallE")

# st.write("Este es un generador de imagenes con DallE, una red neuronal que puede generar imagenes a partir de texto")

# with st.form("image_form"):
#     text = st.text_input("Para usarlo, escribe una frase que describa la imagen que quieres generar")
#     num_images = st.number_input("Numero de imagenes a generar", min_value=1, max_value=3, value=1)
#     image_size = st.selectbox("Tamaño de la imagen", ["256x256", "512x512", "1024x1024"], index=0)
#     submit_button = st.form_submit_button("Generar imagen")

# if submit_button:
#     st.write("Generando imagen...")
#     response = client.images.generate(
#         prompt=text,
#         n=num_images,
#         size=image_size
#     )
#     print(response)
#     for i in range(num_images):
#         url = response.data[i].url
#         st.image(url, caption=f"Imagen {i+1}", use_column_width=True)

import streamlit as st
import openai

# Configura la clave API de OpenAI
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.title("Generador de imágenes con DALL·E")

st.write("Este es un generador de imágenes con DALL·E, una red neuronal que puede generar imágenes a partir de texto")

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
    # Asumiendo que la respuesta contiene las URLs de las imágenes
    if response and 'data' in response:
        for i, img in enumerate(response['data']):
            st.image(img['url'], caption=f"Imagen {i+1}", use_column_width=True)
