import fileinput

def get_input():
        f = fileinput.input()
        n = int(next(f))
        height = [int(i) for i in next(f).strip('\n').split()]
        return n,height

n, height = get_input()
i = [0, len(height)-1,0,0,0,0]
while(i[0] <i[1]):
    if (height[i[0]] < height[i[1]]):
        i[5] = 0
        i[3] = max(i[3], height[i[0]])
        i[4] += i[3] - height[i[0]]
        if  (i[4] >0 and i[2]==i[4]): i[4] = 0
        else: i[2]= max(i[2],i[4])
        i[0] += 1
    else:
        i[4] = 0
        i[3] = max(i[3], height[i[1]])
        i[5] += i[3] - height[i[1]]
        if (i[5] > 0 and i[2] == i[5]): i[5] = 0
        else: i[2] = max(i[2], i[5])
        i[1] -= 1
print(i[2] )

