# IMDb Sentiment Analysis using LSTM and Flask

#Project Overview
This project implements a Sentiment Analysis System for IMDb movie reviews using Long Short-Term Memory (LSTM) neural networks. The trained model predicts whether a given review expresses a positive or negative sentiment. The project also includes a Flask web application for real-time sentiment prediction.

#Technologies Used
Programming Language: Python 
Libraries: TensorFlow, Keras, NumPy, Pandas, NLTK, Flask
Model Architecture: LSTM with Embedding, Dropout, and Dense layers
Dataset: IMDb movie reviews dataset
Deployment: Flask web app for real-time predictions
Optimization: Adam Optimizer, Categorical Cross-Entropy Loss

#Features
Preprocesses text by removing HTML tags, URLs, special characters, and emojis
LSTM-based deep learning model for sentiment analysis
Uses Model Checkpointing to save the best model
Web-based sentiment prediction using Flask
Saves and loads Tokenizer using JSON for consistent preprocessing

#Future Improvements
Improve model accuracy with fine-tuned hyperparameters
Deploy as a REST API for wider accessibility
Integrate with a front-end framework for better UI

#License
This project is open-source under the MIT License.
