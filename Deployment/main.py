from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from model import ModelPredict
from typing import List

app = FastAPI()
model = ModelPredict()


class QueryText(BaseModel):
    text: str


class TestingData(BaseModel):
    texts: List[str]


# @app.post("/predict", summary="Predict single input")
# def predict(query_text: QueryText):
#     try:
#         prediction = model.predict([query_text.text])[0]
#         return prediction
#     except Exception as e:
#         raise HTTPException(status_code=503, detail=str(e))


@app.post("/predict-batch", summary="predict a batch of sentences")
def predict_batch(testing_data: TestingData):
    try:
        predictions = model.predict(testing_data.texts)
        return predictions
    except Exception as e:
        raise HTTPException(status_code=503, detail=str(e))


@app.get("/")
def home():
    return {"message": "System is up"}
