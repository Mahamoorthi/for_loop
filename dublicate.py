arr = [2,5,8,10,2]
s = set()
result = []
for i in arr:
    if i not in s:
        s.add(i)
        result.append(i)
print(result)