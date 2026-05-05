class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, v):
        if v not in self.vertices:
            self.vertices[v] = []
            print("Vertex added")
        else:
            print("Vertex already exists")

    def add_edge(self, u, v, cost=0):
        if u in self.vertices and v in self.vertices:
            if (v, cost) in self.vertices[u]:
                print("Edge already exists")
            else:
                self.vertices[u].append((v, cost))
                self.vertices[v].append((u, cost))
                print("Edge added")
        else:
            print("Add vertices first")

    def delete_vertex(self, v):
        if v in self.vertices:
            self.vertices.pop(v)
            for n in self.vertices:
                self.vertices[n] = [(x, c) for x, c in self.vertices[n] if x != v]
            print("Vertex deleted")
        else:
            print("Vertex not found")

    def delete_edge(self, u, v):
        if u in self.vertices:
            before = len(self.vertices[u])
            self.vertices[u] = [(x, c) for x, c in self.vertices[u] if x != v]
            self.vertices[v] = [(x, c) for x, c in self.vertices[v] if x != u]
            if len(self.vertices[u]) < before:
                print("Edge deleted")
            else:
                print("Edge not found")
        else:
            print("Edge not found")

    def display(self):
        print("\nGraph:")
        for v in self.vertices:
            print(v, "-", self.vertices[v])

    def display_adj(self, v):
        if v in self.vertices:
            print(v, "-", self.vertices[v])
        else:
            print("Vertex not found")

    def dfs_lr(self, start, goal=None):
        if start == goal:
            print(f"Start is goal! Path: {start}")
            return
        explored = set()
        stack = [(start, [start])]
        itr = 1
        print(f"\n{'Iter':<10} | {'Stack':<30} | {'Explored'}")
        print("-" * 60)
        while stack:
            print(f"{itr:<10} | {str([x[0] for x in stack]):<30} | {sorted(explored)}")
            node, path = stack.pop()  # LIFO - pop from end
            if node not in explored:
                explored.add(node)
                if node == goal:
                    print(f"\nGoal '{goal}' reached! Path: {' -> '.join(path)}")
                    return
                for nb, _ in reversed(self.vertices[node]):
                    if nb not in explored and nb not in [x[0] for x in stack]:
                        stack.append((nb, path + [nb]))
            itr += 1
        print(f"\nGoal '{goal}' not found.")

    def dfs_rl(self, start, goal=None):
        if start == goal:
            print(f"Start is goal! Path: {start}")
            return
        explored = set()
        stack = [(start, [start])]
        itr = 1
        print(f"\n{'Iter':<10} | {'Stack':<30} | {'Explored'}")
        print("-" * 60)
        while stack:
            print(f"{itr:<10} | {str([x[0] for x in stack]):<30} | {sorted(explored)}")
            node, path = stack.pop()  # LIFO - pop from end
            if node not in explored:
                explored.add(node)
                if node == goal:
                    print(f"\nGoal '{goal}' reached! Path: {' -> '.join(path)}")
                    return
                for nb, _ in self.vertices[node]:
                    if nb not in explored and nb not in [x[0] for x in stack]:
                        stack.append((nb, path + [nb]))
            itr += 1
        print(f"\nGoal '{goal}' not found.")


g = Graph()
print("\n--- DFS MENU ---")
print("1 Add Vertex\n2 Add Edge\n3 Delete Vertex\n4 Delete Edge")
print("5 Display Graph\n6 Display Adjacency List")
print("7 DFS Left to Right\n8 DFS Right to Left\n9 Exit")

while True:
    try:
        ch = int(input("Enter choice: "))
    except ValueError:
        print("Enter a valid number")
        continue
    if ch == 1:
        g.add_vertex(input("Vertex: "))
    elif ch == 2:
        g.add_edge(input("From: "), input("To: "), int(input("Cost (0 if none): ")))
    elif ch == 3:
        g.delete_vertex(input("Vertex: "))
    elif ch == 4:
        g.delete_edge(input("From: "), input("To: "))
    elif ch == 5:
        g.display()
    elif ch == 6:
        g.display_adj(input("Vertex: "))
    elif ch == 7:
        g.dfs_lr(input("Start: "), input("Goal: "))
    elif ch == 8:
        g.dfs_rl(input("Start: "), input("Goal: "))
    elif ch == 9:
        print("Program terminated")
        break
    else:
        print("Invalid choice")
