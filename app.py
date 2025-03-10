import streamlit as st
import requests
from PIL import Image
from io import BytesIO
from dotenv import load_dotenv
import os

load_dotenv()

st.title('Welcome to Pixel Mind')
st.write('This is a simple web app that uses the Stable Diffusion API to generate image based on a prompt you provide.')

# API details
API_URL = os.getenv("API_URL")
API_KEY = os.getenv("API_KEY")
HEADERS = {"Authorization": f"Bearer {API_KEY}"}

# Function to generate image from prompt
def generate_image(prompt):
    payload = {"inputs": prompt}
    response = requests.post(API_URL, headers=HEADERS, json=payload)
    
    if response.status_code == 200:
        return Image.open(BytesIO(response.content))
    else:
        st.error(f"Error: {response.status_code}")
        return None

# Streamlit UI
prompt = st.text_input("Enter a prompt", "A beautiful sunset over the mountains")

if st.button("Generate Image") and prompt:
    st.write("Generating image...")
    image = generate_image(prompt)
    if image:
        st.image(image, caption="Generated Image", use_column_width=True)