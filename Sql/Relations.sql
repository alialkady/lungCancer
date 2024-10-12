-- Add foreign key to PatientInformation table
	 
ADD CONSTRAINT FK_PatientInformation_FactTable
FOREIGN KEY (patient_id) REFERENCES fact_table(patient_id);

-- Add foreign key to RiskFactors table
ALTER TABLE RiskFactors
ADD CONSTRAINT FK_RiskFactors_FactTable
FOREIGN KEY (patient_id) REFERENCES fact_table(patient_id);

-- Add foreign key to MedicalConditions table
ALTER TABLE MedicalConditions
ADD CONSTRAINT FK_MedicalConditions_FactTable
FOREIGN KEY (patient_id) REFERENCES fact_table(patient_id);

-- Add foreign key to Treatments table
ALTER TABLE Treatments
ADD CONSTRAINT FK_Treatments_FactTable
FOREIGN KEY (patient_id) REFERENCES fact_table(patient_id);

-- Add foreign key to Outcomes table
ALTER TABLE Outcomes
ADD CONSTRAINT FK_Outcomes_FactTable
FOREIGN KEY (patient_id) REFERENCES fact_table(patient_id);
