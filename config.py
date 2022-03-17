from pydantic import BaseSettings


class Settings(BaseSettings):
    MESSAGE: str = "Hello FASTAPI"
    GRAPH_DB_USER: str = "neo4j"
    GRAPH_DB_PASSWORD: str = "neo4jj"
    GRAPH_DB_HOST: str = "localhost"
    GRAPH_DB_PORT: int = 7687
    USER_NODE_NAME: str = "user"
    USER_NODE_LABEL: str = "User"


settings = Settings()
