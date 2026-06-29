
from model.model import Model

model=Model()
print(len(model._allRating))
model.buildGraphPesato(9,10)
print("Num nodi:", model.getNumNodi())
print("Num archi:", model.getNumArchi())
