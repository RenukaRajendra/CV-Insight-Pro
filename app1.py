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

st.set_page_config(page_title="CV Insight Pro")
st.header("ATS Tracking System")
input_text = st.text_area("Job Description: ", key="input")
uploaded_file = st.file_uploader("Upload your CV in PDF format", type=["pdf"])

if uploaded_file is not None:
    st.write('PDF uploaded successfully')
submit1 = st.button("Tell me about the resume")
submit2 = st.button("How Can I improve my skills")
submit3 = st.button("Percentage Match")

input_prompt1 = """
    As an experienced HR professional with significant expertise in Data Science, Full Stack Web Development, Big Data Engineering, DevOps, and Data Analysis, your task is to conduct a thorough review of the provided resume in relation to the given job description. Evaluate the candidate’s qualifications, skills, and experiences to determine how well they align with the job requirements. Your analysis should cover the following aspects:

Relevance of Experience: Assess the candidate’s previous work experience and how it fits with the responsibilities outlined in the job description.
Technical Proficiency: Evaluate the technical skills and knowledge listed on the resume against the key skills required for the role.
Strengths and Weaknesses: Highlight the candidate’s strengths that align with the job requirements and identify any areas where their qualifications may fall short.
Overall Fit: Provide a summary of how well the candidate's profile matches the job description and suggest any areas for improvement or additional qualifications that could enhance their suitability for the role.
"""

input_prompt2 = """
    In your role as a Technical HR Manager with expertise in Data Science, Full Stack Web Development, Big Data Engineering, DevOps, and Data Analysis, you are tasked with a detailed examination of the resume relative to the provided job description. Your review should include:

Alignment with Job Requirements: Analyze how well the candidate’s skills, experiences, and qualifications match the key requirements of the job description.
Suitability for the Role: Provide insights on the candidate’s potential fit for the role from an HR perspective, considering factors such as cultural fit, teamwork capabilities, and potential for growth.
Skill Enhancement Recommendations: Offer detailed suggestions on how the candidate can improve their skills or experience to better align with the job requirements. This may include additional training, certifications, or practical experience.
Evaluation Summary: Summarize your findings and offer a clear recommendation on the candidate's suitability for the position, including any reservations or concerns.
"""

input_prompt3 = """
    As an expert in ATS (Applicant Tracking Systems) with deep knowledge in Data Science, Full Stack Web Development, Big Data Engineering, DevOps, and Data Analysis, your role is to evaluate the resume against the provided job description with a focus on ATS compatibility. Your assessment should include:

Match Percentage: Calculate the percentage indicating how closely the resume matches the job description. This percentage reflects how well the resume aligns with the job requirements based on key criteria.
Keyword Analysis: Identify any important keywords or phrases that are missing from the resume but are essential for the role. This helps in understanding how well the resume is optimized for ATS and the job description.
Strengths and Gaps: Provide a detailed analysis of the strengths demonstrated in the resume and any significant gaps or areas where the resume does not fully meet the job requirements.
Final Thoughts: Offer your overall evaluation and insights, including suggestions for improving the resume's alignment with the job description and enhancing its effectiveness in passing ATS screenings.
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
