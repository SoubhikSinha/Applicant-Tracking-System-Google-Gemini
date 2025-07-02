from dotenv import load_dotenv

load_dotenv()

# Importing necessay libraries
import streamlit as st
import os
from PIL import Image
import pdf2image
import google.generativeai as genai
import io
import base64

genai.configure(
    api_key = os.getenv("GOOGLE_API_KEY") # Loading the Google Gemini API key 
)

# Obtaining Gemini Response
def get_gemini_response(input, pdf_content, prompt):
    model = genai.GenerativeModel('gemini-2.0-flash') # Loading the model
    
    # Combining inputs into a single structured input
    combined_input = f"{prompt}\n\nJob Description:\n{input_text}\n\nResume Details:\n{pdf_content[0]}"
    
    response = model.generate_content(combined_input) # Getting response
    return response.text

# Setting up the PDF file for the LLM model
def input_pdf_setup(uploaded_file):
    '''
    Converting the PDF file into image
    '''
    if uploaded_file is not None:
        images = pdf2image.convert_from_bytes(uploaded_file.read()) # converting the file (read) - from bytes to Image
        
        first_page = images[0]

        # Converting into bytes
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format = 'JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts = [
            {
                "mime_type" : "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode() # Encoding to base64
            }
        ]

        return pdf_parts
    else:
        raise FileNotFoundError("No File Uploaded")

# Streamlit Application
st.set_page_config(page_title = "ATS Resume Expert")
st.header("ATS Trackig System - powered by Google Gemini")
input_text = st.text_area("Job Description : ", key = "input")
uploaded_file = st.file_uploader("Upload Your Resume (PDF)", type = ['pdf'])

if uploaded_file is not None:
    st.write("PDF Uploaded Successfully")

# Creating Functionalities
submit1 = st.button("Tell me about the Resume")
submit2 = st.button("Percentage Match")


input_prompt1 = """
You are an experienced HR professional specializing in one of the following domains: Data Science, Full Stack Development, Web Development, Big Data Engineering, DevOps, or Data Analysis. Your task is to critically evaluate the provided resume against the given job description for the relevant role.

Assess the candidate's qualifications, skills, and experience in relation to the job requirements. Provide a structured analysis, highlighting key strengths that align well with the role and identifying any gaps or weaknesses that could affect their suitability. Where applicable, suggest areas for improvement to enhance the candidate's chances of success in the job application process.
"""

input_prompt2 = """
You are an advanced Applicant Tracking System (ATS) scanner with deep expertise in one of the following fields: Data Science, Full Stack Development, Web Development, Big Data Engineering, DevOps, or Data Analysis, along with a strong understanding of ATS functionality and keyword-based resume screening. Your task is to evaluate the provided resume against the given job description and determine the percentage match based on skills, experience, and relevant keywords. The output should first display the match percentage, followed by a list of missing keywords, and conclude with final thoughts providing a brief professional assessment of the candidate’s suitability, highlighting strengths and areas for improvement.
"""

if submit1:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt1, pdf_content, input_text)
        st.subheader("The response is : ")
        st.write(response)
    else:
        st.write("Please upload your Resume")

elif submit2:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt2, pdf_content, input_text)
        st.subheader("The response is : ")
        st.write(response)
    else:
        st.write("Please upload your Resume")

