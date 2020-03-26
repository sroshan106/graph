from collections import defaultdict
graph = defaultdict(list)

def addEdge(graph,u,v):
    graph[u].append(v)

def generate(graph):
    l=[]
    for node in graph:
        for neighbour in graph[node]:
            l.append((node,neighbour))
    return l


def find_path(graph,start, end, path =[]): 
  path = path+[start]
  print(path)
  if start == end: 
    return path

  for node in graph[start]: 
    if node not in path: 
      newpath = find_path(graph,node, end, path) 
      if newpath:  
        return newpath 
      return None



def find_all_path(graph,start, end, path =[]):
path = path+[start]
    print(path)
    if start == end: 
        return path

    for node in graph[start]: 
        if node not in path: 
          newpath = find_path(graph,node, end, path) 
          if newpath:  
            return newpath 
          return None

    
addEdge(graph,'u','v')
addEdge(graph,'v','b')

print(graph)

print(generate(graph))
print(find_path(graph,'u','b'))
print(find_all_path(graph,'u','b'))











