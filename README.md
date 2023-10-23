# Forecaster-app
The app can be accessed with the following link: https://forecaster-app-lhdlo22sdhvfdoipcwn5vi.streamlit.app/

# How it works
No setup of any kind is needed to run the app. The app is hosted on streamlit community cloud, click on the above link and start making forecasting for the year 2022.

# Project Overview
The data daily.csv file provides the number of the observed scanned receipts each day for the year 2021. Based on this prior knowledge, I have developed an Deep Learning algorithm which can predict the approximate number of the scanned receipts for each month of 2022.

# Model Training
I have trained a Tensorflow model in google colab environment that predict the approximate number of scanned receipts for each month of 2022.
Detailed description of model development with the code can be accessed using the following link:
https://colab.research.google.com/drive/1rxeO_y3vENw5-d-_ONb5R0RUfIEefLGw?usp=sharing

### Note
If you are trying to reproduce the model in colab, please download the data_daily.csv file and upload it in the colab to reproduce the model. An alternate method to test the app locally without using the **Forecaster-app**:  
1. clone the repository and create a virtual environment in python
2. install all the required libraries using **requirements.txt**
3. run the following command: **streamlit run app.py**
4. This will open a webpage, where you can forecast predictions for each month of 2022 
