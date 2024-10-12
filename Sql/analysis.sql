#1 Gender Distribution:
-- Goal: Visualize and calculate the proportion of male vs female patients.

SELECT gender, COUNT(*) * 100.0 / (SELECT COUNT(*) FROM PatientInformation) AS percentage
FROM PatientInformation
GROUP BY gender;


#2 Age Distribution:
-- Goal: Understand the distribution of patient ages and identify age groups with higher occurrences of cancer.

SELECT CASE 
         WHEN age BETWEEN 0 AND 30 THEN '0-30'
         WHEN age BETWEEN 31 AND 50 THEN '31-50'
         WHEN age > 50 THEN '51+'
       END AS age_group, COUNT(*) AS frequency
FROM PatientInformation
GROUP BY age;

#3 Treatment Distribution Analysis:
-- Goal:  Analyze which treatments for lung cancer (e.g., chemotherapy, radiation, surgery) are most used.


SELECT treatment_type, COUNT(*) AS frequency 
FROM Treatments
GROUP BY treatment_type
ORDER BY frequency DESC;

#4 Survival Status Analysis:
-- Goal: Analyze the survival rates based on gender, age, and treatment type.

SELECT p.gender, t.treatment_type, 
       SUM(CASE WHEN o.survival_rate >= 0.5 THEN 1 ELSE 0 END) * 100.0 / COUNT(*) as survival_rate 
FROM PatientInformation p 
JOIN treatments t ON p.patient_id = t.patient_id  join outcomes o
on p.patient_id = o.patient_id
GROUP BY p.gender, t.treatment_type ;


#5 Treatment and Outcome Correlation:
-- Goal: Investigate correlations between treatment types (e.g., chemotherapy, radiation, surgery) and survival outcomes.

SELECT t.treatment_type, AVG(o.survival_rate) AS avg_survival_rate
FROM Treatments t
JOIN Outcomes o ON t.patient_id = o.patient_id
GROUP BY t.treatment_type;


#6 Smoking and Alcohol Consumption:
-- Goal: Explore the impact of smoking and alcohol consumption on lung cancer survival rates.

SELECT rf.smoking AS smoking_status, rf.alcohol_use AS alcohol_consumption, 
       AVG(o.survival_rate) AS avg_survival_rate
FROM RiskFactors rf
JOIN Outcomes o ON rf.patient_id = o.patient_id
GROUP BY rf.smoking, rf.alcohol_use;


#7 Age vs. Survival Rate:
-- Goal: Evaluate how survival rates vary with age.

SELECT pi.age, AVG(o.survival_rate) AS avg_survival_rate
FROM PatientInformation pi
JOIN Outcomes o ON pi.patient_id = o.patient_id
GROUP BY pi.age;


#8 Statistical Significance Testing:
-- Goal: Conduct statistical tests (e.g., chi-square, t-tests) to see if survival differences between different groups are significant (e.g., gender, treatment type, smoking).

SELECT rf.smoking AS smoking_status, 
       o.survival_rate, 
       COUNT(*) AS count
FROM RiskFactors rf
JOIN Outcomes o ON rf.patient_id = o.patient_id
GROUP BY rf.smoking, o.survival_rate;


#9 Survival Rate by Treatment Type and Age Group
-- Goal: Examine the survival rate for each treatment type, broken down by age groups.

SELECT t.treatment_type, 
       CASE 
         WHEN pi.age BETWEEN 0 AND 30 THEN '0-30'
         WHEN pi.age BETWEEN 31 AND 50 THEN '31-50'
         WHEN pi.age > 50 THEN '51+'
       END AS age_group, 
       AVG(o.survival_rate) AS avg_survival_rate
FROM Treatments t
JOIN PatientInformation pi ON t.patient_id = pi.patient_id
JOIN Outcomes o ON t.patient_id = o.patient_id
GROUP BY t.treatment_type, 
         CASE 
           WHEN pi.age BETWEEN 0 AND 30 THEN '0-30'
           WHEN pi.age BETWEEN 31 AND 50 THEN '31-50'
           WHEN pi.age > 50 THEN '51+'
         END;


#10 Alcohol Consumption and Survival Rate
-- Goal: Analyze whether alcohol consumption affects survival rates.

SELECT rf.alcohol_use AS alcohol_consumption, 
       AVG(o.survival_rate) AS avg_survival_rate
FROM RiskFactors rf
JOIN Outcomes o ON rf.patient_id = o.patient_id
GROUP BY rf.alcohol_use;