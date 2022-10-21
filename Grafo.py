import networkx as nx
import matplotlib.pyplot as plt

#Determinando os vértices e as arestas
nodes = [1,2,3,4,5,6,7,8,9,10]
edges = [(1,4,{'weight': 20}), (1,5,{'weight': 20}),
        (1,6,{'weight': 5}),(1,7,{'weight': 5}),
        (1,2,{'weight': 10}),(2,4,{'weight': 10}),
        (2,3,{'weight': 5}),(3,2,{'weight': 15}),
        (3,4,{'weight': 5}),(4,5,{'weight': 10}),
        (5,6,{'weight': 5}),(7,6,{'weight': 10}),
        (8,7,{'weight': 5}),(8,1,{'weight': 5}),
        (8,2,{'weight': 20}),(9,2,{'weight': 15}),
        (9,8,{'weight': 20}),(9,10,{'weight': 10}),
        (10,2,{'weight': 5}),(10,3,{'weight': 15})]

#Criando o Grafo
G = nx.DiGraph()
G.add_nodes_from(nodes)
G.add_edges_from(edges)

# Letra a)
mi = nx.incidence_matrix(G,nodelist=nodes,edgelist=edges) #Matriz de Incidência
print(mi.todense())

# Letra b)
ma = nx.adjacency_matrix(G,nodelist=nodes,weight=None) #Matriz de adjacência
print(ma.todense())

# Letra c) // Lista dos Vértices e Arestas
print(list(G.nodes)) 
print(list(G.edges))

# Letra d)
mw = nx.adjacency_matrix(G,nodelist=nodes) #Matriz dos pesos
print(mw.todense())

# Letra e)
print(G.has_edge(1,4)) #Caso os vértices inseridos estejam conectados retornarar True, caso contrário, False

# Letra f) // Desenho do grafo sem peso
nx.draw(G, with_labels=1)
plt.savefig("simpleGraph.png")
plt.close()

# Letra g) // Desenho do grafo com peso
pos = nx.spring_layout(G, seed=7)

nx.draw(G,pos,with_labels=1)
nx.draw_networkx_edge_labels(
    G,pos,
    edge_labels= {(1,4):'20',(1,5):'20',(1,6):'5',(1,7):'5',(1,2):'10',
                (2,4):'10',(2,3):'5',(3,2):'15',(3,4):'5',(4,5):'10',
                (5,6):'5',(7,6):'10',(8,7):'5',(8,1):'5',(8,2):'20',
                (9,2):'15',(9,8):'20',(9,10):'10',(10,2):'5',(10,3):'15'},
    font_color='red'
)

plt.savefig("weightGraph.png")

# Letra h)
def isDirected(g):
    if(nx.is_directed(g)):
        print("O grafo é direcionado")
    else:
        print("O grafo não é direcionado")

isDirected(G) #Determina se o grafo criado é direcionado ou não

# Letra i)
def getWeight(u,v):
    if(G.has_edge(u,v)):
        print(G.get_edge_data(u,v))
    else:
        print("Aresta não encontrada")

getWeight(1,4) #Retorna o peso, caso existente, entre dois vértices
