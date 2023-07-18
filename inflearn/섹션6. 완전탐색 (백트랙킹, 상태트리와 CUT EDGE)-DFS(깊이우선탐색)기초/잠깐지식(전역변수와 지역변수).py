def dfs():
    global a
    a = a + [4] # 얘는 오류남, 그래서 a가 전역변수라고 알려줘야함
    # a[0] = 7 # 얘는 오류 안남
    print(a)

a = [1, 2, 3]
dfs()
print(a)