import sys

from pyspark.sql import SparkSession

from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import LinearRegression
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml import Pipeline

# A1
spark = SparkSession.builder.appName("ws5-regression").getOrCreate()

# A2
if len(sys.argv) < 2:
    print("Usage: sparkdemo.py (path to csv)")
    sys.exit()

path = sys.argv[1]
df = spark.read.csv(path, header=True, inferSchema=True)

df.show()

# A3
featureAssembler = VectorAssembler(inputCols=["total_bill", "size"], outputCol="features")

# A4
train_set, test_set = df.randomSplit([0.8,0.2], seed=42)

# A5
linRegModel = LinearRegression(featuresCol="features", labelCol="tip")
pipeline = Pipeline(stages=[featureAssembler, linRegModel])
pipelineModel = pipeline.fit(train_set)

# A6
results = pipelineModel.transform(test_set)

# A7
evaluator = RegressionEvaluator(labelCol="tip", predictionCol="prediction")
rmse = evaluator.evaluate(results, {evaluator.metricName: "rmse"})
r2 = evaluator.evaluate(results, {evaluator.metricName: "r2"})

# A8
fittedModel = pipelineModel.stages[-1]
print("")
print("A8/Printing Results")
print(f"Coefficients: {fittedModel.coefficients}")
print(f"Intercept: {fittedModel.intercept}")
print(f"RMSE: {rmse}")
print(f"R^2: {r2}")
print("")
