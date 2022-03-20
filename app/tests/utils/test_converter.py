from pydantic import BaseModel

from app import utils


class TestModelConverter:

    def test_to_cypher_object(self):

        class User(BaseModel):
            name: str
            description: str
            price: str
            tax: str

        user = {
            "name": 'name0',
            "description": 'description1',
            "price": 'price2',
            "tax": 'tax3'
        }

        modelConverter = utils.modelConverter.to_cypher_object(User(**user))
        assert modelConverter == \
            '{name: "name0",description: "description1",price: "price2",tax: "tax3"}'
