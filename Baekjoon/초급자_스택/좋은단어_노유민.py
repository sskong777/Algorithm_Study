n=int(input())

word_list=[]
for i in range(n):
    word_list.append(input())

stack=[]
count=0

for i in range(n):
    for j in range(len(word_list[i])):
        if len(stack)==0:
            stack.append(word_list[i][j])
        else:
            if stack[-1]==word_list[i][j]:
                stack.pop()
            else:
                stack.append(word_list[i][j])

    if len(stack)==0:
        count+=1
        stack=[]
    else:
        stack=[]   
print(count)
