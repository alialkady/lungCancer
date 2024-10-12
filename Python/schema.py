from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class PatientInformation(Base):
    __tablename__ = 'PatientInformation'
    
    patient_id = Column(String(20), primary_key=True)
    age = Column(String(20))
    gender = Column(String(20))


class RiskFactors(Base):
    __tablename__ = 'RiskFactors'
    
    patient_id = Column(String(20), primary_key=True)
    air_pollution = Column(String(20))
    alcohol_use = Column(String(20))
    smoking = Column(String(20))
    occupational_hazards = Column(String(20))
    dust_allergy = Column(String(20))
    genetic_risk = Column(String(20))
    passive_smoker = Column(String(20))


class MedicalConditions(Base):
    __tablename__ = 'MedicalConditions'
    
    patient_id = Column(String(20), primary_key=True)
    chronic_lung_disease = Column(String(20))
    fatigue = Column(String(20))
    weight_loss = Column(String(20))
    balanced_diet = Column(String(20))
    obesity = Column(String(20))
    chest_pain = Column(String(20))
    coughing_of_blood = Column(String(20))
    shortness_of_breath = Column(String(20))
    wheezing = Column(String(20))
    swallowing_difficulty = Column(String(20))
    clubbing_of_finger_nails = Column(String(20))
    frequent_cold = Column(String(20))
    snoring = Column(String(20))
    dry_cough = Column(String(20))


class Treatments(Base):
    __tablename__ = 'Treatments'
    
    patient_id = Column(String(20), primary_key=True)
    treatment_type = Column(String(50))
    cost = Column(String(20))


class Outcomes(Base):
    __tablename__ = 'Outcomes'
    
    patient_id = Column(String(20), primary_key=True)
    survival_rate = Column(String(20))
    treatment_outcome = Column(String(50))


# Database connection details
db_user = "root"
db_pass = "Aa22540444"
db_host = "127.0.0.1"
db_name = "lungcancerpy"

# Replace your connection details accordingly
engine = create_engine(f"mysql+pymysql://{db_user}:{db_pass}@{db_host}/{db_name}", echo=True)

# Create all the tables
Base.metadata.create_all(bind=engine)