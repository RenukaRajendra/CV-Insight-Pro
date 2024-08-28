import base64
import io
from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
from PIL import Image
from PyPDF2 import PdfReader
import google.generativeai as genai

def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        pdf_reader = PdfReader(uploaded_file)
        # Extract text from the first page
        first_page_text = pdf_reader.pages[0].extract_text()
        return first_page_text
    else:
        raise FileNotFoundError("No File Uploaded")


def get_gemini_response(input, pdf_content, prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([input, pdf_content, prompt])
    return response.text

st.set_page_config(page_title="ATS Resume Expert")
st.header("ATS Tracking System")
input_text = st.text_area("Job Description: ", key="input")
uploaded_file = st.file_uploader("Upload your CV in PDF format", type=["pdf"])

if uploaded_file is not None:
    st.write('PDF uploaded successfully')
submit1 = st.button("Tell me about the resume")
submit2 = st.button("How Can I improve my skills")
submit3 = st.button("Percentage Match")

input_prompt1 = """
    You are an experienced HR with tech experience in the field of Data Science, Full Stack Web Development,
    Big Data Engineering, DevOps, Data Analysis. Your task is to review the provided resume against the job
    description for these profiles. Please share your professional evaluation on whether the candidate's profile
    aligns with the job description or not. Highlight the strengths and weaknesses of the applicant in relation to
    the job description.
"""

input_prompt2 = """
    You are a Technical HR manager with expertise in Data Science, Full Stack Web Development,
    Big Data Engineering, DevOps, Data Analysis. Your role is to scrutinize the resume in light of the job
    description provided. Share your insights on the candidate's suitability for the role from an HR perspective,
    and additionally, provide detailed advice on enhancing the skills for the shortlist.
"""

input_prompt3 = """
    You are a skilled ATS (Application Tracking System) scanner with a deep understanding of Data Science, Full Stack Web Development,
    Big Data Engineering, DevOps, Data Analysis, and ATS functionality. Your task is to evaluate the resume against the provided
    job description. Give the percentage of match if the resume matches the job description. First, the output should come as a percentage,
    then keywords missing, and lastly final thoughts.
"""

if submit1:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt1, pdf_content, input_text)
        st.subheader('The response is ')
        st.write(response)
    else:
        st.write("Please upload the resume")
elif submit2:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt2, pdf_content, input_text)
        st.subheader('The response is ')
        st.write(response)
    else:
        st.write("Please upload the resume")
elif submit3:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt3, pdf_content, input_text)
        st.subheader('The response is ')
        st.write(response)
    else:
        st.write("Please upload the resume")
