from src.domain.service.ClassificationService import ClassificationService
from src.infra.schema.ClassificationRequest import ClassificationRequest


class ClassificationController:
    @staticmethod
    def classify(request: ClassificationRequest):

        classificationService = ClassificationService()
        return classificationService.execute(request.id, request.sample)
        