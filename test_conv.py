from pydantic import BaseModel

from conv import ModelConverter


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

        modelConverter = ModelConverter(User(**user))
        assert modelConverter.to_cypher_object(
        ) == '{name: "name0",description: "description1",price: "price2",tax: "tax3"}'
