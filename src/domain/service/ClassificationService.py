from typing import Any, Dict
import pandas as pd
from src.infra.providers.S3Provider import S3Provider
from src.infra.repository.MongoDBRepository import MongoDBRepository
from src.infra.Gateway.NaiveBayesClassifier import NaiveBayesClassifier
from src.utils.handle import handle

class ClassificationService:
    def __init__(
            self, classifierRepository: MongoDBRepository, 
            storageProvider: S3Provider
        ):
        self.classifierRepository = classifierRepository
        self.storageProvider = storageProvider
    
    def execute(self, id: str, sample: Dict[str, Any]):

        # Read One By ID
        classifier = self.classifierRepository.readOneById(id)
        if classifier is None:
            raise Exception(f"Invalid ID: {id}")
        

        # Get Object from S3
        file = self.storageProvider.getObject(classifier['path'])
        if file is None:
            raise Exception(f"Invalid file: {id}")
        
        # Recover the classifier
        naiveBayesClassifier = NaiveBayesClassifier(file) 
        df = pd.DataFrame(sample, index=[0])

        try:
            result = naiveBayesClassifier.classify(df)
            return result
        except Exception as err:
            raise err
    