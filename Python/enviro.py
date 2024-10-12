from pyspark.sql import SparkSession

# Use a raw string to handle backslashes in Windows paths
jdbc_jar_path = r"D:\Programming\jdbc6\sqljdbc_6.0\enu\jre8\sqljdbc42.jar"

spark = SparkSession.builder \
    .appName("SQLServerConnection") \
    .config("spark.jars", jdbc_jar_path) \
    .getOrCreate()

# Connection details with trustServerCertificate=true
jdbc_url = "jdbc:sqlserver://DESKTOP-FCEDQJG:1433;databaseName=cancer;trustServerCertificate=true"
table = "PatinetInformation"

# Replace with your SQL Server credentials
df = spark.read.format("jdbc").options(
    url=jdbc_url,
    driver="com.microsoft.sqlserver.jdbc.SQLServerDriver",
    dbtable=table,
    user="alialkady",
    password="Aa22540444"
).load()

# Display the data
df.show(5)

# Close Spark session
#spark.stop()


import pickle
from pyspark.sql import SparkSession
from pyspark.sql.types import IntegerType
import numpy as np

# Create a Spark session
spark = SparkSession.builder \
    .appName("SQLServerConnection") \
    .config("spark.jars", jdbc_jar_path) \
    .getOrCreate()

# Load the pre-trained model
with open('models/logistic_regression.pkl', 'rb') as file:
    model = pickle.load(file)  # Load the model

# Verify the model type
print(f"Model type: {type(model)}")  # Check if it's a scikit-learn model

# Load data from SQL Server into Spark DataFrame
df = spark.read.format("jdbc").options(
    url=jdbc_url,
    driver="com.microsoft.sqlserver.jdbc.SQLServerDriver",
    dbtable=table,
    user="alialkady",
    password="Aa22540444"
).load()

# Select the feature columns used in the original model
feature_columns = ['coughing_of_blood', 'alcohol_use', 'passive_smoker',
                   'obesity', 'smoking', 'balanced_diet', 'chest_pain',
                   'fatigue', 'air_pollution', 'genetic_risk']  # Adjust as needed

# Convert Spark DataFrame to Pandas DataFrame for model input
features = df.select(*feature_columns).toPandas()  # Convert Spark DataFrame to Pandas DataFrame

# Check selected features
print("Selected Features:\n", features.head())  # Display the first few rows

# Make predictions using the loaded model
predictions = modelmodel.predict(features)  # Use the model to predict

# Ensure predictions is a NumPy array
print(f"Predictions type: {type(predictions)}")  # Check predictions type

# Add predictions to the original Spark DataFrame
df_with_predictions = df.withColumn('predictions', spark.createDataFrame(predictions.tolist(), IntegerType()))

# Show results
df_with_predictions.show()
