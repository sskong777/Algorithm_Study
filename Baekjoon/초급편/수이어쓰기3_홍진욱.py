target = int(input())
sample_data = ''
for i in range(1,target+1):
    sample_data += str(i)
print(sample_data.find(str(target))+1)