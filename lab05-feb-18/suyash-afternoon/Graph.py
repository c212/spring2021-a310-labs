class Graph:
    def __init__(self):
        self.graph = {}

    def insert(self, source, destination):
        # destination is a list
        for dest in destination:
            if source in self.graph.keys():
                if dest in self.graph[source]:
                    pass
                else:
                    self.graph[source].append(dest)
            else:
                self.graph[source] = [dest]

    def shortestPath(self, stop, candidates):

        print(str(stop))

        if candidates == None:
            return None
        elif len(candidates) == 0:
            return []
        else:

            for c in candidates:
                print("     ", str(c))
            print("******")

            for candidate in candidates:
                if candidate[-1] == stop:
                    print(" Solution is : ", str(candidate))
                    return candidate
            newSet = []

            for c in candidates:
                if c[-1] not in self.graph:
                    print(c[-1], " is a dead end in the graph")
                else:
                    for v in self.graph[c[-1]]:
                        clone = c[:]
                        if v in clone:
                            pass
                        else:
                            clone = clone + [v]
                            newSet = newSet + [clone]
            return self.shortestPath(stop, newSet)


g = Graph()

g.insert('seattle', ['portland'])
g.insert('san francisco', ['portland', 'salt lake city', 'los angeles'])
g.insert('portland', ['seattle', 'salt lake city', 'san francisco'])
g.insert('salt lake city', ['helena', 'denver', 'las vegas', 'san francisco', 'portland'])
g.insert('los angeles', ['san francisco', 'las vegas', 'phoenix', 'el paso'])

print(g.graph)

g.shortestPath('seattle', [['los angeles']])