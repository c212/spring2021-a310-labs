
graph = {
    'seattle'        : ['portland'                                                                     ],
    'san francisco'  : ['portland'     , 'salt lake city', 'los angeles'                               ],
    'portland'       : ['seattle'      , 'salt lake city', 'san francisco'                             ],
    'salt lake city' : ['helena'       , 'denver'        , 'las vegas'    , 'san francisco', 'portland'],
    'los angeles'    : ['san francisco', 'las vegas'     , 'phoenix'      , 'el paso'                  ],
}

def shortestPath(stop, candidates): 
  if candidates == None: return None
  elif len(candidates) == 0: return []
  else:
    for c in candidates:
      print("  " + str(c))
    print("---")
    for candidate in candidates:
      if candidate[-1] == stop:
        print("here's a solution: " + str(candidate))
        return candidate
    for candidate in candidates: 
      newSet = []
      for c in candidates:
        if c[-1] not in graph: 
          print (c[-1] + " dead end so I give up.")
        else:
          for v in graph[c[-1]]:
            clone = c[:] # create copy (clone) of c
            if v in clone:
              pass
            else:
              clone = clone + [ v ]
              newSet = newSet + [ clone ]
      return shortestPath(stop, newSet);

shortestPath('los angeles', [['seattle']])
