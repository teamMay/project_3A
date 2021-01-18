from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .entities.sentiment_analysis import SentimentAnalysisInput, SentimentAnalysisOutput
from .services.sentiment_analysis.main import distress_detector

app = FastAPI()


origins = ["http://localhost", "http://localhost:8080", "https://sentiment-analysis.may-care.fr"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/sentiment-analysis", response_model=SentimentAnalysisOutput)
async def sentiment_analysis(text_input: SentimentAnalysisInput) -> SentimentAnalysisOutput:
    return distress_detector(text_input)
