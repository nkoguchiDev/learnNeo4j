import uuid

from pydantic import BaseModel

from app.core.config import settings
from app.utils.converter import ModelConverter
from app import crud


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


class TestCRUDUser:

    def test_create(self, db):
        result = crud.user.create(db, User(**_user))
        assert result[0]['name'] == _user['name']

    def test_get_by_email(self, db):
        result = crud.user.get_by_email(db, email=_user['email'])

        assert len(result) == 1
        assert result[0]['email'] == _user['email']

    def test_delete_by_email(self, db):
        crud.user.delete_by_email(db, email=_user['email'])
        result = crud.user.get_by_email(db, email=_user['email'])
        assert len(result) == 0
