import joblib
import pandas as pd

labels = [
    'await',
    'sell',
    'buy'
]

class NaiveBayesClassifier:
    def __init__(self, model_file):
        self.model = joblib.load(model_file)

    def classify(self, df: pd.DataFrame):
            # Realizar a classificação usando o modelo carregado
            prediction = int(self.model.predict(df)[0])
            
            # Formatar a classificação como um JSON
            result = {'classification': labels[prediction]}
            
            return result
