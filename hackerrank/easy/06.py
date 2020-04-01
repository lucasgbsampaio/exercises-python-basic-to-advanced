"""
Let's learn about list comprehensions!
You are given three integers X,Y and Z representing the dimensions of a cuboid along with an integer N.
You have to print a list of all possible coordinates given by (i,j,k) on a 3D grid where the sum of i+j+k is not equal to N.
Here, 0<= i <= x; 0<= j <= y; 0<= k <= z
"""

x = int(input().strip())
y = int(input().strip())
z = int(input().strip())
n = int(input().strip())

print([[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if ((i+j+k) != n)])
