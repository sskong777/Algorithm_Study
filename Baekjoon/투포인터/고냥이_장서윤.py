N = int(input())
S = input()

s, e = 0, 1
len_max = -1
len_c = 1
a = dict()
a[S[s]] = 1


def check(alp):
    if alp not in a.keys():
        return False
    else:
        return True


while s < e < len(S):

    if (len(a.keys()) == N and check(S[e])) or (len(a.keys()) < N):
        a[S[e]] = 1
        e += 1
        len_c += 1
        if len_c == len(S):
            len_max = len_c

    else:
        len_max = max(len_max, len_c)
        a.clear()

        if e == len(S) - 1:
            break
        else:
            s += 1
            e = s + 1
            a[S[s]] = 1
            len_c = 1

print(len_max)
