class ModelConverter:
    def __init__(self, model):
        self.model = model.__dict__

    def to_cypher_object(self):
        key_values = [
            f'{key}: "{self.model.get(key)}"'
            for key in list(self.model.keys())
        ]
        return f'{{{",".join(key_values)}}}'
