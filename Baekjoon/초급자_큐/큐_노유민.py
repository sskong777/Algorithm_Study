def push(x):
    list_que.append(x)

def pop():
    if empty()==1:
        return -1
    return list_que.pop(0)

def size():
    return len(list_que)

def empty():
    if len(list_que)==0:
        return 1
    else:
        return 0
    
def front():
    if empty()==1:
        return -1
    return list_que[0]

def back():
    if empty()==1:
        return -1
    return list_que[-1]


n= int(input())


list_que=[]

quest=[]
for i in range(n):
    quest.append(input().split())


for i in range(len(quest)):
    if len(quest[i])>1:
        push(int(quest[i][1]))
    else:
        if quest[i][0]=='pop':
            print(pop())
        elif quest[i][0]=='size':
            print(size())
        elif quest[i][0]=='empty':
            print(empty())
        elif quest[i][0]=='front':
            print(front())
        elif quest[i][0]=='back':
            print(back())