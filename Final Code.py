import json

symptom_disease_db = {
    "fever": {"diseases": ["Flu", "Malaria", "Typhoid"], "treatments": ["Rest", "Hydration", "Medication (consult doctor)"]},
    "cough": {"diseases": ["Flu", "Common Cold", "Bronchitis"], "treatments": ["Rest", "Hydration", "Cough syrup (consult doctor)"]},
    "headache": {"diseases": ["Stress", "Migraine", "Dehydration"], "treatments": ["Rest", "Hydration", "Pain reliever (consult doctor)"]},
    "fatigue": {"diseases": ["Flu", "Anemia", "Stress"], "treatments": ["Rest", "Healthy diet", "Stress management"]},
    "muscle_ache": {"diseases": ["Flu", "Dehydration", "Overexertion"], "treatments": ["Rest", "Hydration", "Pain reliever (consult doctor)"]},
    # ... more symptoms and diseases
}

def get_symptoms():
    symptoms = []
    print("Enter your symptoms (type 'done' when finished):")
    while True:
        symptom = input("> ").lower()
        if symptom == "done":
            break
        symptoms.append(symptom)
    return symptoms

def diagnose(symptoms):
    possible_diseases = set()
    for symptom in symptoms:
        if symptom in symptom_disease_db:
            possible_diseases.update(symptom_disease_db[symptom]["diseases"])
        else:
            print(f"Symptom '{symptom}' not recognized in the database.")

    if not possible_diseases:
        return "No matching diseases found."

    return list(possible_diseases)

def suggest_treatment(diseases):
    treatments = set()
    for disease in diseases:
        for symptom, data in symptom_disease_db.items():
            if disease in data["diseases"]:
                treatments.update(data["treatments"])
    return list(treatments)

def main():
    print("Welcome to the AI Symptom Checker and Treatment Advisor!")

    symptoms = get_symptoms()
    if not symptoms:
        print("No symptoms entered.")
        return

    diseases = diagnose(symptoms)

    if isinstance(diseases, str):
        print(diseases)
        return

    print("\nPossible Diseases:")
    for disease in diseases:
        print(f"- {disease}")

    treatments = suggest_treatment(diseases)

    print("\nSuggested Treatments (Consult a doctor for accurate diagnosis and treatment):")
    for treatment in treatments:
        print(f"- {treatment}")

if __name__ == "__main__":
    main()