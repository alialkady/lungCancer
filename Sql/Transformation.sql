-- Altering columns in PatientInformation table
ALTER TABLE PatientInformation
ALTER COLUMN age INT;

ALTER TABLE PatientInformation
ALTER COLUMN gender INT;

-- Altering columns in RiskFactors table
ALTER TABLE RiskFactors
ALTER COLUMN air_pollution INT;

ALTER TABLE RiskFactors
ALTER COLUMN alcohol_use INT;

ALTER TABLE RiskFactors
ALTER COLUMN dust_allergy INT;

ALTER TABLE RiskFactors
ALTER COLUMN occupational_hazards INT;

ALTER TABLE RiskFactors
ALTER COLUMN genetic_risk INT;

ALTER TABLE RiskFactors
ALTER COLUMN smoking INT;

ALTER TABLE RiskFactors
ALTER COLUMN passive_smoker INT;

-- Altering columns in MedicalConditions table
ALTER TABLE MedicalConditions
ALTER COLUMN chronic_lung_disease INT;

ALTER TABLE MedicalConditions
ALTER COLUMN fatigue INT;

ALTER TABLE MedicalConditions
ALTER COLUMN weight_loss INT;

ALTER TABLE MedicalConditions
ALTER COLUMN balanced_diet INT;

ALTER TABLE MedicalConditions
ALTER COLUMN obesity INT;

ALTER TABLE MedicalConditions
ALTER COLUMN chest_pain INT;

ALTER TABLE MedicalConditions
ALTER COLUMN coughing_of_blood INT;

ALTER TABLE MedicalConditions
ALTER COLUMN shortness_of_breath INT;

ALTER TABLE MedicalConditions
ALTER COLUMN wheezing INT;

ALTER TABLE MedicalConditions
ALTER COLUMN swallowing_difficulty INT;

ALTER TABLE MedicalConditions
ALTER COLUMN clubbing_of_finger_nails INT;

ALTER TABLE MedicalConditions
ALTER COLUMN frequent_cold INT;

ALTER TABLE MedicalConditions
ALTER COLUMN dry_cough INT;

ALTER TABLE MedicalConditions
ALTER COLUMN snoring INT;

-- Altering columns in Treatments table
ALTER TABLE Treatments
ALTER COLUMN cost DECIMAL(10, 2);

-- Altering columns in Outcomes table
ALTER TABLE Outcomes
ALTER COLUMN survival_rate DECIMAL(5, 2);
