import streamlit as st
from sklearn.preprocessing import*
import pandas as pd 
from olist_cluster_object import Olist_cluster
from pydantic import BaseModel

st.markdown('''
## Olist customer clustering prediction apps
''')

#P5_segmentez_ecommerce/deploy/WebApps/

customers = pd.read_csv('P5_segmentez_ecommerce/deploy/WebApps/DRV_customer_clustering_all.csv')        
st.sidebar.header("Select the customer")

def user_input():
    customer_id = st.sidebar.selectbox('Customer id', (customers['customer_unique_id'].sample(2000).unique()))
    df = customers.loc[customers['customer_unique_id'] == customer_id, :]
    return(df)
df=user_input()

#Model
class Customer(BaseModel):
    recency: int
    frequency: float
    monetary_value: float
    satisfactory: float
    city_size: float

selected_features = ['recency',
                     'frequency',
                     'monetary_value',
                     'avg_review_score',
                     'customer_city_size']

df = df[selected_features]

customer = Customer(recency=df['recency'],
                    frequency=df['frequency'],
                    monetary_value=df['monetary_value'],
                    satisfactory=df['avg_review_score'],
                    city_size=df['customer_city_size'],)


st.subheader('Customer informations: ')
st.write('Recency: ', round(df.iloc[0, 0], 0))
st.write('Frequency: ', round(df.iloc[0, 1], 0))
st.write('Monetary: ', round(df.iloc[0, 2], 2))
st.write('Satisfactory: ', round(df.iloc[0, 3], 1))
st.write('City Size: ', round(df.iloc[0, 4], 0))

#creating the classifier
clusterer = Olist_cluster('P5_segmentez_ecommerce/deploy/WebApps/pickle_scaler', 'P5_segmentez_ecommerce/deploy/WebApps/pickle_model')

def get_prediction(features:Customer):
    cluster_pred = clusterer.make_prediction(features.dict())
    return (cluster_pred)

prediction = get_prediction(customer)
st.markdown("### Customer cluster is: ")
st.text(prediction)