import numpy as np
import pickle

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

class Olist_cluster:
    '''Create a object to implement the olist clustering.
    '''
    def __init__(self, scaler_path:str, model_path:str):
        self.scaler = self.get_scaler(scaler_path)
        self.model = self.get_model(model_path)
        self.olist_cluster = {
            0: 'Former average',
            1: 'Current average',
            2: 'Big city average',
            3: 'Unsatisfied',
            4: 'Champions'}
    
    def get_model(self, model_path:str) -> KMeans:
        '''Open the pkl file which store the model.
        Arguments: 
            model_path: Path model with pkl extension
        
        Returns:
            model: Model object
        '''

        with open(model_path,"rb") as f:
            model = pickle.load(f)
        
        return model
    
    def get_scaler(self, scaler_path:str) -> StandardScaler:
        '''Open the pkl file which store the scaler.
        Arguments: 
            scaler_path: Path scaler with pkl extension
        
        Returns:
            scaler: scaler object
        '''

        with open(scaler_path,"rb") as f:
            scaler = pickle.load(f)
        
        return scaler

    def make_prediction(self, features:dict)->str:
        '''Predicts the cluster.
        Argument:
            features: list
        
        return:
            cluster: str
        '''
        features = np.array(list(features.values()))
        features_scaled = self.scaler.transform(features.reshape(1,-1))
        pred = self.model.predict(features_scaled.reshape(1,-1))[0]
        cluster_pred = self.olist_cluster[pred]
        return cluster_pred