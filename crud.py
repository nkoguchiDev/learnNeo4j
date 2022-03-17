from config import settings
from neo4j import GraphDatabase

driver = GraphDatabase.driver(
    f"neo4j://{settings.GRAPH_DB_HOST}:{settings.GRAPH_DB_PORT}",
    auth=(settings.GRAPH_DB_USER,
          settings.GRAPH_DB_PASSWORD))


class User:
    id = 'test'
    email = 'email'
    hashed_password = 'test'


def create(db: GraphDatabase) -> list:
    query = f"""
                CREATE ({settings.USER_NODE_NAME}:{settings.USER_NODE_LABEL}
                        {{
                            id: 'test',
                            email: 'email',
                            hashed_password: 'test'
                        }}
                        )
                        RETURN {settings.USER_NODE_NAME}
                """
    result = db.run(query)
    return result.data()


if __name__ == '__main__':
    user = User()
    for key in user.__dict__.keys():
        print(key)
