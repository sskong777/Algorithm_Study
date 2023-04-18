'''n, m = map(int, input().split())
ans = []

def back():
    if len(ans) == m:
        print('========================')
        print("성공")
        print(" ".join(map(str, ans)))
        return
    for i in range(1, n+1):
        print(f'i : {i} , ans : {ans}')
        if i not in ans:
            print('***********************')
            print(f'if문 속의 i : {i} , ans : {ans}')
            ans.append(i)
            print(f'추가한 뒤 ans : {ans}')
            print("한바퀴 돈다")
            print('************************')
            back()
            ans.pop()

back()
'''


n, m = map(int, input().split())
ans = []

def back():

    # ans 리스트의 길이가 m과 같으면 함수 실행을 종료하고 ans를 출력합니다.
    if len(ans) == m:
        print(" ".join(map(str, ans)))
        return

    # 1부터 n까지의 숫자를 탐색하면서 ans 리스트에 없는 숫자를 추가합니다.
    for i in range(1, n+1):

        # ans 리스트에 i가 없으면 i를 추가합니다.
        if i not in ans:

            # i를 ans 리스트에 추가합니다.
            ans.append(i)

            # 재귀 호출로 back 함수를 다시 호출합니다.
            back()
            # 재귀 호출이 끝나면 마지막에 추가된 i를 ans 리스트에서 제거합니다.
            ans.pop()

back()
