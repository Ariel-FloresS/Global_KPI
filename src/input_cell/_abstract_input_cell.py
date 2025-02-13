from abc import ABC, abstractmethod
from typing import Union

class AbstractInputCell(ABC):
    def __init__(self):
        self.status_cell = False

    @abstractmethod
    def input(self)->Union[int,str]:
        raise NotImplementedError('This Method must be implemented by a subclass.')
    
    