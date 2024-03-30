from typing import Any, Dict
import pandas as pd
from src.infra.Gateway.NaiveBayesClassifier import NaiveBayesClassifier
from src.utils.handle import handle

FILE = 'C:\\Users\\Desktop\\Projects\\NLP\\naive-bayes-classifier-microservices\\naive-bayes-classifier-runner-py\\src\\mock\\modelo_naive_bayes.pkl'

class ClassificationService:

    def __init__(self) -> None:
        pass
    
    def execute(self, id: str, sample: Dict[str, Any]):
        
        df = pd.DataFrame(sample, index=[0])
        naiveBayesClassifier = NaiveBayesClassifier(FILE) 

        try:
            result = naiveBayesClassifier.classify(df)
            return result
        except Exception as err:
            raise err
    