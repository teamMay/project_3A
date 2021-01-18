from entities.sentiment_analysis import SentimentAnalysisInput, SentimentAnalysisOutput


def distress_detector(input: SentimentAnalysisInput) -> SentimentAnalysisOutput:
    # Hello darkness my old friend
    # PLACE YOUR MODEL CALL THERE
    if "déprimée" in input.text:
        return {"label": "Distress", "confidence": 0.99}

    return {"label": "Neutral", "confidence": 0.75}
