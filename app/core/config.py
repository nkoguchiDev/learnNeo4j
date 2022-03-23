from pydantic import BaseSettings


class Settings(BaseSettings):
    MESSAGE: str = "Hello FASTAPI"
    GRAPH_DB_USER: str = "neo4j"
    GRAPH_DB_PASSWORD: str = "neo4jj"
    GRAPH_DB_HOST: str = "localhost"
    GRAPH_DB_PORT: int = 7687
    USER_NODE_NAME: str = "user"
    USER_NODE_LABEL: str = "User"

    SECRET_KEY = "cce45e4c8450c2781ff1f2e1436cd61fb49c730f5b74b7b4824ca09d77eb89c3"
    ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 8


settings = Settings()
