from dotenv import load_dotenv
load_dotenv()#load all the environment variable from .env

import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#Function to load gemini pro vision
model.genai.GenerativeModel('gemini-pro-vision')

def get_gemini_response(input,image,prompt):
    response=model.generate_content([input,image[0],prompt])
    return response.text


def input_image_details(uploaded_file):
    if uploaded_file is not None:
        bytrs_data=uploaded_file.getvalue()

        image_parts=[
            {
                "mime_type":uploaded_file.type,
                "data":bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")


#initiaize our streamlit app
st.set_page_config(page_title="Multilanguage Invoice Extractor")
input=st.text_input("Input Prompt",key="input")
uploaded_file=st.file_uploader("Choose an image of the invoice...",type=["jpeg","jpg","png"])
image=""
if uploaded_file is not None:
    image=Image.open(uploaded_file)
    image.thumbnail((300,300))
    st.image(image,caption="Upload Image.",use_column_width=True)

submit=st.button("Tell me about the invoice")

input_prompt="""
You are an expert in understanding invoices.we will upload a image as invoices and you will have to answer any question based on the uploaded invoices image
"""

#if submit button is clicked
if submit:
    image_data=input_image_details(uploaded_file)
    resonse = get_gemini_response(input_prompt,image_data,input)
    st.subheader("The Response is ")
    st.write(resonse)