from typing import Any, Dict
from pydantic import BaseModel

# Definindo a classe do modelo para a entrada da requisição
class ClassificationRequest(BaseModel):
    id: str
    sample: Dict[str, Any]