# Applicant Tracking System (ATS) — Powered by Google Gemini

## Acknowledgement
I extend my sincere gratitude to **[Krish Naik](https://github.com/krishnaik06)** for his exceptional educational resources and mentorship. His content was instrumental in conceptualizing and implementing this project.

<br>

## Project Overview
This project showcases a cutting-edge **AI-powered Applicant Tracking System (ATS)** that leverages **Google Gemini** and **Streamlit** to evaluate resumes against specific job descriptions. It offers a real-time, automated assessment pipeline that delivers actionable feedback for job seekers and hiring professionals alike.

<br>

## Key Technologies
**Google Gemini** : Utilized as the core **large language model** for semantic analysis, comparison, and recommendation, enabling deep contextual understanding of resumes and job descriptions.
<br>
**Streamlit** : Provides a sleek, responsive web interface allowing users to seamlessly upload documents and interact with the system in real-time.

<br>

## Features
### **"Tell Me About the Resume"**

-   The LLM evaluates the uploaded resume and provides a structured analysis.
    
-   Suggests actionable edits to better align the resume with the job description.
    
-   Identifies skill gaps and content mismatches.
    

### **Percentage Match Score**

-   Computes a similarity score indicating how well the resume matches the job description.
    
-   Offers an objective metric for resume-job fit analysis.

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
