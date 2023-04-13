import sys
input = sys.stdin.readline

a, b, c = map(int, input().strip().split())
a_cards = sorted(list(map(int, input().strip().split())))
b_cards = sorted(list(map(int, input().strip().split())))
c_cards = sorted(list(map(int, input().strip().split())))

def binary_search(target, arr):
    min_d = 1e9
    left, right = 0, len(arr)-1
    result = 0
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return target
        if abs(arr[mid] - target) < min_d:
            result = arr[mid]
            min_d = abs(arr[mid] - target)
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result

min_value = 1e9
for card_a in a_cards:
    card_b = binary_search(card_a, b_cards)
    card_c_1 = binary_search(card_a, c_cards)
    card_c_2 = binary_search(card_b, c_cards)
    min_value = min(min_value, abs(max(card_a, card_b, card_c_1) - min(card_a, card_b, card_c_1)))
    min_value = min(min_value, abs(max(card_a, card_b, card_c_2) - min(card_a, card_b, card_c_2)))

print(min_value)