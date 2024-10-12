

CREATE TABLE fact_table (
    patient_id VARCHAR(20) PRIMARY KEY,
	total_risk_factors int,
	total_medical_conditions int
);

CREATE TABLE PatientInformation (
    patient_id VARCHAR(20) PRIMARY KEY,
    age VARCHAR(20),
    gender VARCHAR(20),
    
);

CREATE TABLE RiskFactors (
    patient_id VARCHAR(20),
    air_pollution VARCHAR(20),
    alcohol_use VARCHAR(20),
    smoking VARCHAR(20),
    occupational_hazards VARCHAR(20),
    dust_allergy VARCHAR(20),
    genetic_risk VARCHAR(20),
    passive_smoker VARCHAR(20),
  
);

CREATE TABLE MedicalConditions (
    patient_id VARCHAR(20),
    chronic_lung_disease VARCHAR(20),
    fatigue VARCHAR(20),
    weight_loss VARCHAR(20),
    balanced_diet VARCHAR(20),
    obesity VARCHAR(20),  -- Fixed typo from 'obesty'
    chest_pain VARCHAR(20),
    coughing_of_blood VARCHAR(20),
    shortness_of_breath VARCHAR(20),
    wheezing VARCHAR(20),
    swallowing_difficulty VARCHAR(20),
    clubbing_of_finger_nails VARCHAR(20),
    frequent_cold VARCHAR(20),
    snoring VARCHAR(20),
    dry_cough VARCHAR(20),

);

CREATE TABLE Treatments (
    patient_id VARCHAR(20),
    treatment_type VARCHAR(50),
    cost VARCHAR(20),
    
);

CREATE TABLE Outcomes (
    patient_id VARCHAR(20),
    survival_rate VARCHAR(20),
    treatment_outcome VARCHAR(50),
   
);

