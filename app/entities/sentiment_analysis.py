from typing import List, Optional, Tuple, Dict
from pydantic import BaseModel, Field


class SentimentAnalysisInput(BaseModel):
    text: str = Field(..., description="Text content to analyse", example="Bonjour, je suis déprimée")

    class Config:
        schema_extra = {
            "example": {"text": "Bonjour, je me sens à bout."}
        }


class SentimentAnalysisOutput(BaseModel):
    label: str = Field(..., description="Detected class", example="Inquiétude / Détresse")
    confidence: float = Field(..., description="Confidence for label result in %", example=0.35)

    class Config:
        schema_extra = {
            "example": {"label": "Distress", "confidence": 0.58}
        }
