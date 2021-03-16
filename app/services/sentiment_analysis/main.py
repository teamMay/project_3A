from entities.sentiment_analysis import SentimentAnalysisInput, SentimentAnalysisOutput
import sklearn.linear_model._logistic
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib
import os

sentiment_dict = {'curiosité/ neutre': 0,'inquiétude':1, 'détresse/epuisement/culpabilité' : 2, 
'heureux/remerciement/rassuré': 3}
labels = list(sentiment_dict.keys())

def distress_detector(input: SentimentAnalysisInput) -> SentimentAnalysisOutput:
	vectorizer = joblib.load(os.getcwd() + '/services/sentiment_analysis/tfidf.sav')
	vec_input = vectorizer.transform([input.text])
	loaded_model = joblib.load(os.getcwd() +'/services/sentiment_analysis/LR_model.sav')
	prediction = loaded_model.predict(vec_input)[0]
	confidence = round(loaded_model.predict_proba(vec_input)[0][int(prediction)],2)
	label = labels[prediction]

	return {"label": label, "confidence": confidence}
