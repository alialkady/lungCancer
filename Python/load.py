import pandas as pd
from sqlalchemy.orm import sessionmaker
from enviro import engine
from schema import PatientInformation, RiskFactors, MedicalConditions, Treatments, Outcomes
import traceback

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

def load_csv():
    try:
        # Load the single CSV file into a DataFrame
        df = pd.read_csv(r"cancer_patient_data_sets_with_treatment_type.csv")
    except FileNotFoundError as e:
        print(f"File not found: {e}")
        return

    # STEP 1: Insert data into PatientInformation table
    for _, row in df.iterrows():
        try:
            # Insert into PatientInformation
            patient_info = PatientInformation(
                patient_id=row['patient_id'],
                age=row['age'],
                gender=row['gender']
            )
            session.add(patient_info)

        except Exception as e:
            print(f"Error inserting into PatientInformation for patient_id {row['patient_id']}: {e}")
            print(traceback.format_exc())
            session.rollback()
            continue

    # Commit PatientInformation first
    try:
        session.commit()
        print("Successfully committed PatientInformation.")
    except Exception as e:
        session.rollback()
        print(f"Error during commit for PatientInformation: {e}")
        print(traceback.format_exc())
        return

    # STEP 2: Insert data into the dependent tables
    for _, row in df.iterrows():
        # Check if patient_id exists in PatientInformation table before inserting
        patient_exists = session.query(PatientInformation).filter_by(patient_id=row['patient_id']).first()

        if not patient_exists:
            print(f"Skipping insertion for patient_id {row['patient_id']} - PatientInformation record not found.")
            continue

        try:
            # Insert into RiskFactors
            risk_factors = RiskFactors(
                patient_id=row['patient_id'],
                air_pollution=row['air_pollution'],
                alcohol_use=row['alcohol_use'],
                smoking=row['smoking'],
                occupational_hazards=row['occupational_hazards'],
                dust_allergy=row['dust_allergy'],
                genetic_risk=row['genetic_risk'],
                passive_smoker=row['passive_smoker']
            )
            session.add(risk_factors)

            # Insert into MedicalConditions
            medical_condition = MedicalConditions(
                patient_id=row['patient_id'],
                chronic_lung_disease=row['chronic_lung_disease'],
                fatigue=row['fatigue'],
                weight_loss=row['weight_loss'],
                balanced_diet=row['balanced_diet'],
                obesity=row['obesity'],
                chest_pain=row['chest_pain'],
                coughing_of_blood=row['coughing_of_blood'],
                shortness_of_breath=row['shortness_of_breath'],
                wheezing=row['wheezing'],
                swallowing_difficulty=row['swallowing_difficulty'],
                clubbing_of_finger_nails=row['clubbing_of_finger_nails'],
                frequent_cold=row['frequent_cold'],
                snoring=row['snoring'],
                dry_cough=row['dry_cough']
            )
            session.add(medical_condition)

            # Insert into Treatments
            treatment = Treatments(
                patient_id=row['patient_id'],
                treatment_type=row['treatment_type'],
                cost=row['cost']
            )
            session.add(treatment)

            # Insert into Outcomes
            outcome = Outcomes(
                patient_id=row['patient_id'],
                survival_rate=row['survival_rate'],
                treatment_outcome=row['treatment_outcome']
            )
            session.add(outcome)

        except Exception as e:
            print(f"Error inserting data for patient_id {row['patient_id']}: {e}")
            print(traceback.format_exc())
            session.rollback()
            continue

    # Commit the session to save the changes for the dependent tables
    try:
        session.commit()
        print("Successfully committed dependent tables.")
    except Exception as e:
        session.rollback()
        print(f"Error occurred during commit for dependent tables: {e}")
        print(traceback.format_exc())
    finally:
        session.close()

# Call the function to load the CSV data into the database
load_csv()
