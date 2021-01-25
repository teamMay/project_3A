from entities.sentiment_analysis import SentimentAnalysisInput, SentimentAnalysisOutput
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegressionCV
from googletrans import Translator

def translateToEng(sentence):
	translator = Translator()
	return(translator.translate(sentence, src='fr').text)


def distress_detector(input: SentimentAnalysisInput) -> SentimentAnalysisOutput:
	vectorizer = joblib.load('/services/sentiment_analysis/tfidf.sav')
	eng_input = vectorizer.transform([translateToEng(input)])
	loaded_model = joblib.load('/services/sentiment_analysis/LR_model.sav')
	prediction = loaded_model.predict(eng_input)[0]
	confidence = round(loaded_model.predict_proba(eng_input)[int(result)],2)
	if prediction == 0:
		label = 'Distressed'
	else:
		label = 'Calm'
	return {"label": label, "confidence": confidence}
