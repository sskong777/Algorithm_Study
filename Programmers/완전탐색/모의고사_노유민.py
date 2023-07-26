def solution(answers):
    answer = []
    length = len(answers)
    num1=0
    list1 = [1,2,3,4,5]
    num2=0
    list2 = [2,1,2,3,2,4,2,5]
    num3=0
    list3 = [3,3,1,1,2,2,4,4,5,5]
    maxNum = 0
    for i in range(length):
        if answers[i]==list1[i%5]:
            num1+=1
    maxNum=num1
    answer.append(1)
    for i in range(length):
        if answers[i]==list2[i%8]:
            num2+=1
    if maxNum<num2:
        maxNum=num2
        answer.pop()
        answer.append(2)
    else:
        if maxNum==num2:
            answer.append(2)
    for i in range(length):
        if answers[i]==list3[i%10]:
            num3+=1
    
    if maxNum<num3:
        for i in range(len(answer)):
            answer.pop()
        answer.append(3)
    else:
        if maxNum==num3:
            answer.append(3)
    return answer