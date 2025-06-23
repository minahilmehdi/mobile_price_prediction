# mobile_price_prediction
Overview:
This project uses supervised machine learning algorithms to predict the price range of mobile phones based on key features like RAM, battery power, camera specs, and more. It was developed as part of the NAVTTC MLOps course and deployed using Streamlit for live interaction.

🚀 Features:
Predicts mobile price range (0–3) using multiple classification algorithms

Includes trained models:

Logistic Regression

Decision Tree

Random Forest

Naive Bayes

Support Vector Machine

K-Nearest Neighbors

Live model version liveModelV1.pkl used in the deployed app

User-friendly Streamlit web app

🛠️ Tech Stack:
Python

Pandas, NumPy, Scikit-learn

Streamlit

Pickle (for model saving)

MLflow (optional)

Git/GitHub

📁 Project Structure:
bash
Copy
Edit
├── mobile_price_range_data.csv        # Dataset
├── streamlitapp.py                    # Streamlit frontend
├── *.pkl                              # Trained model files
├── requirements.txt                   # Dependencies
└── README.md                          # Project documentation
📊 Dataset:
The dataset includes features like:

Battery Power

RAM

Mobile Weight

Camera Specs

Number of Cores

Internal Memory
→ Each sample is labeled with a price range:
0 (Low), 1 (Medium), 2 (High), 3 (Very High)

🎯 Goal:
To demonstrate the practical deployment of ML models using MLOps techniques and provide a quick, efficient mobile price predictor for tech vendors and enthusiasts.

🔗 How to Run:
Clone the repo

Install dependencies

nginx
Copy
Edit
pip install -r requirements.txt
Run the app

arduino
Copy
Edit
streamlit run streamlitapp.py
🤝 Contribution:
This project was built by Minahil Mehdi as part of her AI training journey under NAVTTC, with an A+ certification in Data Science, AI, and Blockchain.
