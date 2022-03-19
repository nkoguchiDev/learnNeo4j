from cgi import test
from curses.ascii import US
import uuid
from config import settings
from conv import ModelConverter

from neo4j import GraphDatabase
from pydantic import BaseModel


driver = GraphDatabase.driver(
    f"neo4j://{settings.GRAPH_DB_HOST}:{settings.GRAPH_DB_PORT}",
    auth=(settings.GRAPH_DB_USER,
          settings.GRAPH_DB_PASSWORD))


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
        modelConverter = ModelConverter(user)
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


if __name__ == '__main__':
    cRUDUser = CRUDUser()
    print(cRUDUser.create(driver.session(), User(**_user)))
    print(cRUDUser.get_by_email(driver.session(), "email1"))
    cRUDUser.delete_by_email(driver.session(), "email1")
