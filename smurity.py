def grid_search(G, P, R, r):
    found_instances = []
    match = False
    
    # Search for the first row of P in G. Save all the instances.
    for p in range(R):
        if G[p].find(P[0]) != -1:
            match = True
            # Append Row & Column for each instance found
            found_instances.append((p, G[p].find(P[0])))
    
    # Lambda function to fetch data from a row of G to match  a row of P.
    searchG = lambda row, column: G[row][column:(column + c)]
    
    if match:
        for instance in found_instances:
            row, column = instance[0], instance[1]
            subG = []
            # Create a subset of G to match with P.
            for q in range(r):
                subG.append(searchG(row, column)) 
                row+=1
                
            # Found at least one instance of P in G
            if subG == P:
                break
        # No instance matches the pattern
        else:
            match = False
    
    if match:
        print("YES")
    else:
        print("NO")

# User input formatting
initit = lambda x: int(x)

t = int(input())
while t > 0:
    d = input()
    R, C = map(initit, d.split(" "))
    
    G = []
    for row in range(R):
        i = input()
        G.append(i)
    
    d = input()
    r, c = map(initit, d.split(" "))
    
    P = []
    for row in range(r):
        i = input()
        P.append(i)
        
    grid_search(G, P, R, r)
    t-=1