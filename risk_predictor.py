def predict_risk(ratings: dict) -> dict:
    values = list(ratings.values())
    avg = sum(values) / len(values) if values else 3.0
    risk_score = (avg - 1) / 4
    if risk_score < 0.33:
        level = "Low"
    elif risk_score < 0.66:
        level = "Moderate"
    else:
        level = "High"

    top_features = sorted(ratings.items(), key=lambda x: x[1], reverse=True)[:3]
    top_factors = [f"{f.replace('_',' ')} (rating {v})" for f, v in top_features]

    return {
        "risk_level": level,
        "risk_score": round(risk_score, 2),
        "confidence": "Medium",
        "top_factors": top_factors,
    }