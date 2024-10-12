UPDATE fact_table
SET 
    total_risk_factors = (
        SELECT 
            (rf.air_pollution + rf.alcohol_use + rf.smoking + rf.occupational_hazards + 
             rf.dust_allergy + rf.genetic_risk + rf.passive_smoker) 
        FROM RiskFactors rf
        WHERE rf.patient_id = fact_table.patient_id
    ),
    total_medical_conditions = (
        SELECT 
            (mc.chronic_lung_disease + mc.fatigue + mc.weight_loss + mc.balanced_diet + 
             mc.obesity + mc.chest_pain + mc.coughing_of_blood + mc.shortness_of_breath + 
             mc.wheezing + mc.swallowing_difficulty + mc.clubbing_of_finger_nails + 
             mc.frequent_cold + mc.snoring + mc.dry_cough) 
        FROM MedicalConditions mc
        WHERE mc.patient_id = fact_table.patient_id
    )
WHERE patient_id IN (SELECT patient_id FROM RiskFactors);

