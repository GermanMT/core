from abc import ABC, abstractmethod


class Operation():
    @abstractmethod
    def execute(self,model):
        pass