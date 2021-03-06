class Node(object):
    def __init__(self, data = None, adj = []):
        self.data = data
        self.adj = adj
        self.state = State.UNVISITED
    def __str__(self):
        return str(self.data)
    def __repr__(self):
        return self.__str__()

class Graph(object):
    def __init__(self, nodes = []):
        self.nodes = nodes

class State:
    UNVISITED = 0
    VISITING = 1
    VISITED = 2

def BuildOrder(G):
    order = []
    for node in G.nodes:
        if node.state == State.UNVISITED:
            if not DFS(node, order):
                print "Not a DAG"
                return
    for i in range(len(order)-1, -1, -1):
        print order[i],

def DFS(root, order):
    root.state = State.VISITING
    for node in root.adj:
        if node.state == State.UNVISITED:
            if not DFS(node, order):
                return False
        # cycle
        elif node.state == State.VISITING:
            return False
    root.state = State.VISITED
    order.append(root)
    return True

if __name__ == '__main__':
    na = Node('a')
    nb = Node('b')
    nc = Node('c')
    nd = Node('d')
    ne = Node('e')
    nf = Node('f')
    na.adj = [nd]
    nb.adj = [nd]
    #nc.adj = [na]
    nd.adj = [nc]
    nf.adj = [na, nb]
    G = Graph()
    G.nodes = [na, nb, nc, nd, ne, nf]
    BuildOrder(G)
    
