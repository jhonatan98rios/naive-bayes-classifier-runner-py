from enum import Enum

class STATUS(Enum):
    READY = 'ready'
    INPROGRESS = 'inProgress'
    FAILED = 'failed'

class Classifier:
    def __init__(
        self, id: str, name: str, description: str, size: int, format: str,
        accuracy: float, status: STATUS, rating: int, path: str,
        isPublic: bool, owners: list[str]
    ):
        self.id = id
        self.name = name
        self.description = description
        self.size = size
        self.format = format
        self.accuracy = accuracy
        self.status = status
        self.rating = rating
        self.path = path
        self.isPublic = isPublic
        self.owners = owners