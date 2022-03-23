import uuid

from pydantic import BaseModel
from neo4j import GraphDatabase

from app.core.config import settings
from app.schemas.user import UserInDB
from app import utils


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

    def create(self, db: GraphDatabase, user: UserInDB) -> list:
        query = f"""
                CREATE ({settings.USER_NODE_NAME}:{settings.USER_NODE_LABEL}
                        {utils.modelConverter.to_cypher_object(user)})
                RETURN {settings.USER_NODE_NAME}
                """
        result = db.run(query)
        return [record.get(settings.USER_NODE_NAME)
                for record in result.data()]

    def update_by_email(
            self,
            db: GraphDatabase,
            email: str,
            update_email: str) -> list:
        query = f"""
                MATCH ({settings.USER_NODE_NAME}:{settings.USER_NODE_LABEL})
                WHERE {settings.USER_NODE_NAME}.email='{email}'
                SET {settings.USER_NODE_NAME}.email='{update_email}'
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
