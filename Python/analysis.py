import pandas as pd
from sqlalchemy.orm import sessionmaker
from enviro import engine
from schema import PatientInformation, RiskFactors, MedicalConditions, Treatments, Outcomes
import traceback
from load import session
from sqlalchemy import func, case
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# Gender Distribution

def gender_distribution():
    try:
        result = session.query(
            PatientInformation.gender,
            func.count(PatientInformation.patient_id) * 100.0 / session.query(func.count(PatientInformation.patient_id)).scalar()
        ).group_by(PatientInformation.gender).all()

        # Convert to DataFrame for easier manipulation/plotting
        df_gender = pd.DataFrame(result, columns=['gender', 'percentage'])

        # Plot the gender distribution
        df_gender.plot(kind='bar', x='gender', y='percentage', legend=False)
        plt.title('Gender Distribution')
        plt.xlabel('Gender')
        plt.ylabel('Percentage')
        plt.show()

    except Exception as e:
        print(f"Error during Gender Distribution Analysis: {e}")
        print(traceback.format_exc())

# Call the function
gender_distribution()


# Age Distribution

def age_distribution():
    try:
        
        result = session.query(
            case(
                (PatientInformation.age.between(0, 30), '0-30'),
                (PatientInformation.age.between(31, 50), '31-50'),
                (PatientInformation.age > 50, '51+')
            ).label('age_group'),
            func.count(PatientInformation.patient_id)
        ).group_by('age_group').all()

        # Convert to DataFrame for plotting
        df_age = pd.DataFrame(result, columns=['age_group', 'frequency'])

        # Plot age distribution
        df_age.plot(kind='bar', x='age_group', y='frequency', legend=False)
        plt.title('Age Distribution')
        plt.xlabel('Age Group')
        plt.ylabel('Frequency')
        plt.show()

    except Exception as e:
        print(f"Error during Age Distribution Analysis: {e}")
        print(traceback.format_exc())

age_distribution()


# Treatment Distribution Analysis

def treatment_distribution():
    try:
        result = session.query(
            Treatments.treatment_type,
            func.count(Treatments.patient_id)
        ).group_by(Treatments.treatment_type).order_by(func.count(Treatments.patient_id).desc()).all()

        # Convert to DataFrame for plotting
        df_treatment = pd.DataFrame(result, columns=['treatment_type', 'frequency'])

        # Plot treatment distribution
        df_treatment.plot(kind='bar', x='treatment_type', y='frequency', legend=False)
        plt.title('Treatment Distribution')
        plt.xlabel('Treatment Type')
        plt.ylabel('Frequency')
        plt.show()

    except Exception as e:
        print(f"Error during Treatment Distribution Analysis: {e}")
        print(traceback.format_exc())

# Call the function
treatment_distribution()


# Survival Status Analysis

def survival_status_analysis():
    try:
        # Adjusting the case() function to use positional arguments correctly
        result = session.query(
            PatientInformation.gender,
            Treatments.treatment_type,
            (func.sum(case((Outcomes.survival_rate >= 0.5, 1), else_=0)) * 100.0 / func.count(PatientInformation.patient_id)).label('survival_rate')
        ) \
        .join(Treatments, PatientInformation.patient_id == Treatments.patient_id) \
        .join(Outcomes, PatientInformation.patient_id == Outcomes.patient_id) \
        .group_by(PatientInformation.gender, Treatments.treatment_type).all()

        # Convert the result to DataFrame for further analysis or visualization
        df_survival = pd.DataFrame(result, columns=['gender', 'treatment_type', 'survival_rate'])

        # Print or visualize the DataFrame as needed
        print(df_survival)

    except Exception as e:
        print(f"Error during Survival Status Analysis: {e}")
        print(traceback.format_exc())

# Call the function
survival_status_analysis()



#5 Treatment and Outcome Correlation

def treatment_outcome_correlation():
    try:
        result = session.query(
            Treatments.treatment_type,
            func.avg(Outcomes.survival_rate)
        ).join(Outcomes, Treatments.patient_id == Outcomes.patient_id
        ).group_by(Treatments.treatment_type).all()

        # Convert to DataFrame
        df_treatment_corr = pd.DataFrame(result, columns=['treatment_type', 'avg_survival_rate'])

        # Plot Treatment vs. Survival Rate
        df_treatment_corr.plot(kind='bar', x='treatment_type', y='avg_survival_rate', legend=False)
        plt.title('Treatment and Outcome Correlation')
        plt.xlabel('Treatment Type')
        plt.ylabel('Average Survival Rate')
        plt.show()

    except Exception as e:
        print(f"Error during Treatment and Outcome Correlation: {e}")
        print(traceback.format_exc())

# Call the function
treatment_outcome_correlation()
