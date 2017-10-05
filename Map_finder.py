""" You want to find a previously undiscovered island.

How do you that? By scanning satellite footage.

Let’s say that a satellite photo is represented by a binary MxN matrix of 0 and 1 where 0 represents water and 1 land.

You want to discover an island represented only by 1s with the maximum perimeter.
In other words, you have to find out the maximum size square Matrix matrix with all 1s.

The output should be the starting position of the island or islands.

Keep in mind that multiple islands can be identified.

If multiple squares will be identified then the positions found should be displayed in the order they were found by iterating through the matrix row after row.
If no island is found, then the output should be: 0 0.
We consider an island to be composed of at least 4 elements.


Input: M, N – integers, A[M,N] of {0,1}

Output: I(x,y) – the starting position of the square(s).


Examples:

For M = N = 4 and A[4][4]
1 1 1 1
1 0 0 1
0 1 1 1
1 0 0 1
The output is 0 0."""

import sys
mSize = [-1,-1,-1,[]]
f = open(sys.argv[1], 'r')

mSize[0] = int(f.readline())
mSize[1] = int(f.readline())
for i in range(0,mSize[0]):
    mSize[3].append((f.readline().replace("\n","").split(" ")))

def findTheCoord(h,r,c):
    for i in range(len(h)):
        h[i] = [int(j) for j in h[i]]
    Matrix = h
    for i in range(len(h)):
        for j in range(len(h[i])):
            if h[i][j]==1 and i>0 and j>0:
                Matrix[i][j] = 0
                Matrix[i][j] = min(Matrix[i-1][j-1],min(Matrix[i][j - 1], Matrix[i - 1][j]))+1
                if mSize[2] < Matrix[i][j]: mSize[2] = Matrix[i][j]
    if  mSize[2] <= 1:  print("0 0")
    else:
     for x in range(len(Matrix)):
        if mSize[2] in Matrix[x]:
           print(str(x - mSize[2]+1)+" "+str(Matrix[x].index(mSize[2])- mSize[2]+1))


findTheCoord(mSize[3],mSize[0],mSize[1])



