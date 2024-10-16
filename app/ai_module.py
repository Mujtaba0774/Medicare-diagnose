from fastapi import HTTPException

#AI health diagnosis
def diagnose_health_issues(symptoms: str):
    if "fever" in symptoms.lower():
        return {"diagnosis": "You might have the flu.", "suggestions": ["Rest", "Drink fluids", "Take aspirin"]}
    else:
        raise HTTPException(status_code=400, detail="Unable to diagnose.")
