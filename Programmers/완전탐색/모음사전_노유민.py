from itertools import product
def solution(word):
    answer = 0
    result = []
    li = ['A','E','I','O','U']
    for i in range(1,6):
        productLists = list(product(li,repeat = i))

        result += [''.join(map(str, productList)) for productList in productLists]
    result.sort()
    
    for i in result:
        answer+=1
        if i==word:
            break
        
    return answer