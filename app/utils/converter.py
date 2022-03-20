class ModelConverter:
    def __init__(self):
        pass

    def to_cypher_object(self, model):
        model_dict = model.dict()
        key_values = [
            f'{key}: "{model_dict.get(key)}"'
            for key in list(model_dict.keys())
        ]
        return f'{{{",".join(key_values)}}}'


modelConverter = ModelConverter()
