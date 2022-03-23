from app.core.security import (create_access_token,
                               verify_password,
                               get_password_hash)
from app.core.config import settings
from app.core import security
from app.schemas.token import TokenPayload

from uuid import uuid4
from jose import jwt, exceptions

import pytest


def test_create_access_token():
    _id = uuid4().hex
    token = create_access_token(_id)
    payload = jwt.decode(
        token, settings.SECRET_KEY, algorithms=[security.ALGORITHM]
    )
    token_data = TokenPayload(**payload)
    assert _id == token_data.sub


def test_faild_create_access_token():
    _id = uuid4().hex
    token = create_access_token(_id)
    with pytest.raises(exceptions.JWTError):
        jwt.decode(
            token[:-1], settings.SECRET_KEY, algorithms=[security.ALGORITHM]
        )
