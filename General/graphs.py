

class Graph():

    def __init__(self,):
        self.graph = {}
        self.nodes = []
    
    def add_edge(self, source, dest):
        
        if source not in self.graph:
            self.graph[source] = []
            self.nodes.append(source)

        if dest not in self.graph:
            self.graph[dest] = []
            self.nodes.append(dest)
        

        if dest not in self.graph[source]:
            self.graph[source].append(dest)
        
    def bfs(self, start):
        q = [start]
        seen = set()
        seen.add(start)
        print(start)

        while len(q) > 0:
            for node in self.graph[q.pop(0)]:
                if node not in seen:
                    q.append(node)
                    seen.add(node)
                    print(node)
        

    def dfs(self, start):
        stack = [start]
        seen = set()
        seen.add(start)

        while len(stack) > 0:
            node = stack.pop()
            print(node)
            for n in self.graph[node]:
                if n not in seen:
                    seen.add(n)
                    stack.append(n)
    

    def print(self,):
        print(f"Nodes: {self.nodes}")
        for src, dest in self.graph.items():
            print(f"{src} -> ", end='')
            for node in dest:
                print(f"{node}, ", end='')
            print("")





if __name__ == "__main__":
    graph = Graph()
    graph.add_edge(1,2)
    graph.add_edge(3,6)
    graph.add_edge(2,3)
    graph.add_edge(2,1)
    graph.add_edge(1,4)
    graph.add_edge(3,5)
    graph.add_edge(3,6)
    graph.add_edge(6,7)
    graph.add_edge(7,8)
    graph.add_edge(4,9)
    graph.add_edge(9,10)

    graph.bfs(1)