import sys
m_size = [-1, -1, -1, []]
f = open(sys.argv[1], 'r')

m_size[0] = int(f.readline())
m_size[1] = int(f.readline())
for i in range(0, m_size[0]):
    m_size[3].append((f.readline().replace("\n", "").split(" ")))

def find_coord(h,r,c):
    for i in range(len(h)):
        h[i] = [int(j) for j in h[i]]
    matrix = h
    for i in range(len(h)):
        for j in range(len(h[i])):
            if h[i][j]==1 and i>0 and j>0:
                matrix[i][j] = 0
                matrix[i][j] = min(matrix[i-1][j-1],min(matrix[i][j - 1], matrix[i - 1][j]))+1
                if m_size[2] < matrix[i][j]: m_size[2] = matrix[i][j]
    if  m_size[2] <= 1:  print("0 0")
    else:
     for x in range(len(matrix)):
        if m_size[2] in matrix[x]:
           print(str(x - m_size[2] + 1) + " " + str(matrix[x].index(m_size[2]) - m_size[2] + 1))

find_coord(m_size[3], m_size[0], m_size[1])
