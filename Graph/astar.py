import heapq

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

    def get_heuristic(self, goal):
        heuristic = {}
        print(f"\n--- Enter Heuristic values (h) for each vertex (Goal '{goal}' = 0) ---")
        for v in self.vertices:
            if v == goal:
                heuristic[v] = 0
            else:
                while True:
                    try:
                        heuristic[v] = int(input(f"  h({v}): "))
                        break
                    except ValueError:
                        print("Enter a valid integer")
        return heuristic

    def astar(self, start, goal):
        if start not in self.vertices or goal not in self.vertices:
            print("Start or Goal vertex not in graph.")
            return

        h = self.get_heuristic(goal)

        # priority queue: (f, g, node, path)
        frontier = [(h[start], 0, start, [start])]
        explored = []
        itr = 1

        print(f"\n{'Iter':<10} | {'Frontier (node:f)':<35} | {'Explored'}")
        print("-" * 70)

        while frontier:
            frontier_view = [(n, f) for f, g, n, _ in sorted(frontier)]
            print(f"{itr:<10} | {str(frontier_view):<35} | {explored}")

            f, g, node, path = heapq.heappop(frontier)  # pop lowest f

            if node in explored:
                itr += 1
                continue

            explored.append(node)

            if node == goal:
                print("-" * 70)
                print(f"Goal '{goal}' reached! Path: {' -> '.join(path)}")
                print(f"Total cost (g): {g}")
                return

            for nb, weight in self.vertices[node]:
                if nb not in explored:
                    new_g = g + weight
                    new_f = new_g + h[nb]
                    heapq.heappush(frontier, (new_f, new_g, nb, path + [nb]))

            itr += 1

        print("Goal not reachable.")


g = Graph()
print("\n--- A* MENU ---")
print("1 Add Vertex\n2 Add Edge\n3 Delete Vertex\n4 Delete Edge")
print("5 Display Graph\n6 Display Adjacency List")
print("7 A* Search\n8 Exit")

while True:
    try:
        ch = int(input("Enter choice: "))
    except ValueError:
        print("Enter a valid number")
        continue
    if ch == 1:
        g.add_vertex(input("Vertex: "))
    elif ch == 2:
        g.add_edge(input("From: "), input("To: "), int(input("Cost: ")))
    elif ch == 3:
        g.delete_vertex(input("Vertex: "))
    elif ch == 4:
        g.delete_edge(input("From: "), input("To: "))
    elif ch == 5:
        g.display()
    elif ch == 6:
        g.display_adj(input("Vertex: "))
    elif ch == 7:
        g.astar(input("Start: "), input("Goal: "))
    elif ch == 8:
        print("Program terminated")
        break
    else:
        print("Invalid choice")
