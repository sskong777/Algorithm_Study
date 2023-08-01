from collections import deque
def solution(n, wires):
    tot = int(1e9)
    for a, b in wires:
        tmp = wires[:]
        tmp.remove([a, b])
        aset = {a}
        bset = {b}
        tmp = deque(tmp)
        while tmp:
            c, d = tmp.popleft()
            if c in aset:
                aset.add(d)
            elif d in aset:
                aset.add(c)
            elif c in bset:
                bset.add(d)
            elif d in bset:
                bset.add(c)
            else:
                tmp.append([c, d])
        tot = min(tot, abs(len(aset)-len(bset)))
            
    return tot