# Fraud Detection in OTT Platforms

## Team Members
- Akshita Sharma (2301730278)
- Aruhi Choudhary (2301730247)
- Chhavi Arora (2301730253)
- Aarushi (2301730216)

## Project Description
This project presents a machine learning-based solution for detecting fraud in OTT streaming platforms. The system identifies suspicious activities like account sharing, credential stuffing, content piracy, and payment fraud by analyzing user behavior, login data, and streaming patterns. A web-based interface built using Streamlit allows real-time predictions of fraudulent activity based on user inputs.

## Video Explanation
[Watch the video explanation here](https://drive.google.com/file/d/1YIrYrLoetC7tq7Z6VLddtSEionvF9fAf/view?usp=drivesdk)

## Technologies Used
- Python 3.x
- Google Colaboratory (Colab)
- Streamlit (for web dashboard)
- Scikit-learn (for ML model)
- Pandas, NumPy (for data handling)
- Matplotlib, Seaborn (for visualizations)
- Joblib (for model persistence)

## Steps to Run/Execute the Project

### If you're using Google Colab:
1. Open the Colab notebook: [Colab Link](https://colab.research.google.com/drive/11cm74HZREX1KnWqY2bN5nISM1J1588Cn?usp=sharing)
2. Upload the dataset (`dataset.csv`) and run each cell sequentially to preprocess, train, and evaluate the model.

### To run the Streamlit app locally:
1. Make sure Python is installed on your machine.
2. Install required libraries:
   ```
   pip install streamlit pandas joblib
   ```
3. Place the following files in the same folder:
   - `FDA.py` (your main Streamlit script)
   - `best_rf_model.pkl` (your trained model file)
4. Run the app:
   ```
   streamlit run FDA.py
   ```

### Output:
- The dashboard will allow you to input flow data and get real-time fraud detection results with visual indicators.

## Notes
- Fraud labels are inferred based on user group consumption types.
- The model currently uses Logistic Regression; future upgrades may include advanced classifiers or ensemble techniques.

## Project Report
A detailed project report explaining methodology, data sources, and results is available in the repository as a PDF.
