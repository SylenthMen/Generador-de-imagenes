import streamlit as st
import openai
import requests
from io import BytesIO
from zipfile import ZipFile, ZIP_DEFLATED

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
        if num_images == 1:
            # Solo hay una imagen para descargar
            image_url = response['data'][0]['url']
            image_response = requests.get(image_url)
            if image_response.status_code == 200:
                bytes_io = BytesIO(image_response.content)
                st.image(image_url, caption="Imagen 1", use_column_width=True)
                st.download_button(
                    label="Descargar imagen",
                    data=bytes_io,
                    file_name="imagen.png",
                    mime="image/png"
                )
        else:
            # Hay varias imágenes para descargar, usar ZIP
            zip_buffer = BytesIO()
            with ZipFile(zip_buffer, 'a', ZIP_DEFLATED) as zip_file:
                for i, img in enumerate(response['data']):
                    image_url = img['url']
                    image_response = requests.get(image_url)
                    if image_response.status_code == 200:
                        image_name = f"imagen_{i+1}.png"
                        zip_file.writestr(image_name, image_response.content)
                        st.image(image_url, caption=f"Imagen {i+1}", use_column_width=True)
                
            zip_buffer.seek(0)
            st.download_button(
                label="Descargar todas las imágenes",
                data=zip_buffer,
                file_name="imagenes.zip",
                mime="application/zip"
            )
