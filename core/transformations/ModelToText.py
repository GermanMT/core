from abc import ABC, abstractmethod
from core.transformations.AbstractTransformation import Transformation


class ModelToText(Transformation):
    
    @abstractmethod
    def register(self, extension, metamodel):
        pass

    @abstractmethod
    def transform(self):
        pass
