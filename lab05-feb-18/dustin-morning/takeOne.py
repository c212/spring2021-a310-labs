graph = {
            'seattle':['portland'],
            'san francisco' : ['portland','salt lake city','los angeles'],
            'portland' : ['seattle', 'salt lake city', 'san francisco'],
            'salt lake city' : ['helena','denver', 'las vegas', 'san francisco'],
            'los angeles' : ['san francisco', 'las vegas', 'phoenix', 'el paso']
            }
def shortestPath(stop, candidates):
    print(str(stop))


    if candidates == None: return None
    elif len(candidates) == 0: return []
    else:
        for c in candidates:
            print("    "+str(c))
        print("---")
        for candidate in candidates:
            if candidate[-1]==stop:
                print("here is a solution: "+str(candidate))
                return candidate
        for candidate in candidates:
            newSet = []
            for c in candidates:
                if c[-1] not in graph:
                    print(c[-1]+ "is a dead end so I give up")
                else: 
                    for v in graph[c[-1]]:
                        clone = c[:]
                        if v in clone:
                            pass
                        else:
                            clone = clone + [v]
                            newSet = newSet + [clone]
        return shortestPath(stop, newSet)

shortestPath('los angeles', [['seattle']])
print("Where are you going from?")
for i in range(len(graph)):
    print(list(graph.keys())[i])
number1 = input()
print("Where are you going to?")
for i in range(len(graph)):
    print(list(graph.keys())[i])
number2 = input()

shortestPath('{}'.format(number1), [['{}'.format(number2)]])







