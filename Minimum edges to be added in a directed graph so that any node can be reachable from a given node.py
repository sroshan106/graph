
def count(node,d,visit):
    visited = visit.copy()
    queue=[]
    temp=[]
    queue.append(node)
    visited[node]=1
    counter=0
    while queue:
        counter+=1
        x= queue.pop()
        temp.append(x)
        if x in d:
            arr = d[x]
            for i in arr:
                if visited[i]==0:
                    queue.append(i)
                    visited[i]=1
    return temp


def groups(node,visited,d):
    queue=[]
    queue.append(node)
    visited[node]=1
    while queue:
        x = queue.pop()
        if x in d:
            arr = d[x]
            for i in arr:
                if visited[i]==0:
                    queue.append(i)
                    visited[i]=1


def compute(source,n,d):
    good=[0]*n
    badVertices = {}
    temp=0
    groups(source,good,d)
    for i in range(n):
        if good[i]==0:
            badVertices[i]=count(i,d,good)
    badVertices = sorted(badVertices.items(),key=lambda x: len (x[1] ) ,reverse=True)
    counter=0
    #print(badVertices)
    for i in badVertices:
        a,b = i
        if good[a]==0:
            counter+=1
            good[a]=1
            for j in b:
                good[j]=1
    return counter
    
t = int(input())
for _ in range(t):
    n,m,source = list(map(int,input().rstrip().split(" ")))
    source-=1
    d={}
    for i in range(m):
        a,b = list(map(int,input().rstrip().split(" ")))
        a-=1
        b-=1
        if a not in d:
            d[a]=[b]
        else:
            d[a].append(b)
    print(compute(source,n,d))
