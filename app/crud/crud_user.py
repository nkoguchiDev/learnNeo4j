import uuid

from pydantic import BaseModel
from neo4j import GraphDatabase

from app.core.config import settings
from app import utils


class User(BaseModel):
    id: str
    name: str
    email: str
    description: str
    price: str
    tax: str


_user = {
    "id": uuid.uuid4().hex,
    "name": 'name0',
    "email": 'email1',
    "description": 'description1',
    "price": 'price2',
    "tax": 'tax3'
}


class CRUDUser:

    def __init__(self):
        pass

    def get_by_email(self, db: GraphDatabase, email: str) -> list:
        query = f"""
                MATCH ({settings.USER_NODE_NAME}:{settings.USER_NODE_LABEL})
                WHERE {settings.USER_NODE_NAME}.email='{email}'
                RETURN {settings.USER_NODE_NAME}
                """
        result = db.run(query)
        return [record.get(settings.USER_NODE_NAME)
                for record in result.data()]

    def create(self, db: GraphDatabase, user: User) -> list:
        modelConverter = utils.modelConverter.to_cypher_object(user)
        query = f"""
                CREATE ({settings.USER_NODE_NAME}:{settings.USER_NODE_LABEL}
                        {modelConverter.to_cypher_object()})
                RETURN {settings.USER_NODE_NAME}
                """
        result = db.run(query)
        return [record.get(settings.USER_NODE_NAME)
                for record in result.data()]

    def delete_by_email(self, db: GraphDatabase, email: str) -> None:
        query = f"""
                MATCH({settings.USER_NODE_NAME}:{settings.USER_NODE_LABEL})
                WHERE {settings.USER_NODE_NAME}.email='{email}'
                DELETE {settings.USER_NODE_NAME}
                """
        db.run(query)


user = CRUDUser()
