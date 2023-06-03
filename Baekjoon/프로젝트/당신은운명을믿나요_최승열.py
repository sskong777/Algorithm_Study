# [27930] 당신은 운명을 믿나요?
# https://www.acmicpc.net/problem/27930
K="KOREA"
Y="YONSEI"
for s in input():
  if not (K and Y):break
  if s==K[0]: K=K[1:]
  if s==Y[0]: Y=Y[1:]
print("YONSEI" if K else "KOREA")