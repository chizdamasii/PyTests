"""
In some cities, the sewage system does not work properly and every time it rains, water accumulates on the streets and in between buildings, blocking traffic and causing distress.

You have an N number of buildings and an array with the height of every building.

You want to find out what is the maximum volume of water that would hypothetically accumulate after heavy rain, in between 2 buildings.

Input: N > 0 on the first line, array of N integer elements on the second line.

Output: integer positive X units of water.

Example: The following sequence of heights will generate the structure below:

Sequence: 1 2 1 5 2 4 1 0 1 2 6 4 5 2 3 4 1 2

The biggest block of water would contain 20 units of water.
"""
import fileinput

def get_input():
        f = fileinput.input()
        n = int(next(f))
        height = [int(i) for i in next(f).strip('\n').split()]
        return n,height

def main():
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

if __name__ == '__main__':
        main()
