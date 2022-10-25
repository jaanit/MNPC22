s = input()
re = 0
count = 0
max = 0
ct = 0
for i in range(1,((len(s)//2))+1):
    s1 = s[i:]
    s2 = s[:len(s)-i]
    for j in range(len(s1)):
        if s1[j] == s2[j]:
            count+=1
    re +=1
    if count>max:
        max = count
        ct = i
    count = 0
print(max,ct)