def solution(clothes):
    clothes_hash = {}
    for cloth, cloth_type in clothes:
        clothes_hash[cloth_type] = clothes_hash.get(cloth_type , 0 ) + 1
    ans = 1
    for cloth_type in clothes_hash:
        ans *= (clothes_hash[cloth_type]+1)
    return ans-1 