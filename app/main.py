from fastapi import FastAPI
import mlflow
import pandas as pd

app = FastAPI()

# Load the model from MLflow
model = mlflow.pyfunc.load_model("s3://mlflowtacit/1/efe465478e0041a98d994d37ef4e87cb/artifacts/model_artifacts/")

@app.post("/predict")
def predict(features: dict):
    # Convert input features into DataFrame
    input_df = pd.DataFrame([features])
    prediction = model.predict(input_df)
    return {"prediction": prediction.tolist()}
