# Sales-Prediction-using-Advertisement-Expenditure
📊 Sales Prediction using Advertisement Expenditure

This project predicts product sales based on advertising expenditure across TV, Radio, and Newspaper using Machine Learning (Linear and Ridge Regression).

The model is deployed as an interactive Streamlit web app where users can input ad budgets and instantly get sales predictions.

🚀 Features

Input advertising spend on TV, Radio, Newspaper

Predict expected sales in real-time

Built with Ridge Regression (regularized Linear Regression)

Deployed with Streamlit for easy access

🧑‍💻 Tech Stack

Python

Pandas, NumPy → Data handling

Scikit-learn → Ridge Regression model

Joblib → Model saving & loading

Streamlit → Web app deployment

Sales-Prediction-using-Advertisement-Expenditure/
│-- app.py               # Streamlit app
│-- sales_model.pkl      # Trained Ridge regression model
│-- requirements.txt     # Dependencies
│-- advertising_sales_data.csv  # Dataset (optional)
│-- README.md            # Project documentation


📊 Example Prediction

TV: 200

Radio: 40

Newspaper: 50

👉 Predicted Sales ≈ XX.XX units

🔮 Future Improvements

Add Lasso Regression for feature selection

Build a visual dashboard (feature importance, trend analysis)

Deploy using Docker + AWS/GCP for scalability