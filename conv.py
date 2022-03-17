from pydantic import BaseModel


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

if __name__ == '__main__':
    _user = User(**user).__dict__

    t = [f'{i}: "{_user.get(i)}"' for i in list(User(**user).__dict__.keys())]
    data_str = f'{{{",".join(t)}}}'
    print(data_str)
