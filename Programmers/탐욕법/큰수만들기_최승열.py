def solution(number, k):
    st = []
    for n in number:
        while st and k and st[-1] < n:
            st.pop()
            k -= 1
        st.append(n)
    return "".join(st[:-k] if k else st)