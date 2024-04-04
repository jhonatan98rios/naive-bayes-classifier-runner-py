from fastapi import FastAPI
from src.infra.schema.ClassificationRequest import ClassificationRequest
from src.infra.controllers.ClassificationController import ClassificationController

# Inicializando a aplicação FastAPI
app = FastAPI()


# Rota para a classificação
@app.post("/num-classify")
async def classify_text(request: ClassificationRequest):
    return ClassificationController.classify(request)


print(f'App running on http://localhost:8000)')

# uvicorn src.main:app --reload