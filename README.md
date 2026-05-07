# News Topic Classification System

A deployed NLP-based news classification system that predicts the topic of a news headline using TF-IDF feature extraction and machine learning models (SVM and Logistic Regression).




## Categories


`World / Political`

`Sports`


`Business`

`Sci/Tech`


## Features


* Text preprocessing and cleaning


* TF-IDF vectorization


* Logistic Regression & SVM comparison


* Hyperparameter tuning with GridSearchCV


* Evaluation using Accuracy, Precision, Recall, F1-score, and Confusion Matrix


* Real-time prediction through a deployed Streamlit web app


## Tech Stack


`Python`


`Scikit-learn`

`re`

`Streamlit`


`Joblib`


`Pandas / NumPy`

## Live demo

Deployment: https://news-classifier123.streamlit.app/


## Example Prediction

Input:
`PSG vs Arsenal: Sky Sports writers select combined line-ups ahead of Champions League final in Budapest`

Prediction:
`Sports`


## Run Locally

`pip install -r requirements.txt`

`streamlit run app.py`



## Conclusions

Sports achieved the highest recall due to highly distinctive vocabulary.


Most classification overlap occurred between Business and Sci/Tech categories.


The deployed app performs real-time inference on custom user input.

