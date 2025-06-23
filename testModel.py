from model.model import Model

mymodel = Model()
mymodel.buildGraph()
print(f"N nodi: {mymodel.getNumNodes()}; N edges: {mymodel.getNumEdges()}")