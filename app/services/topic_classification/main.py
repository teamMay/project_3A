from entities.topic_classification import TopicClassificationInput, TopicClassificationOutput
import sklearn.linear_model._logistic
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib
import os

theme_dict = {'Aucun': 0,'Alimentation':1, 'Allaitement' : 2, 
'Education positive': 3, 
'Eveil & Motricité': 4, 
'Ma vie de parent' : 5, 
'Pédiatrie générale' :6, 
'Sommeil':7}
labels = list(theme_dict.keys())

def topic_detector(input: TopicClassificationInput) -> TopicClassificationOutput:
	vectorizer = joblib.load(os.getcwd() + '/services/topic_classification/tfidf.sav')
	print(input)
	vec_input = vectorizer.transform([input.text])
	loaded_model = joblib.load(os.getcwd() +'/services/topic_classification/LR_model.sav')
	prediction = loaded_model.predict(vec_input)[0]
	proba = loaded_model.predict_proba(vec_input)[0]
	confidence = round(loaded_model.predict_proba(vec_input)[0][int(prediction)],2)
	label = labels[preidction]
	return {"label": label, "confidence": confidence}