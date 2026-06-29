from dataclasses import dataclass
from datetime import datetime


@dataclass
class Connessione:
    id:str
    id2:str
    peso:str

    def __hash__(self):
        return hash(self.id)
    def __eq__(self, other):
        return self.id == other.id and self.id2 == other.id2
