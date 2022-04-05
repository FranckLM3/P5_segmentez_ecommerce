from fastapi import FastAPI
from fastapi.responses import JSONResponse
from api.olist_cluster_object import Olist_cluster
from pydantic import BaseModel

#create the application
app = FastAPI(
    title = "Olist Clustering API",
    version = 1.0,
    description = "Simple API to make predict cluster of Olist client."
)

#creating the classifier

clusterer = Olist_cluster('api/pickle_scaler', 'api/pickle_model')

#Model
class Customer(BaseModel):
    recency: int
    frequency: float
    monetary_value: float
    satisfactory: float
    city_size: float

@app.post("/",tags = ["olist_clustering"])
def get_prediction(features:Customer):
    cluster_pred = clusterer.make_prediction(features.dict())
    return JSONResponse({"cluster":cluster_pred})