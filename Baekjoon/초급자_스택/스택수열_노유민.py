def stack_list(n,list_que):
    point=0
    answer_list=[]
    temp=[]
    for i in range(n):
        if list_que[i]>=point:
            while(list_que[i]>=point):
                if list_que[i]==point:
                    answer_list.append("-")
                    temp.pop()
                    break
                point+=1
                temp.append(point)
                answer_list.append("+")     
        if list_que[i]<point:
            if list_que[i]==temp[-1]:
                answer_list.append("-")
                temp.pop()
            else:
                return "NO"
    return answer_list
n=int(input())

list_que=[]
for i in range(n):
    list_que.append(int(input()))

result=stack_list(n,list_que)

if result=='NO':
    print(result)
else:
    for i in result:
        print(i)