import sys
import math

s = input()
match = 0
mv = 0
move =0
for i in range(1,(len(s)+1)):
    match = 0
    so = s[i:]
    s1 = s[:len(s)-i]
    for j in range(len(s1)):
        if so[j]==s1[j]:
            match+=1
    if match > mv:
        mv = match
        move=i
print(mv,move)
