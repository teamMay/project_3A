from typing import List, Optional, Tuple, Dict
from pydantic import BaseModel, Field


class TopicClassificationInput(BaseModel):
    text: str = Field(..., description="Text content to analyse", example="Bonjour, mon bébé a du mal à s'endormir")

    class Config:
        schema_extra = {
            "example": {"text": "Bonjour, ma fille a de la fièvre"}
        }


class TopicClassificationOutput(BaseModel):
    label: str = Field(..., description="Detected topic", example="Pédiatrie générale/Sommeil")
    confidence: float = Field(..., description="Confidence for label result in %", example=0.35)

    class Config:
        schema_extra = {
            "example": {"label": "Pédiatrie générale", "confidence": 0.58}
        }
