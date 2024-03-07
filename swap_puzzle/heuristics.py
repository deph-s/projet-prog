from grid import Grid

def manhattan_distance(p,q,m,n):
        g = Grid(1,1)
        acc = 0 
        g1 = g.id_to_grid(p,m,n)
        g2 = g.id_to_grid(q,m,n)
        for i in range(m):
            for j in range(n):
                acc += abs(g1.state[i][j] - g2.state[i][j])
        return acc

def supnorm(p,q,m,n):
    g = Grid(1,1)
    g1 = g.id_to_grid(p,m,n)
    g2 = g.id_to_grid(q,m,n)
    m = 0
    for i in range(m):
            for j in range(n):
                v = abs(g1.state[i][j] - g2.state[i][j])
                if v > m:
                    m = v
    return m

def maxswap_h(p,q,m,n): # Heuristique qui renvoie le nombre maximal de swaps à faire pour mettre un nombre à la bonne place dans la grid
    g = Grid(1,1)
    g1 = g.id_to_grid(p,m,n)
    g2 = g.id_to_grid(q,m,n)
    h = 0
    for i in range(m):
        for j in range(n):
            v = g1.state[i][j]
            for k in range(m):
                for l in range(n):
                    if g2.state[k][l] == v:
                        val = abs(i-k) + abs(j-l)
                        if val > h:
                            h = val
    return h

def hash_h(p,q,m,n): # Utiliser la fonction de hash elle même comme heuristique par différence
    return p-q