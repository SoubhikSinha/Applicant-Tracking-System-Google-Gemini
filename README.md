# Applicant Tracking System (ATS) -  Google Gemini

## Acknowledgement
I would like to extend my sincere thanks to  **[Krish Naik](https://github.com/krishnaik06)**  for his invaluable content and guidance, which helped me build this project. This project wouldn't have been possible without his educational resources.

<br>

## About the Project

This project demonstrates the integration of **[Google Gemini](https://aistudio.google.com/prompts/new_chat)** and an **[Application Tracking System (ATS)](https://www.jobscan.co/blog/8-things-you-need-to-know-about-applicant-tracking-systems/)** to analyze resumes against job descriptions. The application is deployed on **[Streamlit](https://streamlit.io/)** and allows users to upload their resume and a job description for analysis.

### Features :

1.  **Tell Me About the Resume**
    
    -   The LLM model assesses the user's resume and compares it to the provided job description.
    -   It suggests modifications or improvements to align the resume better with the job requirements.
2.  **Percentage Match**
    
    -   The model provides a **percentage match score** indicating how well the resume aligns with the job description.

<br>

## How to Run the Project ?

(NOTE : This project was carried out on a  [Macintosh](https://www.apple.com/mac/)  machine)

### **1. Clone the Repository**
Clone the repository to your local machine :
```bash
git clone https://github.com/SoubhikSinha/Applicant-Tracking-System-Google-Gemini.git
```

<br>

### **2. Create a Virtual Environment**
Navigate to the repository's root directory and create a Conda virtual environment :
```bash
conda create -p ./venv python=3.11 -y
```

<br>

### **3. Activate the Conda Environment**
Activate the newly created environment :
```bash
conda activate venv/
```

<br>

### **4. Install Required Libraries**
Install all the necessary dependencies :
```bash
pip install -r requirements.txt
```

<br>

### **5. Set Up Google API Key**
Create and paste your Google API key inside  `.env`  file. Get your API key from  [Google AI Studio](https://aistudio.google.com/app/apikey).

Example  `.env`  file content :
```bash
GOOGLE_API_KEY="your_api_key_here"
```

<br>

### **6. Run the Application**
Start the Streamlit application by running :
```bash
streamlit run app.py
```

<br>

### **7. Upload and Analyze**
-   Upload your resume and the job description.
-   Explore the application's insights and resume-matching features.
