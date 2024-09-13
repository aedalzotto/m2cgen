class ModelAssembler:

    def __init__(self, model):
        self.model = model

    def assemble(self):
        raise NotImplementedError

    def get_feature_types(self):
        return None

    def get_feature_names(self):
        return None
