from fastapi import FastAPI
from src.infra.schema.ClassificationRequest import ClassificationRequest
from src.infra.controllers.ClassificationController import ClassificationController


# Inicializando a aplicação FastAPI
app = FastAPI()

@app.get("/")
async def hello_word():
    return {"message": "Hello World"}


# Rota para a classificação
@app.post("/classify")
async def classify_text(request: ClassificationRequest):
    return ClassificationController.classify(request)

print(f'App running on http://localhost:8000)')