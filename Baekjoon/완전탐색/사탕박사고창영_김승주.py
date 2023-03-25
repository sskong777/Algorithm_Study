
t = int(input())

def check_is_candies(i,j):
    if candies[i][j]=='>' and j < c-2:
        if candies[i][j+1]=='o' and candies[i][j+2] =='<':
            return True
        else:
            return False
    else:
        if i < r-2 and candies[i][j]=='v' and candies[i+1][j]=='o' and candies[i+2][j]=='^':
            return True
        else:
            return False


for test in range(t):
    input()

    r, c = map(int,input().split())
    
    candies = []

    for i in range(r):
        inputs = list(input())
        candies.append(inputs)

    count =0
    for i in range(r):
        for j in range(c):
            if candies[i][j] == '>' or candies[i][j] == 'v':
                if check_is_candies(i,j):
                    count+=1
    print(count)