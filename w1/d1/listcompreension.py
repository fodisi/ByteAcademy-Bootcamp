x = 1
y = 1
z = 1
n = 2

print([ [i, j, r] for i in range(x + 1) for j in range(y + 1) for r in range(z + 1) if ( (i + j + r) != n) ])
