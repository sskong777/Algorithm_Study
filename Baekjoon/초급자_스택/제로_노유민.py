n=int(input())

list_n=[]

for i in range(n):
    num=int(input())
    if num==0:
        list_n.pop()
    else:
        list_n.append(num)


'''
list_input=[]
for i in range(n):
    list_input.append(int(input()))

list_answer=[]
for i in range(len(list_input)):
    if list_input[i]==0:
        list_answer.pop()
    else:
        list_answer.append(list_input[i])
'''
print(sum(list_n))
