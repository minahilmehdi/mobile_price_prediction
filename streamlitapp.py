import pandas as pd
import joblib
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import streamlit as st

# load the updated model to be make live
model = joblib.load("liveModelIV1.pkl")

# load the data to check accuracy
data = pd.read_csv("mobile_price_range_data.csv")
X = data.iloc[:, :-1]
y = data.iloc[:, -1]

#train test split for accuracy calculation on only the testing data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# for predictions
y_pred = model.predict(X_test)

#Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

#Page title
st.title("Model Accuracy and Real-Time Prediction")

#Display accuracy
st.write(f"Model: {accuracy}")

# Real time prediction based on user inputs
st.header("Real-Time Prediction")
input_data = []
for col in X_test.columns:
    input_value = st.numner_input(f'Input for feature{col}', value='')
    input_data.append(input_value)

#Convert input data to dataframe
input_df = pd.DataFrame([input_data], columns=X_test.columns)

#Make Prediction
if st.button("Predict"):
    prediction = model.predict(input_df)
    st.write(f'Prediction: {prediction[0]}')
    