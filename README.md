
# CV-Insight-Pro

**CV-Insight-Pro** is a web application that leverages AI to analyze resumes against job descriptions. By using advanced AI models, it provides insights into how well a resume matches a job description, offers suggestions for skill improvements, and evaluates the resume's compatibility with Applicant Tracking Systems (ATS).

## Features

- **Resume Analysis**: Evaluate how well a resume aligns with a given job description.
- **Skill Improvement**: Get personalized advice on enhancing skills based on the job description.
- **ATS Compatibility**: Check how well a resume matches with ATS systems and receive a percentage match score.
- **Text Extraction**: Extract and analyze text from PDF resumes.

## Technologies Used

- **Streamlit**: Framework for creating the web application.
- **Google Generative AI**: For generating insights and responses.
- **PyPDF2**: For extracting text from PDF files.
- **dotenv**: For managing environment variables.

## Installation

### Prerequisites

- Python 3.7 or higher
- `pip` (Python package installer)

### Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/CV-Insight-Pro.git
   cd CV-Insight-Pro
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**

   Create a `.env` file in the root directory of the project with the following content:

   ```
   GOOGLE_API_KEY=your_google_api_key
   ```

5. **Run the Application**

   ```bash
   streamlit run app.py
   ```

   The application will start and be available at `http://localhost:8501` by default.

## Usage

1. **Upload a Resume**: Click on the "Upload your CV in PDF format" button and select a PDF file.
2. **Enter Job Description**: Provide the job description in the text area.
3. **Select Analysis Type**: Choose from:
   - "Tell me about the resume"
   - "How Can I improve my skills"
   - "Percentage Match"
4. **Get Results**: Click the appropriate button to receive insights and suggestions based on your input.

## Project Structure

```
CV-Insight-Pro/
│
├── app1.py              # Main application file
├── requirements.txt    # Python dependencies
├── .env                # Environment variables
└── README.md           # Project documentation
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your improvements or bug fixes. For larger changes, please open an issue first to discuss.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or inquiries, please contact renukarajendrab@gmail.com).

---

