class Graph:
    def __init__(self):
        self.graph = {}

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []
            print("Node added")
        else:
            print("Node already exists")

    def add_edge(self, u, v, cost=0):
        if u in self.graph and v in self.graph:
            if (v, cost) in self.graph[u]:
                print("Edge already exists")
            else:
                self.graph[u].append((v, cost))
                self.graph[v].append((u, cost))
                print("Edge added")
        else:
            print("Add nodes first")

    def delete_node(self, node):
        if node in self.graph:
            self.graph.pop(node)
            for n in self.graph:
                self.graph[n] = [(x, c) for x, c in self.graph[n] if x != node]
            print("Node deleted")
        else:
            print("Node not found")

    def delete_edge(self, u, v):
        if u in self.graph:
            before = len(self.graph[u])
            self.graph[u] = [(x, c) for x, c in self.graph[u] if x != v]
            self.graph[v] = [(x, c) for x, c in self.graph[v] if x != u]
            if len(self.graph[u]) < before:
                print("Edge deleted")
            else:
                print("Edge not found")
        else:
            print("Edge not found")

    def display(self):
        print("\nGraph:")
        for node in self.graph:
            print(node, "-", self.graph[node])

    def display_adj(self, node):
        if node in self.graph:
            print(node, "-", self.graph[node])
        else:
            print("Node not found")

    def dfs(self, start, goal, rtl=True):
        if start not in self.graph:
            print("Error: Start node not found")
            return
        if goal not in self.graph:
            print("Error: Goal node not found")
            return

        stack = [start]
        explored = []
        parent = {start: None}

        itr = 1
        print("\nIter | Stack | Explored")
        print("-" * 40)

        while stack:
            print(f"{itr:>4} | {stack} | {explored}")
            itr += 1

            node = stack.pop()
            if node not in explored:
                explored.append(node)

                if node == goal:
                    path = []
                    temp = goal
                    while temp is not None:
                        path.append(temp)
                        temp = parent[temp]
                    path.reverse()
                    print("\nExplored Order:", explored)
                    print("Path:", " -> ".join(path))
                    return

                children = sorted([child for child, _ in self.graph[node]], reverse=rtl)
                for child in children:
                    if child not in parent:
                        stack.append(child)
                        parent[child] = node

        print("Error: Goal not reachable")


g = Graph()
print("\n--- DFS MENU ---")
print("1 Add Node\n2 Add Edge\n3 Delete Node\n4 Delete Edge")
print("5 Display Graph\n6 Display Adjacency List")
print("7 DFS Left to Right\n8 DFS Right to Left\n9 Exit")

while True:
    try:
        ch = int(input("Enter choice: "))
    except ValueError:
        print("Enter a valid number")
        continue
    if ch == 1:
        g.add_node(input("Node: "))
    elif ch == 2:
        g.add_edge(input("From: "), input("To: "), int(input("Cost (0 if none): ")))
    elif ch == 3:
        g.delete_node(input("Node: "))
    elif ch == 4:
        g.delete_edge(input("From: "), input("To: "))
    elif ch == 5:
        g.display()
    elif ch == 6:
        g.display_adj(input("Node: "))
    elif ch == 7:
        g.dfs(input("Start: "), input("Goal: "), rtl=False)  # Left to Right
    elif ch == 8:
        g.dfs(input("Start: "), input("Goal: "), rtl=True)   # Right to Left
    elif ch == 9:
        print("Program terminated")
        break
    else:
        print("Invalid choice")
