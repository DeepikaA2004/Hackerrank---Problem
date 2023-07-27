if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    g=list(arr)
    mx=max(g)
    c=[]
    for i in range(len(g)):
        if g[i]!=mx:
            c.append(g[i])

    print(max(c))