import pandas as pd
import streamlit as st
from plotly import graph_objs as go
import pymongo
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error


st.set_page_config(layout='wide', initial_sidebar_state='expanded')


st.title('Dashboard Siswa :student:')

data = pd.read_csv("combine_final_fix.csv")

# Sidebar for user input
st.sidebar.title("Masukan Data Siswa :books:")
input_data = st.sidebar.text_input(label="Nama", placeholder="masukan nama")


if input_data:
    filtered_data = data[data['name'].str.contains(input_data, case=False, na=False)]
    st.subheader('Raw Data: Filtered by Name')
    st.write(filtered_data)
else:
    st.subheader('Raw Data: Last 50 Entries')
    st.write(data.tail(50))
    # Pie chart
    st.subheader('Chart')
    cabang_counts = data['branch_name'].value_counts()
    fig = go.Figure(data=[go.Pie(labels=cabang_counts.index, values=cabang_counts.values)])
    st.plotly_chart(fig)
    # Split the data into features and target variable
    X = data[['twk', 'tiu', 'tkp']]  # Replace 'feature1', 'feature2', 'feature3' with actual feature names
    y = data['total']  # Replace 'total_exam_score' with actual target variable name

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create and train the SVM model
    svm_model = SVR()
    svm_model.fit(X_train, y_train)

    # Make predictions on the test set
    y_pred = svm_model.predict(X_test)

    # Evaluate the model
    mse = mean_squared_error(y_test, y_pred)
    st.subheader('Model Evaluation')
    st.write('Mean Squared Error:', mse)
    # User input for prediction
    input_twk = st.sidebar.number_input(label="Nilai TWK", value=0.0)
    input_tiu = st.sidebar.number_input(label="Nilai TIU", value=0.0)
    input_tkp = st.sidebar.number_input(label="Nilai TKP", value=0.0)

    # Predict the total score for the input values
    input_values = [[input_twk, input_tiu, input_tkp]]
    predicted_score = svm_model.predict(input_values)

    # Display the predicted score
    st.sidebar.subheader('Predicted Total Score')
    st.sidebar.write(predicted_score)