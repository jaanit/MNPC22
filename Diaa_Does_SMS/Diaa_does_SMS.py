t = int(input())
l = []
di = []
re =0
for i in range(t):
    l.append(input().split(','))
region = int(input())
for _ in range(region):
    reg, num = input().split(',')
    for n in l:
        if (n[0] == num):
            print(','.join(map(str, n)),reg, sep=',')
            re = 1
if re == 0:
    print("nomatch")