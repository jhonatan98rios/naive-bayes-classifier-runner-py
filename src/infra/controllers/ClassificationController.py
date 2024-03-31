from src.infra.providers.S3Provider import S3Provider
from src.infra.repository.MongoDBRepository import MongoDBRepository
from src.domain.service.ClassificationService import ClassificationService
from src.infra.schema.ClassificationRequest import ClassificationRequest
import json

class ClassificationController:
    @staticmethod
    def classify(request: ClassificationRequest):

        classifierRepository = MongoDBRepository()
        storageProvider = S3Provider()
    
        classificationService = ClassificationService(
            classifierRepository=classifierRepository,
            storageProvider=storageProvider
        )

        return classificationService.execute(request.id, request.sample)
        