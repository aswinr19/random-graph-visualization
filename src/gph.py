"""
We have graph represented as adjacency list using python dictionary and list. Generate a visual graph
from this data (e.g., use dot library/tool or convert this data to json/javascript and use some
javascript graph viz library). Generate random graphs for development/testing. Screencast code walkthrough.
"""

import random
import graphviz


class Grph:
    def __init__(self):
        self.adj_list = {}
        self.n = random.randrange(5, 10)
        self.p = random.uniform(0, 1) * 0.999 + 0.0005 # random probability between 0 and 1
        self.visited = []

        print(self.n, self.p)

    # traverse through all nodes in the graph 
    def bfs(self, start):
        queue = []
        queue.append(start)
        self.visited.append(start)
      
        popped = queue.pop(0)
        print(popped)
        while(len(queue) != 0):

            for elm in self.adj_list[popped]:
                if elm not in self.visited:
                    queue.append(elm)
                    self.visited.append(elm)

    def generate(self):
        random_edges = []

        # using Erdős–Rényi model G(n,p)
        connected_vertices = set()

        for i in range(1, self.n):
            for j in range(i + 1, self.n + 1):
                if random.random() < self.p:
                    random_edges.append((i, j))
                    connected_vertices.add(i)

        non_isolated_edges = []

        print(connected_vertices)

        for u, v in random_edges:
            if u in connected_vertices and v in connected_vertices:
                non_isolated_edges.append((str(u), str(v)))

        print(f"random edges: {non_isolated_edges}")
        self.edges = non_isolated_edges

        for start, end in self.edges:
            if end not in self.adj_list.get(start, []) and start != end:
                if start in self.adj_list:
                    self.adj_list[start].append(end)
                else:
                    self.adj_list[start] = [end]

        #print("bfs")
        #self.bfs(random.choice(self.edges))

    def rendr(self):

        g = graphviz.Digraph("Graph", filename="output.gv", engine="sfdp")

        for vertex, edges in self.adj_list.items():
            g.node(str(vertex))
            for edge in edges:
                g.edge(str(vertex), str(edge))

        g.render("output", format="png", view=False)


def main():

    grph = Grph()
    grph.generate()
    grph.rendr()


if __name__ == "__main__":
    main() 
