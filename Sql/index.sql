
CREATE INDEX idx_patient_id ON fact_table(patient_id);

CREATE INDEX idx_age ON PatientInformation(age);
CREATE INDEX idx_gender ON PatientInformation(gender);
CREATE INDEX idx_patient_id_info ON PatientInformation(patient_id);

CREATE INDEX idx_patient_id_risk ON RiskFactors(patient_id);
CREATE INDEX idx_alcohol_use ON RiskFactors(alcohol_use);
CREATE INDEX idx_smoking ON RiskFactors(smoking);

CREATE INDEX idx_patient_id_medical ON MedicalConditions(patient_id);
CREATE INDEX idx_chronic_lung_disease ON MedicalConditions(chronic_lung_disease);
CREATE INDEX idx_fatigue ON MedicalConditions(fatigue);

CREATE INDEX idx_patient_id_treatment ON Treatments(patient_id);
CREATE INDEX idx_treatment_type ON Treatments(treatment_type);

CREATE INDEX idx_patient_id_outcome ON Outcomes(patient_id);
CREATE INDEX idx_survival_rate ON Outcomes(survival_rate);
