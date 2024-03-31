from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv.main import load_dotenv
import os

load_dotenv()

DATABASE_USER=os.environ['DATABASE_USER']
DATABASE_PASS=os.environ['DATABASE_PASS']
DATABASE_HOST=os.environ['DATABASE_HOST']
DATABASE_NAME=os.environ['DATABASE_NAME']

class MongoDBRepository:
    def __init__(self):
        self.connection()
        
    def connection(self):
        try:
            uri = f"mongodb+srv://{DATABASE_USER}:{DATABASE_PASS}@{DATABASE_HOST}/?retryWrites=true&w=majority&appName=ClusterBlog"
            self.client = MongoClient(uri, server_api=ServerApi('1'))
            self.db = self.client["naive-bayes-classifier-database"]
            self.collection = self.db["classifiers"]

        except Exception:
            raise Exception("Connection Error")

    def readOneById(self, document_id: str):
        try:
            document = self.collection.find_one({"id": document_id})
            return document
        except Exception:
            raise Exception(f"Erro ao ler documento por ID: {document_id}")


    def readAll(self):
        try:
            cursor = self.collection.find()
            print(cursor)
            return cursor
        except Exception:
            raise Exception("Erro ao ler todos os documentos")
